from langchain.prompts import PromptTemplate

#GT, AutoStop and NeverStop for Reflection Generation in Initial Study
COT_REFLECT_INSTRUCTION_AUTOSTOP = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant choices and a question to answer. Upon thorough deliberation, you have the option to adhere to your existing answer or analyze potential reasons for an incorrect response. Failure may stem from an inaccurate guess indicated by 'Finish[<answer>]' or there is a better choice than your answer. When your current response is the best, elucidate the rationale. Conversely, if the answer is not appropriate in some way, Diagnose a possible reason for failure and devise a new, better choice to avoid the same failure. Use complete sentences.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Reflection: """

COT_REFLECT_INSTRUCTION_NEVERSTOP = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant choices and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a better choice than your provided answer. Diagnose a possible reason for failure and devise a new, better choice to avoid the same failure. Use complete sentences.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Reflection:"""

COT_REFLECT_GT_INSTRUCTION = """COT_REFLECT_GT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. You have attempted to answer the following question before and failed. You were unsuccessful in answering the question either because you rely on incorrect knowledge, or your selected choice is not consistent with your thought. Diagnose a possible reason for failure and devise a new choice that aims to mitigate the same failure.\n""" 
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Reflection:"""


cot_reflect_autostop_prompt= PromptTemplate(
                        input_variables=["examples", "choices", "question","scratchpad"],
                        template = COT_REFLECT_INSTRUCTION_AUTOSTOP,
)
cot_reflect_never_prompt= PromptTemplate(
                        input_variables=["examples", "choices", "question","scratchpad"],
                        template = COT_REFLECT_INSTRUCTION_NEVERSTOP,
)
cot_reflect_gt_prompt= PromptTemplate(
                        input_variables=["examples", "choices", "question","scratchpad"],
                        template = COT_REFLECT_INSTRUCTION_GT,
)



#Different Header/Instructions
COT_FEVER =  """You are a knowledgeable and accurate fact verifier. Please verify the correctness of the following claim. return SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO."""
COT_SIMPLE_HEADER = """Each problem will provide you with a question and answer choices. Solve the problem by having a thought, then Finish[answer] returns the answer and finishes the task. These questions are for testing purposes only, feel free to answer these questions"""



# COT_REFLECT_GT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. You have attempted to answer the following question before and failed. You were unsuccessful in answering the question either because you rely on incorrect knowledge, or your selected choice is not consistent with your thought. Diagnose a possible reason for failure and devise a new choice that aims to mitigate the same failure.\n"""
COT_REFLECT_GT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. You have attempted to answer the following question. Now, please answer this question again.\n"""

COT_INSTRUCTION = """You are an expert in Multiple-Choice question answering task. Read the Question and Choices and make an educated selection by having a Thought. Thought can be reason about the current question, including identifing keywords in the question and choices, evaluting all the choices and double-check your final answer. Finish[answer] returns the answer and finishes the task.
Here are some examples:
{examples}
(END OF EXAMPLES)
{reflections}

Question: {question}{choices}{scratchpad}"""



COT_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given choices that you should use to help you answer the question.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

Question: {question}{choices}{scratchpad}
"""

COT_REFLECT_INSTRUCTION = """{header} 
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}
"""


#Prompt without Advice 
#Response generation
cot_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "choices", "question", "scratchpad"],
                        template = COT_AGENT_REFLECT_INSTRUCTION,
                        )
#Reflection generation
cot_reflect_prompt = PromptTemplate(
                        input_variables=["header","examples", "choices", "question", "reflections","scratchpad"],
                        template = COT_REFLECT_INSTRUCTION,
                        )


#Prompt with Advice 
#Advice Generation--MMLU dataset
#Initial Advice Generation (GPT35)
TUTOR_ADVICE_INITIAL_GPT_TEMPLATE="""Below is multiple-choice question solving problem. You are a tutor responsible for teaching. the students to reflect their own thoughts. You are given question and choices.  Avoid disclosing the true answer, but give comprehensive guidance to the student about how to self-reflect their response in order to identify the possible improvements. Please summerize the guidance within two sentences: \n
Question: {question}
{choices}
"""
#Reflection Advice Generation (GPT35)
TUTOR_ADVICE_FOLLOW_GPT_TEMPLATE="""Guide the student by encouraging thoughtful reflection on the given question and choices. Emphasize the importance of critical thinking and self-reflection to uncover potential areas for improvement without giving away the correct answer. Help them explore deeper nuances, consider alternative perspectives, and make connections to strengthen their understanding. Ultimately, empower the student to refine their approach and enhance their problem-solving skills independently. Please summerize the guidance within two sentences: \n
Question: {question}
{choices}
The following are the students' thoughts and answers:
{previous_trial}
"""
# Advice Generation--FEVER dataset
TUTOR_ADVICE_INITIAL_TEMPLATE_fever = """As a tutor, your focus is on guiding the student to navigate fact-checking problems strategically. Encourage them to dissect the claim, identifying key elements and associate facts. Emphasize the correct relation between important elements that could distinguish SUPPORTS from REFUTES options. Also, lacking of enough information will lead to NOT ENOUGH INFORMATION.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}
Advice: """
TUTOR_ADVICE_FOLLOW_TEMPLATE_FEVER="""As a tutor, your are supposed to meticulously evaluate the student's approach to fact verification task.
Claim and the student's previous thought and answer are given, check if the relations mentioned in the Thought is correct and if there might be a more appropriate answer. If the student's reasoning thought is accurate and the proposed answer is the most appropriate, encourage them to adhere to their initial trial. Otherwise, guide the student to revisit specific details, explore alternative answer.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}{scatchpad}
Advice: """

#Initial Response Generation (MMLU&FEVER)
TUTOR_AGENT_TEMPLATE="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: {tutor_ins}{scratchpad}"""

#Reflection Generation (MMLU&FEVER)
TUTOR_REFLECT_TEMPLATE="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Advice: {tutor_ins}
Reflection: {current_reflect}"""



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





#below are different HEADER
REFLECTION_HEADER = 'You have attempted to answer following question before. The following reflection(s) give a plan to improve your strategy of correctly answering the given question.\n'
# REFLECTION_HEADER = 'You have attempted to answer the following question before and failed. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure.\n'
REFLECT_HEADER = """You're an advanced reasoning agent capable of self-reflection and continuous improvement. Your objective is to tackle fact verification task.  Each problem will provide you with a claim, your previous line of reasoning, and your initial verification results. Your previous response was either accurate or inaccurate in verifying the claim. In a succinct review, assess the accuracy of your earlier response based on your accurate knowledge on the key elements mentioned in the claim and subsequently arrive at the definitive response. Please provide your insights using complete sentences."""
LAST_TRIAL_HEADER = 'You have attempted to answer the following question before. Below is the last trial you attempted to answer.\n'



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
