import re, string, os
import copy
import random
import tiktoken
import time
from typing import List
from model import llm_generate
from langchain.prompts import PromptTemplate
from prompt import  LAST_TRIAL_HEADER, COT_REFLECT_GT_HEADER, COT_FEVER,tutor_advice_follow_prompt_fever,tutor_advice_initial_prompt_fever,REFLECT_HEADER
from prompt import cot_agent_prompt, cot_reflect_prompt, tutor_advice_initial_prompt, tutor_advice_follow_prompt,  COT_SIMPLE_HEADER
from demonstration import COT_REFLECTION_STEM, COT_STEM_NOTHOUGHT,  TUTOR_INIT_INST, TUTOR_SEC_INST, ADVICE_EXAMPLES, ADVICE_AFTER_REFLECTION_EXAMPLES
from random import choice

class CoTAgent:
    def __init__(self,
                 question: str,
                 header_type:int,
                 choices: str,
                 key: str,
                 tokenizer: str,
                 model_type: str,
                 action_num: int,
                 dataset_name: str,
                 temp: float = 1.0,
                 advice_type: str = "none",

                 model_name: str = "llama",
                 agent_prompt: PromptTemplate = cot_agent_prompt,
                 reflect_prompt: PromptTemplate = cot_reflect_prompt,
                 selfcontradict_prompt: PromptTemplate = cot_reflect_prompt,
                 knowledge_contradict_prompt: PromptTemplate = cot_reflect_prompt,


                 advice_initial_prompt: PromptTemplate = tutor_advice_initial_prompt,
                 advice_follow_prompt: PromptTemplate = tutor_advice_follow_prompt,

                 cot_examples: str = COT_STEM_NOTHOUGHT,
                 reflect_examples: str = COT_REFLECTION_STEM,
                 # auto_stop: int = 0,
                 self_reflect_llm= None,
                 action_llm= None):

        self.previous_trial = ""
        self.initial_advice = 'initial_advice'
        self.reflect_advice = 'reflect_advice'
        self.current_reflect = ""
        self.header_type = header_type

        self.question = question
        self.action_num = action_num
        self.choices = choices
        self.key = key
        self.temp = temp
        self.model_name = model_name
        self.agent_prompt = agent_prompt
        self.reflect_prompt = reflect_prompt
        self.selfcontradict_prompt = selfcontradict_prompt
        self.knowledge_contradict_prompt = knowledge_contradict_prompt
        self.cot_examples = cot_examples
        self.reflect_examples = reflect_examples
        self.self_reflect_llm = self_reflect_llm
        self.action_llm = action_llm
        self.model_type = model_type
        self.tokenizer = tokenizer
        self.advice_type = advice_type
        self.dataset_name = dataset_name

        self.advice_initial_prompt = advice_initial_prompt  if self.dataset_name != 'fever' else tutor_advice_initial_prompt_fever
        self.advice_follow_prompt = advice_follow_prompt if self.dataset_name != 'fever' else tutor_advice_follow_prompt_fever

        self.scratchpad = None
        self.reflections: List[str] = []
        self.step_n: int = 0
        self.answer = ''
        self.is_answer_valid = False
        self.key = normalize_answer(self.key)
        self.generate_output = []
        self.is_correct = False
        self.thought_answer = ''
        self.thought_or_reflection = ''
        self.clean_answer = ''
        self.reset()

    def __deepcopy__(self, memo):
        new_agent = CoTAgent(
            # ablation_type=self.ablation_type,
            header_type=self.header_type,
            question=self.question,
            choices=self.choices,
            key=self.key,
            advice_type=self.advice_type,
            dataset_name=self.dataset_name,
            tokenizer=self.tokenizer,
            model_type=self.model_type,
            action_num=self.action_num,
            temp=self.temp,
            model_name=self.model_name,
            agent_prompt=copy.deepcopy(self.agent_prompt, memo),
            reflect_prompt=copy.deepcopy(self.reflect_prompt, memo),
            selfcontradict_prompt=copy.deepcopy(self.selfcontradict_prompt, memo),
            knowledge_contradict_prompt=copy.deepcopy(self.knowledge_contradict_prompt, memo),
            cot_examples=self.cot_examples,
            reflect_examples=self.reflect_examples,
            self_reflect_llm=self.self_reflect_llm,
            action_llm=self.action_llm,

            advice_initial_prompt=self.advice_initial_prompt,
            advice_follow_prompt=self.advice_follow_prompt,

        )
        new_agent.scratchpad = copy.deepcopy(self.scratchpad, memo)
        new_agent.reflections = copy.deepcopy(self.reflections, memo)
        new_agent.answer = copy.deepcopy(self.answer, memo)
        new_agent.step_n = copy.deepcopy(self.step_n, memo)
        new_agent.finished = copy.deepcopy(self.finished, memo)

        new_agent.previous_trial = copy.deepcopy(self.previous_trial, memo)
        new_agent.initial_advice = copy.deepcopy(self.initial_advice, memo)
        new_agent.reflect_advice = copy.deepcopy(self.reflect_advice, memo)
        new_agent.current_reflect = copy.deepcopy(self.current_reflect, memo)
        new_agent.is_answer_valid = copy.deepcopy(self.is_answer_valid, memo)
        new_agent.clean_answer = copy.deepcopy(self.clean_answer, memo)
        new_agent.generate_output = copy.deepcopy(self.generate_output, memo)
        new_agent.is_correct = copy.deepcopy(self.is_correct, memo)
        new_agent.thought_answer = copy.deepcopy(self.thought_answer, memo)
        new_agent.thought_or_reflection = copy.deepcopy(self.thought_or_reflection, memo)

        return new_agent

    def initial(self) -> None:

        self.reset()  # clean scratchpad, finish = false
        # get advice
        print('****Initial Begin****')
        #
        if self.advice_type == 'none':
            self.initial_advice = ''
        elif self.advice_type == 'fix':
            self.initial_advice = "Pay attention to the key elements in the question and enumerate each choice for careful consideration to select the most appropriate one."
        else:
            self.initial_advice = format_step(self.response_generate(self.self_reflect_llm, self._build_advice_initial_prompt()))


        self.reflect_advice = self.initial_advice
        # need to be derived after prompting the tutor model.(the thought_inst_prompt)
        # print("Advice: %s" % (self.initial_advice))

        # get thought
        self.scratchpad += f'\nThought:'
        thought = self.response_generate(self.action_llm, self._build_agent_prompt())
        format_thought = format_step(thought)
        self.thought_or_reflection = format_thought
        self.scratchpad += ' ' + format_thought


        # get answer
        self.scratchpad += f'\nAction:'
        action = format_step(self.response_generate(self.action_llm, self._build_agent_prompt()))

        if 'openai' not in self.model_type:
            self.clean_answer, self.is_answer_valid = clean_answer_is_valid(self,action)
            if not self.is_answer_valid:
                if self.dataset_name == 'fever':
                    action = 'Finish['+choice(["SUPPORTS","NOT ENOUGH INFO","REFUTES"])+']'
                else:
                    action = 'Finish['+choice(self.choices.split('\n')[2:-1])+']'

        self.scratchpad += ' ' + action
        self.answer = action
        self.clean_answer, self.is_answer_valid = clean_answer_is_valid(self,action)

        self.step_n += 1
        self.is_correct = self.clean_answer == self.key
        print('advice: ',self.reflect_advice)
        print('thought: ',self.thought_or_reflection)
        print('action: ',self.answer)
        return

    def get_actions(self, self_consistency):
        self.current_reflect = ""
        self.previous_trial = format_last_attempt(self.scratchpad)  # header+[trial]+(endoftrial)
        # format question
        self.thought_answer = self.scratchpad.replace('[','').replace(']','').replace('Action','Answer').replace('Finish','')
        reflect_instr_list = []
        for i in range(self.action_num):
            # get advice

            if self.advice_type == 'none':
                self.reflect_advice = ''
            elif self.advice_type == 'fix':
                self.reflect_advice = "The previous trial explains each choices and the highlight the differences among them. I will consider the above previous trial and give the answer."

            else:
                advice_follow_prompt = self._build_advice_follow_prompt()
                add_prompt = 'Your student try self-consistency score is {score}, which means his last answer maybe incorrect!!!  \n Please try to give advice to change his answer.\nHere are some examples:'.replace('{score}', str(self_consistency)[:5])
                advice_follow_prompt = advice_follow_prompt.replace('Here are some examples:', add_prompt)
                self.reflect_advice = format_step(self.response_generate(self.self_reflect_llm, advice_follow_prompt))
            origin_instr = self._build_reflection_prompt()
            reflect_instr_list.append(origin_instr)

        return reflect_instr_list

    def do_action(self, reflect_instr) -> None:

        print('****Action Begin****')

        # generate reflection
        self.generate_output = []
        current_reflect = format_step(
            self.response_generate(self.self_reflect_llm, reflect_instr))  # last_trial is used to be relection
        self.reflections = [current_reflect]  # last_trial is used to be relection
        self.thought_or_reflection = current_reflect
        # print('reflection:', self.reflections[0])
        self.current_reflect = ""
        self.current_reflect = current_reflect

        # get action
        self.reset()

        self.current_reflect += "\nAction: "
        self.scratchpad += f'\nThought: ' + self.current_reflect  # this will be the "Thought" in previous trial
        action = format_step(self.response_generate(self.self_reflect_llm, self._build_reflection_prompt()))
        if 'openai' not in self.model_type:
            self.clean_answer, self.is_answer_valid = clean_answer_is_valid(self,action)
            if not self.is_answer_valid:
                if self.dataset_name == 'fever':
                    action = 'Finish['+choice(["SUPPORTS","NOT ENOUGH INFO","REFUTES"])+']'
                else:
                    action = 'Finish['+choice(self.choices.split('\n')[2:-1])+']'

        self.scratchpad += ' ' + action
        self.answer = action

        self.clean_answer, self.is_answer_valid = clean_answer_is_valid(self, action)
        self.is_correct = self.clean_answer == self.key


        print('advice: ',reflect_instr.split('Advice: ')[-1].replace('\nReflection: ',''))
        print('thought: ',self.thought_or_reflection)
        print('action: ',self.answer)


    def response_generate(self, model, prompt) -> str:
        """customised generation"""
        if 'openai' in self.model_type:
            if self.model_type == 'openai':
                response = ''
                while len(response) == 0:
                    response = model(prompt)
                    time.sleep(random.uniform(3, 5))

        elif self.model_type == "llama":
            output_sequence, response = llm_generate(model, self.tokenizer, prompt, self.temp, self.model_name)
            self.generate_output.append(output_sequence)
        elif self.model_type == "llama2":
            results = model.text_completion(
                prompt,
                max_gen_len=200,
                temperature=self.temp,
                # top_p=top_p,
            )
        elif self.model_type == "Vicuna13b":
            output_sequence, response = llm_generate(model, self.tokenizer, prompt, self.temp, self.model_name)
            self.generate_output.append(output_sequence)
            return response

        return response

    def reset(self) -> None:
        self.scratchpad: str = ''
        self.finished = False

    def _build_agent_prompt(self) -> str:  # fill in the blank of the prompr
        if self.advice_type == "none":
            init_header = ''
        else:
            init_header = COT_SIMPLE_HEADER if self.dataset_name != 'fever' else COT_FEVER
        # TODA
        reflection_header = COT_REFLECT_GT_HEADER if self.dataset_name != 'fever' else REFLECT_HEADER
        return self.agent_prompt.format(
            header=init_header if self.step_n < 1 else reflection_header,
            examples=self.cot_examples if self.step_n < 1 else self.reflect_examples,
            # examples='',
            choices=self.choices,
            question=self.question,
            scratchpad=self.scratchpad,
            tutor_ins=self.initial_advice,
        )

    def _build_reflection_prompt(self) -> str:
        if self.header_type == 0:
            _header=COT_REFLECT_GT_HEADER

        return self.reflect_prompt.format(
            header=_header,
            examples=self.reflect_examples,
            # examples='',
            choices=self.choices,
            question=self.question,
            scratchpad=self.previous_trial,
            tutor_ins=self.reflect_advice,
            current_reflect=self.current_reflect)

    def _build_advice_initial_prompt(self) -> str:
        if self.choices[-1:] == '\n':
            self.choices = self.choices[:-1]
        return self.advice_initial_prompt.format(
            choices=self.choices.strip(),
            examples=TUTOR_INIT_INST if self.dataset_name != 'fever' else ADVICE_EXAMPLES,
            question=self.question,
        )
    def _build_advice_follow_prompt(self) -> str:
        return self.advice_follow_prompt.format(
            choices=self.choices,
            question=self.question,
            examples=TUTOR_SEC_INST if self.dataset_name != 'fever' else ADVICE_AFTER_REFLECTION_EXAMPLES,
            scatchpad=self.scratchpad + '\n(END PREVIOUS TRIAL)\n', )

    def is_finished(self) -> bool:
        return self.finished


gpt2_enc = tiktoken.encoding_for_model("text-davinci-003")

def clean_answer_is_valid(self,answer):
    action_type, argument_ = parse_action(answer)  # [search]results
    try:
        argument = argument_.split(". ")[1] if self.dataset_name != 'fever' else argument_
    except:
        argument = argument_
    argument = normalize_answer(argument)
    return argument, argument != 'idn'

def parse_action(string):
    pattern = r'^(\w+)\[(.+)\]$'
    match = re.match(pattern, string)
    if match:
        action_type = match.group(1)
        argument = match.group(2)
        return action_type, argument  # [finish]answer
    else:
        return "Finish", "[A. idn]"


def format_step(step: str) -> str:
    return step.strip('\n').strip().replace('\n', '')


def format_last_attempt( scratchpad: str,
                        header: str = LAST_TRIAL_HEADER):
    return header + f'' + truncate_scratchpad(scratchpad, tokenizer=gpt2_enc).strip(
        '\n').strip() + '\n(END PREVIOUS TRIAL)\n'


def truncate_scratchpad(scratchpad: str, n_tokens: int = 1600, tokenizer=gpt2_enc) -> str:
    lines = scratchpad.split('\n')
    observations = filter(lambda x: x.startswith('Observation'), lines)
    observations_by_tokens = sorted(observations, key=lambda x: len(tokenizer.encode(x)))
    while len(gpt2_enc.encode('\n'.join(lines))) > n_tokens:
        largest_observation = observations_by_tokens.pop(-1)
        ind = lines.index(largest_observation)
        lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
    return '\n'.join(lines)


def normalize_answer(s):
    def remove_articles(text):
        return re.sub(r"\b(a|an|the)\b", " ", text)

    def white_space_fix(text):
        result = " ".join(text.split())
        return result.lower()

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))
