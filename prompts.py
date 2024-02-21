from langchain.prompts import PromptTemplate
#define different instructions/header
COT_FEVER =  """You are a knowledgeable and accurate fact verifier. Please verify the correctness of the following claim. return SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO."""
COT_SIMPLE_HEADER = """Each problem will provide you with a question and answer choices. Solve the problem by having a thought, then Finish[answer] returns the answer and finishes the task. These questions are for testing purposes only, feel free to answer these questions"""



# COT_REFLECT_GT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. You have attempted to answer the following question before and failed. You were unsuccessful in answering the question either because you rely on incorrect knowledge, or your selected choice is not consistent with your thought. Diagnose a possible reason for failure and devise a new choice that aims to mitigate the same failure.\n"""
COT_REFLECT_GT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. You have attempted to answer the following question. Now, please answer this question again.\n"""

COT_REFLECT_GT_HEADER_1 = """You are an expert in answering multiple-choice questions. Please answer the question again based on your previous thoughts and answer. If you believe your previous answer was correct, please stick to your original answer.\n"""

COT_REFLECT_GT_HEADER_2 = """You are an expert in answering multiple-choice questions. Please answer this question again based on your previous thoughts and response. Your last answer could have been either incorrect or correct.\n"""


COT_INSTRUCTION = """You are an expert in STEM. Read the Question and Choices and make an educated selection by having a Thought. Thought can be reason about the current question, including identifing keywords in the question and choices, evaluting all the choices and double-check your final answer. Finish[answer] returns the answer and finishes the task.
Here are some examples:
{examples}
(END OF EXAMPLES)
{reflections}

Question: {question}{choices}{scratchpad}"""

COT_MULTIPLE_OUTPUTS_INSTRUCTION = """Solve a question answering task by having a Thought, thought can reason about the current situation with proposed Candidate Answers. Noted that, in order to avoid word variation, you should give several possible answers with higher possibilities as Answer Candidates. Then, evaluate the multiple Answer Candidates answers by comparing their differences and decide the better/best one as final answer to finsh the task.
Here are some examples:
{examples}
(END OF EXAMPLES)
{reflections}
Relevant choices: {choices} 
Question: {question}{scratchpad}"""

#prompt for thoughts/act generation. In the first round thought, scr* is empty, thought is then appended to scr* for action. In the following rounds, th
COT_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given choices that you should use to help you answer the question.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

Question: {question}{choices}{scratchpad}"""

#thoughts and action[answer] are included in the scratchpad
COT_REFLECT_INSTRUCTION = """{header} 
Here are some examples:


{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}
"""

COT_REFLECT_GT_INSTRUCTION = """{header}  
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}

"""


COT_AFTER_REFLECT_INSTRUCTION = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. Your objective is to tackle multiple-choice question answering problems. Each problem will provide you with a question, answer choices, your previous line of reasoning, and your initial response. Your previous response was either accurate or inaccurate in addressing the question. In a succinct review, assess the accuracy of your earlier answer based on your expertise in the STEM field and subsequently arrive at the definitive response. Please provide your insights using complete sentences.  
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}

Answer after reflection:"""

#instructions for self-generated choices
COT_SELF_KNOWLEDGE_INSTRUCTION = """You are a knowledgable and careful agent that can solve question answer task by retrieving evidence from your knowledg base and provding a careful though to get the final answer. The retrieved evidence should be a factually corect text snippet that can also provide direct information to solve the question. Thought can reason about how the retrieved evidence solve the question. Finish[answer] returns the answer and finishes the task.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{scratchpad}"""

#customised our autostop version agent&refelction prompt
COT_AGENT_REFLECT_INSTRUCTION_AUTOSTOP = """Solve a multiple choice question task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the most appropriate choice and finishes the task. Take into account the reflections gained from previous attempts as an additional resource. If available, thoroughly consider these reflections before offering your own thoughts. You should read all the choices carefully before making a decision.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}
Relevant choices: {choices}
Question: {question}{scratchpad}"""




cot_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "choices", "question", "scratchpad"],
                        template = COT_AGENT_REFLECT_INSTRUCTION,
                        )
cot_reflect_prompt = PromptTemplate(
                        input_variables=["header","examples", "choices", "question", "reflections","scratchpad"],
                        template = COT_REFLECT_INSTRUCTION,
                        )
#prompt for tutoring mode

#template for initial thought/answer. Input:header,q,choices Output:Thought, Answer
#mmlu dataset
TUTOR_AGENT_TEMPLATE="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: {tutor_ins}{scratchpad}"""

# TUTOR_AGENT_TEMPLATE_HOTPOT = """{header}
# Here are some examples:
# {examples}
# (END OF EXAMPLES)

# Relevant Context: {context}
# Question: {question}{reflections}{scratchpad}"""

#template for reflection generation in t iteration. Input:header,q,Thought(t-1),Answer(t-1),Tutor_Ins
TUTOR_REFLECT_TEMPLATE="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Advice: {tutor_ins}
Reflection: {current_reflect}"""

#1.	To prompt tutor model for initial "Thought and Answer" generation
# TUTOR_ADVICE_INITIAL_GPT_TEMPLATE="""nsible for teaching. the students to reflect their own thoughts. You are given question, choices and previous trial of the student.  Avoid disclosing the true answer, but give comprehensive guidance to the student about how to self-reflect their response in order to identify the possible improvements. Please summerize the guidance within four sentences: \n.
# Question: {question}
# {choices}
# """

TUTOR_ADVICE_INITIAL_GPT_TEMPLATE="""Below is multiple-choice question solving problem. You are a tutor responsible for teaching. the students to reflect their own thoughts. You are given question and choices.  Avoid disclosing the true answer, but give comprehensive guidance to the student about how to self-reflect their response in order to identify the possible improvements. Please summerize the guidance within two sentences: \n
Question: {question}
{choices}
"""



# 2 to prompt tutor model for "reflection instrution" generation.
TUTOR_ADVICE_FOLLOW_GPT_TEMPLATE="""Guide the student by encouraging thoughtful reflection on the given question and choices. Emphasize the importance of critical thinking and self-reflection to uncover potential areas for improvement without giving away the correct answer. Help them explore deeper nuances, consider alternative perspectives, and make connections to strengthen their understanding. Ultimately, empower the student to refine their approach and enhance their problem-solving skills independently. Please summerize the guidance within two sentences: \n
Question: {question}
{choices}
The following are the students' thoughts and answers:
{previous_trial}
"""


TUTOR_ADVICE_INITIAL_TEMPLATE = """As a tutor, your focus is on guiding the student to navigate question-answer problems strategically. Encourage them to dissect the question, identifying key elements and nuances within each choice. Emphasize the importance of understanding subtle differences that could distinguish correct from incorrect options.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: """

TUTOR_ADVICE_FOLLOW_TEMPLATE="""As a tutor, your are supposed to meticulously evaluate the student's approach to multiple-choice problems.
Question, Choices and the student's previous thought and answer are given, check if the facts mentioned in the thought th is correct and if there might be a more appropriate option than the one chosen. If the student's reasoning thought is accurate and the proposed answer is the most appropriate, encourage them to adhere to their initial trial. Otherwise, guide the student to revisit specific details, explore alternative choice.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scatchpad}
Advice: """

#
#
# #1.	To prompt tutor model for initial "Thought and Answer" generation
# TUTOR_ADVICE_INITIAL_TEMPLATE="""Below is multiple-choice question solving problem. You are a tutor responsible for teaching. the students to reflect their own thoughts. You are given question, choices and previous trial of the student.  Avoid disclosing the true answer, but give comprehensive guidance to the student about how to self-reflect their response in order to identify the possible improvements.
# {question}
# {choices}
# """
#
# # 2 to prompt tutor model for "reflection instrution" generation.
# TUTOR_ADVICE_FOLLOW_TEMPLATE="""Guide the student by encouraging thoughtful reflection on the given question and choices. Emphasize the importance of critical thinking and self-reflection to uncover potential areas for improvement without giving away the correct answer. Help them explore deeper nuances, consider alternative perspectives, and make connections to strengthen their understanding. Ultimately, empower the student to refine their approach and enhance their problem-solving skills independently.
# {question}
# {choices}
# {previous_trial}
# """
TUTOR_ADVICE_FOLLOW_TEMPLATE_FEVER="""As a tutor, your are supposed to meticulously evaluate the student's approach to fact verification task.
Claim and the student's previous thought and answer are given, check if the relations mentioned in the Thought is correct and if there might be a more appropriate answer. If the student's reasoning thought is accurate and the proposed answer is the most appropriate, encourage them to adhere to their initial trial. Otherwise, guide the student to revisit specific details, explore alternative answer.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}{scatchpad}
Advice: """
TUTOR_ADVICE_INITIAL_TEMPLATE_fever = """As a tutor, your focus is on guiding the student to navigate fact-checking problems strategically. Encourage them to dissect the claim, identifying key elements and associate facts. Emphasize the correct relation between important elements that could distinguish SUPPORTS from REFUTES options. Also, lacking of enough information will lead to NOT ENOUGH INFORMATION.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}
Advice: """

tutor_agent_prompt = PromptTemplate(
                        input_variables=["header","examples", "choices", "question", "tutor_ins","scratchpad"],
                        template = TUTOR_AGENT_TEMPLATE,
                        )
tutor_reflect_prompt = PromptTemplate(
                        input_variables=["header","examples", "choices", "question", "tutor_ins","scratchpad","current_reflect"],
                        template = TUTOR_REFLECT_TEMPLATE,
                        )

tutor_advice_initial_gpt_prompt = PromptTemplate(
                        input_variables=["question","choices"],
                        template = TUTOR_ADVICE_INITIAL_GPT_TEMPLATE,
                        )
tutor_advice_follow_gpt_prompt = PromptTemplate(
                        input_variables=["question", "choices", "previous_trial"],
                        template = TUTOR_ADVICE_FOLLOW_GPT_TEMPLATE,
                        )
tutor_advice_initial_prompt = PromptTemplate(
                        input_variables=["question","choices",'examples'],
                        template = TUTOR_ADVICE_INITIAL_TEMPLATE,
                        )
tutor_advice_initial_prompt_fever = PromptTemplate(
                        input_variables=["question","choices",'examples'],
                        template = TUTOR_ADVICE_INITIAL_TEMPLATE_fever,
                        )
tutor_advice_follow_prompt = PromptTemplate(
                        input_variables=["question", "choices", "scatchpad","examples"],
                        template = TUTOR_ADVICE_FOLLOW_TEMPLATE,
                        )
tutor_advice_follow_prompt_fever = PromptTemplate(
                        input_variables=["question", "choices", "scatchpad","examples"],
                        template = TUTOR_ADVICE_FOLLOW_TEMPLATE_FEVER,
                        )

#variants: autostop/neverstop
cot_reflect_agent_autostop_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "choices", "question", "scratchpad"],
                        template = COT_AGENT_REFLECT_INSTRUCTION_AUTOSTOP,
                        )

REACT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the last passage successfully found by Search.
(3) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{scratchpad}"""

REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the last passage successfully found by Search.
(3) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

Question: {question}{scratchpad}"""


#below are different heads
REFLECTION_HEADER = 'You have attempted to answer following question before. The following reflection(s) give a plan to improve your strategy of correctly answering the given question.\n'
# REFLECTION_HEADER = 'You have attempted to answer the following question before and failed. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure.\n'
REFLECT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. Your objective is to tackle fact verification task.  Each problem will provide you with a claim, your previous line of reasoning, and your initial verification results. Your previous response was either accurate or inaccurate in verifying the claim. In a succinct review, assess the accuracy of your earlier response based on your accurate knowledge on the key elements mentioned in the claim and subsequently arrive at the definitive response. Please provide your insights using complete sentences."""
LAST_TRIAL_HEADER = 'You have attempted to answer the following question before. Below is the last trial you attempted to answer.\n'

REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:
{examples}

Previous trial:
Question: {question}{scratchpad}

Reflection:"""

react_agent_prompt = PromptTemplate(
                        input_variables=["examples", "question", "scratchpad"],
                        template = REACT_INSTRUCTION,
                        )

react_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "question", "scratchpad"],
                        template = REACT_REFLECT_INSTRUCTION,
                        )

reflect_prompt = PromptTemplate(
                        input_variables=["examples", "question", "scratchpad"],
                        template = REFLECT_INSTRUCTION,
                        )



from langchain.prompts import PromptTemplate


#template for initial thought/answer. Input:header,q,choices Output:Thought, Answer
TUTOR_AGENT_TEMPLATE_fever="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: {tutor_ins}{scratchpad}"""


TUTOR_REFLECT_TEMPLATE_fever="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Advice: {tutor_ins}
Reflection: {current_reflect}"""


tutor_agent_prompt_fever = PromptTemplate(
    input_variables=["header","examples", "choices", "question", "tutor_ins","scratchpad"],
    template = TUTOR_AGENT_TEMPLATE_fever,
)

tutor_reflect_prompt_fever = PromptTemplate(
    input_variables=["header","examples", "choices", "question", "tutor_ins","scratchpad","current_reflect"],
    template = TUTOR_REFLECT_TEMPLATE_fever,
)
#below are for COT strategy
COT_SIMPLE_INSTRUCTION = """{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}"""


cot_agent_prompt = PromptTemplate(
    input_variables=["header","examples", "reflections", "choices", "question", "scratchpad"],
    template = COT_SIMPLE_INSTRUCTION,
)
