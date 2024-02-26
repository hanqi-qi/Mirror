from langchain.prompts import PromptTemplate

LAST_TRIAL_HEADER = 'You have attempted to answer the following question before. Below is the last trial you attempted to answer.\n'
COT_REFLECT_GT_HEADER = """You’re an advanced reasoning agent capable of self-reflection and continuous improvement. Your objective is to tackle multiple-choice question answering problems. Each problem will provide you with a question, answer choices, your previous line of reasoning, and the detailed analyses from an experienced tutor. In a succinct review, assess the accuracy of your earlier answer based on your expertise and the advice, subsequently arrive at the definitive response."""
COT_FEVER =  """You are a knowledgeable and accurate fact verifier. Please verify the correctness of the following claim based on your expertise and provided advice. Return SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO."""
REFLECT_HEADER = """You’re an advanced reasoning agent capable of self-reflection in fact verification task. Claim and the your previous response and answer are given, along with the advice. In a succinct review, assess the accuracy of your earlier answer based on your expertise and the advice, subsequently arrive at the definitive response."""
COT_SIMPLE_HEADER = """You are an expert in multiple-choice question answering. Each problem will provide you with a question and answer choices. Read the question and all the choices carefully, along with the provided advice, and solve the problem by having a thought. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task."""




# template for initial thought/answer. Input:header,q,choices Output:Thought, Answer
TUTOR_AGENT_TEMPLATE_fever = """{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: {tutor_ins}{scratchpad}"""

tutor_agent_prompt_fever = PromptTemplate(
    input_variables=["header", "examples", "choices", "question", "tutor_ins", "scratchpad"],
    template=TUTOR_AGENT_TEMPLATE_fever,
)

# template for reflection. Input:header,q,choices,thought,answer Output:Reflection
TUTOR_REFLECT_TEMPLATE_fever = """{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Advice: {tutor_ins}
Reflection: {current_reflect}"""

tutor_reflect_prompt_fever = PromptTemplate(
    input_variables=["header", "examples", "choices", "question", "tutor_ins", "scratchpad", "current_reflect"],
    template=TUTOR_REFLECT_TEMPLATE_fever,
)

# Initial Response Generation (MMLU&FEVER)
TUTOR_AGENT_TEMPLATE = """{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: {tutor_ins}{scratchpad}"""

tutor_agent_prompt = PromptTemplate(
    input_variables=["header", "examples", "choices", "question", "tutor_ins", "scratchpad"],
    template=TUTOR_AGENT_TEMPLATE,
)

# Reflection Generation (MMLU&FEVER)
TUTOR_REFLECT_TEMPLATE="""{header}
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scratchpad}
Advice: {tutor_ins}
Reflection: {current_reflect}"""


tutor_reflect_prompt = PromptTemplate(
    input_variables=["header","examples", "choices", "question", "tutor_ins","scratchpad","current_reflect"],
    template = TUTOR_REFLECT_TEMPLATE,
)

#below are for FEVER advice
TUTOR_ADVICE_FOLLOW_TEMPLATE_FEVER="""As a tutor, your are supposed to meticulously evaluate the student’s approach to fact verification task. Claim and the student’s previous thought and answer are given, check if the relations mentioned in the Thought is correct and if there might be a more appropriate answer. If the student’s reasoning thought is accurate and the proposed answer is the most appropriate, encourage them to adhere to their initial trial. Otherwise, guide the student to revisit specific details, explore alternative answer.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}{scatchpad}
Advice: """

tutor_advice_follow_prompt_fever = PromptTemplate(
    input_variables=["question", "choices", "scatchpad","examples"],
    template = TUTOR_ADVICE_FOLLOW_TEMPLATE_FEVER,
)

#below are for FEVER initial advice
TUTOR_ADVICE_INITIAL_TEMPLATE_fever = """As a tutor, your focus is on guiding the student to navigate fact-checking problems strategically. Encourage them to dissect the claim, identifying key elements and associate facts. Emphasize the correct relation between important elements that could distinguish SUPPORTS from REFUTES options. Also, lacking of enough information will lead to NOT ENOUGH INFO.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{choices}
Advice: """

tutor_advice_initial_prompt_fever = PromptTemplate(
    input_variables=["question","choices",'examples'],
    template = TUTOR_ADVICE_INITIAL_TEMPLATE_fever,
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

#below are for COT reflection
COT_REFLECT_INSTRUCTION = """{header} 
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{reflections}{scratchpad}
"""


cot_reflect_prompt = PromptTemplate(
    input_variables=["header","examples", "choices", "question", "reflections","scratchpad"],
    template = COT_REFLECT_INSTRUCTION,
)


#below are for TUTOR strategy
TUTOR_ADVICE_INITIAL_TEMPLATE = """As a tutor, your focus is on guiding the student to navigate multiple-choice question-answering problems strategically. Encourage them to dissect the question, identifying key elements and nuances within each choice. Emphasize the importance of understanding subtle differences that could distinguish correct from incorrect options.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}
Advice: """

tutor_advice_initial_prompt = PromptTemplate(
    input_variables=["question","choices",'examples'],
    template = TUTOR_ADVICE_INITIAL_TEMPLATE,
)

#below are for TUTOR reflection
TUTOR_ADVICE_FOLLOW_TEMPLATE="""As a tutor, your are supposed to meticulously evaluate the student’s approach to multiple-choice problems. Question, Choices and the student’s previous thought and answer are given, check if the facts mentioned in the thought is correct and if there might be a more appropriate option than the one chosen. If the student’s reasoning thought is accurate and the proposed answer is the most appropriate, encourage them to adhere to their initial trial. Otherwise, guide the student to revisit specific details, explore alternative choice.
Here are some examples:
{examples}
(END OF EXAMPLES)

Question: {question}{choices}{scatchpad}
Advice: """

tutor_advice_follow_prompt = PromptTemplate(
    input_variables=["question", "choices", "scatchpad","examples"],
    template = TUTOR_ADVICE_FOLLOW_TEMPLATE,
)