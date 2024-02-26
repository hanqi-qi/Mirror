
#thought/reflection generation of previous trial is given
TUTOR_REFLECTION_STEM = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
Action: Finish[B. Homeostasis]
(END PREVIOUS TRIAL)

Advice: The previous trial explains each choices and the highlight the differences among them. Significantly, it verifies that B is consistent with question. So, you can make up your mind the previous trial. 
Reflection: According to the Advice, I will insist on my previous answer. so the final answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Thought: The second pharyngeal arch contributes to the body and greater horns of the hyoid bone, while the third pharyngeal arch contributes to the lesser horns. So the answer is C.
Action: Finish[C. The second pharyngeal arch]
(END PREVIOUS TRIAL)

Advice: Part of the Thought in the previous trial is correct. However, there is minor misunderstanding that to the third pharyngeal arches mentioned in D. There are indeed differences between the second and pharyngeal arch, but you should indepedently check if third pharyngeal arches contributes to the key element in the question, i.e., orign of the hyoid bone, regardless its contribution is greater or lesser. 
Reflection: The Advice reminds me that I should pay more attention to check if the key element in the question is correctly responded by choices. Therefore, I re-assess if third pharyngeal arches is origin of the hyoid bone and the the conclusion is that it ossifies into the inferior part and the greater cornu of the hyoid bone. Based on this and previous trial, both the second and third pharyngeal arches are correct for the question, so the answer is D.
Action: Finish[D. The second and third pharyngeal arches]

Question: The pleura
Choices: 
A. have no sensory innervation
B. are separated by a 2 mm space
C. extend into the neck
D. are composed of respiratory epithelium
Thought: The pleura, the double-layered membranes that surround the lungs and line the chest cavity, do not have sensory innervation. This means that they are not sensitive to touch, pain, or other sensory stimuli. So the answer is A. have no sensory innervation.
Action: Finish[A. A. have no sensory innervation]
(END PREVIOUS TRIAL)

Advice: There might be multiple possible choices, you need to enumerate each of them and select the best one.
Reflection: Let's evaluate each choice: A. "have no sensory innervation" - This is not accurate. The pleura do have sensory innervation. B. "are separated by a 2 mm space" - The pleura are actually in very close proximity to each other, with only a small amount of lubricating fluid between them. They do not have a 2 mm space between them. C. "extend into the neck" - This is not true. The pleura do not extend into the neck. D. "are composed of respiratory epithelium" - The pleura are indeed composed of a specialized type of epithelium called mesothelium. Given the accurate information about the pleura's composition, the correct answer is D.
Action: Finish[D. are composed of respiratory epithelium]
"""

# thought/reflection generation of previous trial is given
TUTOR_STEM = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Advice: You should pay attention to the differences of the multiple choices and select the one most related to normal state.
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Advice: There are overlapping between Choice A and B, between C and D. For example, if A is correct, you need to further verfiy if the second pharyngeal arches are correct according to the question. If so, B is more appropriate than A. The similar sitatution is applicable to C and D.
Thought: According to the Advice, The second pharyngeal arch contributes to the body and greater horns of the hyoid bone, while the third pharyngeal arch contributes to the lesser horns. Both C and D mention the second pharyngeal arch, but D includes the additional incorrect information. So the answer is C.
Action: Finish[C. The second pharyngeal arch]

Question: Say the pupil of your eye has a diameter of 5 mm and you have a telescope with an aperture of 50 cm. How much more light can the telescope gather than your eye?
Choices:
A. 100 times more
B. 1000 times more
C. 10000 times more
D. 10 times more
Advice: You need to pay attention to the different number of in the choices, 10, 100, 1000 or 10000. Calculate very carefully to avoid any confusion.
Thought: Following the advice aboev, after careful evaluations for each choice, C. 10000 times more is the best choices.
Action: Finish[C. 1000 times more]
"""

# thought/reflection generation of previous trial is given
TUTOR_STEM_NOADVCIE = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Advice: None
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Advice: None
Thought: According to the Advice, The second pharyngeal arch contributes to the body and greater horns of the hyoid bone, while the third pharyngeal arch contributes to the lesser horns. Both C and D mention the second pharyngeal arch, but D includes the additional incorrect information. So the answer is C.
Action: Finish[C. The second pharyngeal arch]

Question: Say the pupil of your eye has a diameter of 5 mm and you have a telescope with an aperture of 50 cm. How much more light can the telescope gather than your eye?
Choices:
A. 100 times more
B. 1000 times more
C. 10000 times more
D. 10 times more
Advice: None
Thought: Following the advice aboev, after careful evaluations for each choice, C. 10000 times more is the best choices.
Action: Finish[C. 1000 times more]
"""

# thought/reflection generation of previous trial is given for fever
COT_FEVER="""Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Advice: The claim "Nikolaj Coster-Waldau worked with the Fox Broadcasting Company" asserts that the actor Nikolaj Coster-Waldau has been involved in projects or collaborations with the Fox Broadcasting Company.
Thought: Nikolaj Coster-Waldau, known for his role as Jaime Lannister in Game of Thrones, appeared in the Fox Broadcasting Company's television series New Amsterdam, which premiered in 2008
Action: Finish[SUPPORTS]

Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
Advice: Verify the claim meticulously, considering pitfalls like potential misinterpretation of "Beautiful," verifying the accurate timeframe (2003), confirming the specific chart (Billboard Hot 100), ensuring reliability of sources, and distinguishing between lack of contradictory information ("Not Enough Information") and direct refutation ("Refutes").
Thought: "Beautiful" by Christina Aguilera reached number two on the Billboard Hot 100 in 2003, making the claim accurate. But the Claim doesn't give specific definition to the "Beautiful", therefore, the answer is [NOT ENOUGH INFO].
Action: Finish[NOT ENOUGH INFO]

Claim: Stranger Things is set in Bloomington, Indiana.
Advice: Clarify any confusion between the show's fictional setting (Hawkins) and the claimed location (Bloomington). Rely on accurate sources like official show statements, credits, and creator statements to avoid misinformation. Scrutinize the opening credits and narrative for explicit mentions of the setting. Cross-verify with creators' statements to ensure clarity. Diligent verification addresses potential pitfalls and ensures accuracy.
Thought: Based on Advice and my internal knowledge, the tv series "Stranger Things"is actually set in the fictional town of Hawkins, Indiana. therefore, the answer is [REFUTES].
Action: Finish[REFUTES]
"""

#  thought/reflection generation of previous trial is given for fever
TUTOR_REFLECTION_FEVER = """Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Advice: The claim "Nikolaj Coster-Waldau worked with the Fox Broadcasting Company" asserts that the actor Nikolaj Coster-Waldau has been involved in projects or collaborations with the Fox Broadcasting Company.
Thought: Nikolaj Coster-Waldau, known for his role as Jaime Lannister in Game of Thrones, appeared in the Fox Broadcasting Company's television series New Amsterdam, which premiered in 2008
Action: Finish[SUPPORTS]
(END PREVIOUS TRIAL)
Advice: The previous trial explains how the claim is correctly link "Nikolaj Coster-Waldau" and "Fox Broadcasting Company"
Reflection: According to the Advice, I will insist on my previous answer.
Action: Finish[SUPPORTS]


Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
Advice: Christina Aguilera's song "Beautiful" did achieve the number two position on the Billboard Hot 100 chart in 2003.
Thought: According to the Advice, the claim abou the song "Beautiful" Christina Aguilera by is supported.
Action: Finish[SUPPORTS]
(END PREVIOUS TRIAL)
Advice: The previous trial adds additional information to the claim: it assumes that the song "Beautiful" is one of Christina Aguilera's song.
Reflection: According to the Advice, the original claim misses the significant information to support the correctness. Therefore, the answer is NOT ENOUGH INFO.
Action: Finish[NOT ENOUGH INFO]
"""


# thought/reflection generation of previous trial is given for stem
COT_REFLECTION_STEM = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Reflection: The Thought explains that Homeostasis plays a role in maintaining the normal state and the answer is B (Homeostasis). The explaination is factually correct and the initial answer is consistent with the explaination. so the initial answer is correct. I will keep the answer when asked next time.
Answer after reflection: The refection above confirms the factual knowledge that Homeostasis is important in 
maintaining the normal state, so the final answer is B. Homeostasis.
Action: Finish[B. Homeostasis]
hanqi
Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Thought: The second pharyngeal arch contributes to the body and greater horns of the hyoid bone, while the third pharyngeal arch contributes to the lesser horns. So the answer is B.
Action: Finish[B. The first and second pharyngeal arches]

Reflection: The Thought above show that both second and third arches are the embryological origin of the hyoid bone, while the answer is B. (The first and second pharyngeal arches). This is contradictary to the Thought, so this initial selected choice is incorrect. The correct answer should be D. The second and third pharyngeal arches.

Answer after reflection: The reflection above correctly points the issue: the initial selected choice is contradictary to its Thought. According to the explainations in Thought, the final answer should be D. The second and third pharyngeal arches.
Action: Finish[D. The second and third pharyngeal arches]

Question: The pleura
Choices: 
A. have no sensory innervation
B. are separated by a 2 mm space
C. extend into the neck
D. are composed of respiratory epithelium

Thought: The pleura, the double-layered membranes that surround the lungs and line the chest cavity, do not have sensory innervation. This means that they are not sensitive to touch, pain, or other sensory stimuli. So the answer is A. have no sensory innervation

Reflection: I apologize for any confusion earlier. Let's evaluate each choice: A. "have no sensory innervation" - This is not accurate. The pleura do have sensory innervation, and irritation or inflammation of the pleura can cause pleuritic chest pain. B. "are separated by a 2 mm space" - The pleura are actually in very close proximity to each other, with only a small amount of lubricating fluid between them. They do not have a 2 mm space between them. C. "extend into the neck" - This is not true. The pleura do not extend into the neck. D. "are composed of respiratory epithelium" - The pleura are indeed composed of a specialized type of epithelium called mesothelium. This epithelium is responsible for producing a lubricating fluid that allows smooth movement of the lungs within the chest cavity. Given the accurate information about the pleura's composition, the correct answer is D. 

Answer after reflection: The reflection gives contradictary knowledge about if pleura has sensory innervation. According to my knowledge about pleura and I double-check the information, the correct clarification is "The pleura do have sensory innervation". I also review the other choices carefully and agree with the reflection, so the final answer is D. are composed of respiratory epithelium
Action: Finish[D. are composed of respiratory epithelium]
"""


# thought/reflection generation of previous trial is given
COT_STEM_NOTHOUGHT = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: After careful evaluations for each choice, B. Homeostasis is the best choice.
Action: Finish[B. Homeostasis] 

Question: You are pushing a truck along a road. Would it be easier to accelerate this truck on Mars? Why? (Assume there is no friction)?
Choices:
A. It would be harder since the truck is heavier on Mars
B. It would be easier since the truck is lighter on Mars
C. It would be harder since the truck is lighter on Mars
D. It would be the same no matter where you are
Thought: After careful evaluations for each choice, D. is the best choice.
Action: Finish[D. It would be the same no matter where you are]

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Thought: After careful evaluations for each choice, D. The second and third pharyngeal arches is the best choice.
Action: Finish[D. The second and third pharyngeal arches]

Question: Say the pupil of your eye has a diameter of 5 mm and you have a telescope with an aperture of 50 cm. How much more light can the telescope gather than your eye?
Choices:
A. 100 times more
B. 1000 times more
C. 10000 times more
D. 10 times more
Thought: After careful evaluations for each choice, C. 10000 times more is the best choices.
Action: Finish[C. 1000 times more]
"""


#Instruction generation demos for initial answer
TUTOR_INIT_INST="""Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Advice: Examine the question centered on the body's ability to maintain its normal state. Delve into the definitions of each term—Anabolism, Homeostasis, Tolerance, and Catabolism. Pay attention to nuanced differences, and systematically eliminate options that don't align with the concept of maintaining normalcy to arrive at a well-informed choice.

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Advice: Explore the question by understanding the embryological origin of the hyoid bone. Examine the contributions of each pharyngeal arch—first, second, and third. Pay close attention to the nuances of the options (A, B, C, D) and consider how each relates to the formation of the hyoid bone. Systematically eliminate choices that do not align with the correct embryological origin to make a well-informed selection.

Question: The pleura
Choices: 
A. have no sensory innervation
B. are separated by a 2 mm space
C. extend into the neck
D. are composed of respiratory epithelium
Advice: Delve into your understanding of the pleura and paying attention to specific details associated with sensory innervation, interpleural space, extension into the neck, and composition. Look for any unique characteristics that may help differentiate the correct answer from the plausible options.

Question: Say the pupil of your eye has a diameter of 5 mm and you have a telescope with an aperture of 50 cm. How much more light can the telescope gather than your eye?
Choices:
A. 100 times more
B. 1000 times more
C. 10000 times more
D. 10 times more
Advice: Consider the relationship between the diameter of the pupil and the aperture of the telescope in terms of light gathering. Think about the formula for the area of a circle, which is πr², where "r" is the radius. For the pupil of the eye with a diameter of 5 mm. Next, apply the same process for the telescope's aperture with a diameter of 50 cm. Now, compare the areas of the two apertures using the formula for the area of a circle, and consider how much more light the telescope can gather compared to the eye. This mathematical approach should guide you to the correct choice among (A, B, C, D).

Question: You are pushing a truck along a road. Would it be easier to accelerate this truck on Mars? Why? (Assume there is no friction)?
Choices:
A. It would be harder since the truck is heavier on Mars
B. It would be easier since the truck is lighter on Mars
C. It would be harder since the truck is lighter on Mars
D. It would be the same no matter where you are
Advice: Focus on the forces influencing the acceleration of the truck along the road. Emphasize that gravity has a minor impact in a horizontal scenario with no incline. Consider the applied force and the absence of friction as the primary factors affecting the ease of acceleration."""

# advice generation demos for after reflection
ADVICE_AFTER_REFLECTION_EXAMPLES="""Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Advice: The claim "Nikolaj Coster-Waldau worked with the Fox Broadcasting Company" asserts that the actor Nikolaj Coster-Waldau has been involved in projects or collaborations with the Fox Broadcasting Company.
Thought: Nikolaj Coster-Waldau, known for his role as Jaime Lannister in Game of Thrones, appeared in the Fox Broadcasting Company's television series New Amsterdam, which premiered in 2008
Action: Finish[SUPPORTS]
(END PREVIOUS TRIAL)
Advice: The previous trial explains how the claim is correctly link "Nikolaj Coster-Waldau" and "Fox Broadcasting Company".
 
Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
Advice: Christina Aguilera's song "Beautiful" did achieve the number two position on the Billboard Hot 100 chart in 2003.
Thought: According to the Advice, the claim abou the song "Beautiful" Christina Aguilera by is supported.
Action: Finish[SUPPORTS]
(END PREVIOUS TRIAL)
Advice: The previous trial adds additional information to the claim: it assumes that the song "Beautiful" is one of Christina Aguilera's song.
"""
#Instruction generation demos for initial answer
TUTOR_SEC_INST = """Question: The theory that cities grow outward from a core utilizing several nodes of growth was proposed by
Choices:
A. Rostow.
B. Ravenstein.
C. von Thünen.
D. Harris and Ullmann.
Thought: von Thünen proposed the theory that cities grow outward from a core utilizing several nodes of growth. The other choices depicted theories related to but different from von Thünen's: Rostow's theory of modern economic growth, Ravenstein's laws of migration, and Harris and Ullmann's matrix analysis. So the answer is C. von Thünen.
Action: Finish[C. von Thünen.]
(END PREVIOUS TRIAL)

Advice: Your selection of answer C (von Thünen) aligns accurately with the theory that cities grow outward from a core with multiple nodes of growth. You've successfully distinguished it from the other choices, so stick to your previous answer C.

Question: The price elasticity of demand for a product is greater if
Choices:
A. the proportion of the good of the consumer's budget is high.
B. the period of time to respond to a price change is short.
C. the number of substitute products is limited.
D. the product is a necessity.
Thought: A. The greater the proportion of a product of a consumer's budget, the more sensitive the customer is to price changes. C. If there are limited substitutes for a product, customers are less likely to switch and will be more sensitive to price changes. B. The elasticity of demand will also increase if there is a short period of time to respond to a price change, such as those with perishable items. D. The more necessary a product is, the less elastic it will be. So the answer is B. the period of time to respond to a price change is short.
Action: Finish[B. the period of time to respond to a price change is short.]
(END PREVIOUS TRIAL)

Advice: The student's thought process demonstrates a solid understanding of the factors influencing price elasticity of demand. Their rationale for choosing option B aligns with the economic concept. Your reasoning about perishable items and the increased sensitivity to price changes in a limited timeframe demonstrates a sound understanding of the concept of price elasticity. Keep up the excellent analytical thinking! 

Question: Most mnemonic devices (like learning the notes on the staff by memorizing the sentence "Every Good Boy Does Fine" and using the first letter of each word) are examples of which memory enhancement technique?
Choices:
A. semantic encoding
B. potentiation
C. recognition
D. chunking
Thought: Mnemonic devices are usually used to improve memory by providing an association between what we want to remember and an easier-to-remember object or phrase. This is most similar to semantic encoding (A), which is the process by which we use meaning to store and retrieve information. Potentiation (B) pertains to strengthening the connection between two neurons, while recognition (C) pertains to recognizing patterns or items. Chunking (D) refers to grouping items together for easy recall. So the answer is A. semantic encoding.
Action: Finish[A. semantic encoding]
(END PREVIOUS TRIAL)

Advice: Please explicitly differentiate semantic encoding from other terms (potentiation, recognition, chunking). Clarify potential pitfalls in the thought process, ensuring semantic encoding aligns precisely with mnemonic devices. Encourage openness to revisions if a more nuanced understanding emerges.

Question: If f(z) is an analytic function that maps the entire finite complex plane into the real axis, then the imaginary axis must be mapped onto
Choices:
A. the entire real axis
B. a point
C. a ray
D. an open finite interval
Thought: When an analytic function is continuously differentiable, it implies that it is a holomorphic function and that it obeys the Cauchy Riemann equations. These equations infer that the real and imaginary axes are mapped to curves of the same length so the answer would be D. an open finite interval
Action: Finish[D. an open finite interval]
(END PREVIOUS TRIAL)

Advice: You have acknowledged the correct use of Cauchy-Riemann equations. Justify option D but consider additional conditions. Use attempts as learning opportunities. Revisit concepts and practice for reinforcement. Consider revising the answer if needed.
"""

# advice generation demos
ADVICE_EXAMPLES = """Claim: Stranger Things is set in Bloomington, Indiana.
Advice: When verifying the claim "Stranger Things is set in Bloomington, Indiana," beware of pitfalls. Clarify any confusion between the show's fictional setting (Hawkins) and the claimed location (Bloomington). Rely on accurate sources like official show statements, credits, and creator statements to avoid misinformation. Scrutinize the opening credits and narrative for explicit mentions of the setting. Cross-verify with creators' statements to ensure clarity. Diligent verification addresses potential pitfalls and ensures accuracy.

Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
Advice: Verify the claim meticulously, considering pitfalls like potential misinterpretation of "Beautiful," verifying the accurate timeframe (2003), confirming the specific chart (Billboard Hot 100), ensuring reliability of sources, and distinguishing between lack of contradictory information ("Not Enough Information") and direct refutation ("Refutes").

Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Advice: The claim requires verification. Pitfalls include potential misinterpretation of "work," timeframe ambiguity, and varied project types (TV, film). Be cautious of missing but critical details that would lead to a classification of "Not Enough Information" rather than "Refutes.
"""

