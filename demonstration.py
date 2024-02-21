

COT_REFLECTION_STEM = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

#Reflection: The Thought explains that Homeostasis plays a role in maintaining the normal state and the answer is B (Homeostasis). The explaination is factually correct and the initial answer is consistent with the explaination. so the initial answer is correct. I will keep the answer when asked next time.
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

#STEM_TUTOR

# #thought and answer generation without previous trial
# TUTOR_STEM = """Question: Which of the following terms describes the body's ability to maintain its normal state?
# Choices:
# A. Anabolism
# B. Homeostasis
# C. Tolerance
# D. Catabolism
# Advice: You should pay attention to the differences of the multiple choices and select the one most related to normal state.
# Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis a self-regulating process by which a living organism can maintain internal stability. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is B. Homeostasis.
# Action: Finish[B. Homeostasis]
# """
TUTOR_STEM_5 = """Question: Which of the following terms describes the body's ability to maintain its normal state?
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

Question: Which of the following problems can be solved by a standard greedy algorithm? 
I. Finding a minimum spanning tree in an undirected graph with positive-integer edge weights 
II. Finding a maximum clique in an undirected graph 
III. Finding a maximum flow from a source node to a sink node in a directed graph with positive-integer edge capacities
Choices:
A. I only
B. II only
C. III only
D. I and II only
Advice: A standard greedy algorithm works for finding a minimum spanning tree in a graph with positive-integer edge weights. It's not effective for maximum clique or maximum flow problems. Thus, the correct choice focuses solely on the minimum spanning tree scenario.
Thought: Option I is correct as greedy algorithms like Kruskal's or Prim's are used for finding minimum spanning trees. Option II is NP-hard and lacks a polynomial-time greedy solution. Option III uses algorithms like Ford-Fulkerson, which are not standard greedy algorithms.
Action: Finish[A. I only]

Question: The primary focus of microeconomics is,
Choices:
A. Families and how they make money.
B. Firms and how they make profits.
C. Individual units within the overall economy.
D. Government.
Advice: Microeconomics primarily studies the behavior of individual units, like households and firms, in their decision-making processes and resource allocation. While it does consider families and firms, and is affected by government policies, its core focus is on the individual entities within the economy.
Thought: Microeconomics examines how individuals and businesses make decisions about using limited resources. It looks at the actions of single units in the economy, like households or companies, rather than the economy as a whole. This focus includes studying supply and demand in specific markets.
Action: Finish[C. Individual units within the overall economy.]
"""
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
#math
TUTOR_MATH="""Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Advice: In April, Natalia sold clips to 48 friends. In May, she sold half as many clips as in April.
To find the total number of clips sold in May, you can take half of the April sales (48/2). Once you have that, you can add the April and May sales together for the total.
Thought: (1) Natalia sold 48/2 = <<48/2=24>>24 clips in May.(2) Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.
Action: Finish[72]

Question: Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"
Advice: To find out how much Weng earned for babysitting, you can use the formula: Earnings=Hourly Rate * Number of Hours, Now, you can substitute these values into the formula and calculate the earnings.
Thought: (1) Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute. (2) Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10
Action: Finish[10]

Question: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Advice: (1) Betty needs $100 for the wallet. (2)She already has half of the money, which is 50. (3)
Her parents gave her an additional $15. (4) Her grandparents gave her twice as much as her parents, which is 2*15
Thought: (1) In the beginning, Betty has only 100 / 2 = $<<100/2=50>>50.Betty's grandparents gave her 15 * 2 = $<<15*2=30>>30. (2) This means, Betty needs 100 - 50 - 30 - 15 = $<<100-50-30-15=5>>5 more.
Action: Finish[5]
"""
#hotpot
TUTOR_HOTPOT = """Relevant Context: The Nile River is the longest river in the world, spanning approximately 6,650 kilometers (4,132 miles) in length. It flows through eleven countries in northeastern Africa, including Egypt, Sudan, and Uganda.
Question: What is the longest river in the world?
Advice: Be aware of the Nile River context, confidently recall it as the longest, and respond clearly, connecting it to your geography knowledge.
Thought: The question asks for the longest river in the world, which I know is the Nile River based on the context provided.
Action: Finish[Nile River]

Relevant Context: Ludwig van Beethoven was a German composer and pianist who was a crucial figure in the transition between the Classical and Romantic eras in Western classical music. One of his most famous compositions is the Symphony No. 9, also known as the "Choral" symphony.
Question: Which composer created Symphony No. 9?
Advice: Be aware of the context, confidently recall Beethoven as the creator of Symphony No. 9, and respond clearly, connecting the composer to the specific symphony.
Thought: The question is asking for the composer of Symphony No. 9. Based on the context, I know that Ludwig van Beethoven composed this symphony.
Action: Finish[Ludwig van Beethoven]

Relevant Context: Photosynthesis is the process by which green plants and some other organisms convert light energy into chemical energy. During this process, plants absorb sunlight, carbon dioxide, and water to produce glucose and oxygen.
Question: What do plants produce during photosynthesis?
Advice: Be aware of the context, confidently recall the products (glucose and oxygen) of photosynthesis, and respond clearly, connecting the process to its outcomes.
Thought: The question is asking about the products of photosynthesis. From the context, I know that plants produce glucose and oxygen during this process.
Action: Finish[Glucose and Oxygen]
"""

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

#thought/reflection generation of previous trial is given
TUTOR_REFLECTION_STEM_5 = """Question: Which of the following terms describes the body's ability to maintain its normal state?
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

Question: Which of the following countries does NOT have a well-known example of a relict boundary?
Choices: 
A. Vietnam
B. United Kingdom
C. Germany
D. Bolivia
Thought: A. Vietnam has well-known examples of relict boundaries, particularly associated with the Vietnam War. The Demilitarized Zone that separated North and South Vietnam during the conflict is a notable relict boundary. B. United Kingdom has historical relict boundaries, such as Hadrian's Wall between England and Scotland. C. Germany has relict boundaries from the Cold War, notably the former border between West and East Germany. D. Bolivia has experienced various boundary changes and conflicts, but it may not have as many well-known examples of relict boundaries compared to some other countries. So the answer is D. Bolivia.
Action: Finish[D. Bolivia]
(END PREVIOUS TRIAL)

Advice: In determining which country lacks a well-known relict boundary, it's essential to compare the global recognition and historical significance of each option's boundaries. Vietnam and Germany have highly notable relict boundaries, while Bolivia's examples are less prominent on the global stage.
Reflection: Reflecting on the analysis, it's evident that understanding the global prominence and historical impact of relict boundaries is crucial for this question. Based on this criteria, Bolivia emerges as the likely answer due to its less globally recognized relict boundaries compared to Vietnam or Germany.
Action: Finish[D. Bolivia]

Question: Which of these principles is not an element of the responsibility to protect?
A. The responsibility to prevent
B. The responsibility to react
C. The responsibility to remain sovereign
D. The responsibility to rebuild
Thought: The other three principles: prevention (A), reaction (B), and rebuilding(D)—are typically considered elements of the responsibility to protect (R2P). So the answer is C. The responsibility to remain sovereign.
Action: Finish[C. The responsibility to remain sovereign]
(END PREVIOUS TRIAL)

Advice: In analyzing the principles related to the "Responsibility to Protect" (R2P), it's clear that prevention, reaction, and rebuilding are integral components of this doctrine. Conversely, the concept of "remaining sovereign" is not traditionally framed as an element of R2P, as this principle focuses more on intervention in cases where a state fails to protect its citizens.
Reflection: Reflecting on the principles of the "Responsibility to Protect," it's clear that prevention, reaction, and rebuilding are key components of this international doctrine. In contrast, the concept of "remaining sovereign," which is not typically associated with R2P's focus on intervention, appears to be the principle that does not align with the elements of R2P, pointing to option C as the answer.
Action: Finish[C. The responsibility to remain sovereign]
"""

#thought/reflection generation of previous trial is given
TUTOR_REFLECTION_STEM_ALL_RIGHT = """Question: Which of the following terms describes the body's ability to maintain its normal state?
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

Question: Which of the following countries does NOT have a well-known example of a relict boundary?
Choices: 
A. Vietnam
B. United Kingdom
C. Germany
D. Bolivia
Thought: A. Vietnam has well-known examples of relict boundaries, particularly associated with the Vietnam War. The Demilitarized Zone that separated North and South Vietnam during the conflict is a notable relict boundary. B. United Kingdom has historical relict boundaries, such as Hadrian's Wall between England and Scotland. C. Germany has relict boundaries from the Cold War, notably the former border between West and East Germany. D. Bolivia has experienced various boundary changes and conflicts, but it may not have as many well-known examples of relict boundaries compared to some other countries. So the answer is D. Bolivia.
Action: Finish[D. Bolivia]
(END PREVIOUS TRIAL)

Advice: In determining which country lacks a well-known relict boundary, it's essential to compare the global recognition and historical significance of each option's boundaries. Vietnam and Germany have highly notable relict boundaries, while Bolivia's examples are less prominent on the global stage.
Reflection: Reflecting on the analysis, it's evident that understanding the global prominence and historical impact of relict boundaries is crucial for this question. Based on this criteria, Bolivia emerges as the likely answer due to its less globally recognized relict boundaries compared to Vietnam or Germany.
Action: Finish[D. Bolivia]

Question: Which of these principles is not an element of the responsibility to protect?
A. The responsibility to prevent
B. The responsibility to react
C. The responsibility to remain sovereign
D. The responsibility to rebuild
Thought: The other three principles: prevention (A), reaction (B), and rebuilding(D)—are typically considered elements of the responsibility to protect (R2P). So the answer is C. The responsibility to remain sovereign.
Action: Finish[C. The responsibility to remain sovereign]
(END PREVIOUS TRIAL)

Advice: In analyzing the principles related to the "Responsibility to Protect" (R2P), it's clear that prevention, reaction, and rebuilding are integral components of this doctrine. Conversely, the concept of "remaining sovereign" is not traditionally framed as an element of R2P, as this principle focuses more on intervention in cases where a state fails to protect its citizens.
Reflection: Reflecting on the principles of the "Responsibility to Protect," it's clear that prevention, reaction, and rebuilding are key components of this international doctrine. In contrast, the concept of "remaining sovereign," which is not typically associated with R2P's focus on intervention, appears to be the principle that does not align with the elements of R2P, pointing to option C as the answer.
Action: Finish[C. The responsibility to remain sovereign]
"""


TUTOR_REFLECTION_MATH = """Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Advice: In April, Natalia sold clips to 48 friends. In May, she sold half as many clips as in April.
To find the total number of clips sold in May, you can take half of the April sales (48/2). Once you have that, you can add the April and May sales together for the total.
Thought: (1) Natalia sold 48/2 = <<48/2=24>>24 clips in May.(2) Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.
Action: 72
(END PREVIOUS TRIAL)

Advice: Fantastic job! You nailed it. Natalia sold 24 clips in May, and when you add that to the 48 clips she sold in April, you get a total of 72 clips sold altogether in April and May. However, you fail to follow the format of answer. Please return Finish[72] instead.
Reflection: The advice is helpful to improve my answer quality. I will give the answer like Finish[72].
Action: Finish[72]

Question: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Advice: (1) Betty needs $100 for the wallet. (2)She already has half of the money, which is 50. (3)
Her parents gave her an additional $15. (4) Her grandparents gave her twice as much as her parents, which is 2*15
Thought: (1) In the beginning, Betty has only 100 / 2 = $<<100/2=50>>50.Betty's grandparents gave her 15 * 2 = $<<15*2=30>>30. (2) This means, Betty needs 100 - 50 - 30 - 15 = $<<100-50-30-15=5>>5 more.
Action: Finish[5]
(END PREVIOUS TRIAL)

Advice: Your action is on point! Betty needs $5 more to buy the wallet. 
Reflection: I will stick to my answer in previous trial.
Action: Finish[5]
"""

TUTOR_REFLECTION_HOTPOT ="""Relevant Context: Ernest Hemingway's novel "The Old Man and the Sea" tells the story of Santiago, an aging Cuban fisherman, who struggles to catch a giant marlin in the Gulf Stream. The book won the Pulitzer Prize for Fiction in 1953 and contributed to Hemingway's Nobel Prize for Literature in 1954.
Question: Which literary award did "The Old Man and the Sea" contribute to Hemingway winning?
Thought: The question is asking which award "The Old Man and the Sea" contributed to Hemingway winning. Based on the context, I know the novel won the Pulitzer Prize for Fiction and contributed to his Nobel Prize for Literature.
Action: Finish[Pulitzer Prize for Fiction]
(END PREVIOUS TRIAL)

Advice: Your response is correct based on the given context, but try to condense the response to the concise answer
Reflection: Upon reflecting on advice, I realize that I included excessive information. Moving forward, when attempting this question again or similar questions, I will make sure to exclude the details and provide a concise answer, Pulitzer Prize.

Relevant Context: On 14 October 1947, Chuck Yeager, a United States Air Force test pilot, became the first person to break the sound barrier by flying the Bell X-1 experimental aircraft at an altitude of 45,000 feet.
Charles Elwood "Chuck" Yeager (13 February 1923 - 7 December 2020) was a United States Air Force officer, flying ace, and test pilot. He is best known for becoming the first person to break the sound barrier, which he achieved in the Bell X-1 aircraft named Glamorous Glennis. Yeager was also a distinguished fighter pilot during World War II and was credited with shooting down at least 12 enemy aircraft. In 1973, he was inducted into the National Aviation Hall of Fame for his significant contributions to aviation.
Question: Who is the first person to break the sound barrier?
Thought: The question is asking for the first person to break the sound barrier. From the context, I know that Chuck Yeager, a United States Air Force test pilot, was the first person to break the sound barrier.
Action: Finish[Chuck Yeager]
(END PREVIOUS TRIAL)

Advice: Your thought is clear and correctly reflecting the fact mentioned in the relevant context. Keep up the careful thoughts!
Reflection: Upon reflecting on advice, I realize that it was accurate within the given context and maintains conciseness by excluding unnecessary details. Therefore, I will stop self-reflection next time.
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

COT_NEG_REFLECTION = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: Let's think step by step. Anabolism refers the synthesis of complex molecule from simpler ones together with the storage of energy. B. Homeostasis is an ability of organisms to withstand or survive prevailing adverse conditions. C. Tolerance is a self-regulating process by which a living organism can maintain internal stability. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is C. Tolerance.
Action: Finish[B. Homeostasis]
(END PREVIOUS TRIAL)

Reflection: The Thought is factually incorrect and I will reconsider and output a different answer. According to the Biology knowledge, Homeostasis plays a role in maintaining the normal state. so the correct answer should be B. Homeostasis.
Thought: The refection above confirms the factual knowledge that Homeostasis is important in 
maintaining the normal state, so the final answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Question: What is the embryological origin of the hyoid bone?
Choices:
A. The first pharyngeal arch
B. The first and second pharyngeal arches
C. The second pharyngeal arch
D. The second and third pharyngeal arches
Thought: The second pharyngeal arch contributes to the body and greater horns of the hyoid bone, while the third pharyngeal arch contributes to the lesser horns. So the answer is B.
Action: Finish[B. The first and second pharyngeal arches]

Reflection: The Thought is contradictary with Answer, I will consider a different answer. The thought show that both second and third arches are the embryological origin of the hyoid bone, so the correct answer should be D. The second and third pharyngeal arches.
Thought: The reflection above correctly points the issue and correct it to D. The second and third pharyngeal arches.
Action: Finish[D. The second and third pharyngeal arches]

Question: The pleura
Choices: 
A. have no sensory innervation
B. are separated by a 2 mm space
C. extend into the neck
D. are composed of respiratory epithelium

Thought: The pleura, the double-layered membranes that surround the lungs and line the chest cavity, do not have sensory innervation. This means that they are not sensitive to touch, pain, or other sensory stimuli. So the answer is A. have no sensory innervation

Reflection: The Thought is factually incorrect and I will propose a new answer after careful consideration. Let's evaluate each choice: A. "have no sensory innervation" - This is not accurate. The pleura do have sensory innervation, and irritation or inflammation of the pleura can cause pleuritic chest pain. B. "are separated by a 2 mm space" - The pleura are actually in very close proximity to each other, with only a small amount of lubricating fluid between them. They do not have a 2 mm space between them. C. "extend into the neck" - This is not true. The pleura do not extend into the neck. D. "are composed of respiratory epithelium" - The pleura are indeed composed of a specialized type of epithelium called mesothelium. This epithelium is responsible for producing a lubricating fluid that allows smooth movement of the lungs within the chest cavity. Given the accurate information about the pleura's composition, the correct answer is D. are composed of respiratory epithelium.
Thought: The Reflection rejects the Thought and propose a new answer. According to my knowledge about pleura and I double-check the information, the final answer is D. are composed of respiratory epithelium.
Action: Finish[D. are composed of respiratory epithelium]
"""

COT_REFLECT_ALLWRONG = """Question: Which of the following terms describes the body's ability to maintain its normal state?
Choices:
A. Anabolism
B. Homeostasis
C. Tolerance
D. Catabolism
Thought: Let's go over each choice. A. Anabolism is a self-regulating process by which a living organism can maintain internal stability. B. Homeostasis refers the synthesis of complex molecule from simpler ones together with the storage of energy. C. Tolerance is an ability of organisms to withstand or survive prevailing adverse conditions. D. Catabolism is the break down of complex molecules, an inverse process of Anabolism. Above all, the answer is A. Anabolism.
Action: Finish[A. Anabolism]
(END PREVIOUS TRIAL)

Reflection: The Thought explains that Anabolism plays a role in maintaining the normal state. However, the statment is factually incorrectm as B. Homeostasis actually refers to the self-regulating process and maintain the body normal state. so the initial answer is incorrect. I will revise the current answer when asked next time.
Thought: The refection above rejects the correctness of the previous Thought and reclaim that B. Homeostasis is the one which describes the ability to maintain body's noraml state. so the final answer is B. Homeostasis.
Action: Finish[B. Homeostasis]

Question: The pleura
Choices: 
A. have no sensory innervation
B. are separated by a 2 mm space
C. extend into the neck
D. are composed of respiratory epithelium
Thought: The pleura, the double-layered membranes that surround the lungs and line the chest cavity, do not have sensory innervation. This means that they are not sensitive to touch, pain, or other sensory stimuli. So the answer is A. have no sensory innervation
Action: Finish[A. have no sensory innervation]
(END PREVIOUS TRIAL)

Reflection: I apologize for any confusion earlier. Let's evaluate each choice: A. "have no sensory innervation" - This is not accurate. The pleura do have sensory innervation, and irritation or inflammation of the pleura can cause pleuritic chest pain. B. "are separated by a 2 mm space" - The pleura are actually in very close proximity to each other, with only a small amount of lubricating fluid between them. They do not have a 2 mm space between them. C. "extend into the neck" - This is not true. The pleura do not extend into the neck. D. "are composed of respiratory epithelium" - The pleura are indeed composed of a specialized type of epithelium called mesothelium. This epithelium is responsible for producing a lubricating fluid that allows smooth movement of the lungs within the chest cavity. Given the accurate information about the pleura's composition, the correct answer is D. 
Thought: The reflection gives contradictary knowledge about if pleura has sensory innervation. According to my knowledge about pleura and I double-check the information, the correct clarification is "The pleura do have sensory innervation". I also review the other choices carefully and agree with the reflection, so the final answer is D. are composed of respiratory epithelium
Action: Finish[D. are composed of respiratory epithelium]
"""

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

COT_SELF_CONTRADICT = """
Statement: The L0 norm is the number of non-zero elements in a vector, while the L1 and L2 norm are the sum of absolute values and sum of squares of the vector elements respectively. It is not possible to zero out coefficients of w using the L0 norm, so the answer must be either B. L1 norm or C. L2 norm.

Assesment: Let's break it down: The L0 norm indeed counts the number of non-zero elements in a vector, while the L1 norm is the sum of absolute values of the vector's elements, and the L2 norm is the square root of the sum of squares of the vector's elements. The L0 norm does not encourage zeroing out coefficients directly; instead, it promotes sparsity by encouraging as few non-zero coefficients as possible. If you want to encourage some coefficients to be exactly zero, you typically use L1 regularization (Lasso) because it tends to produce sparse solutions by setting some coefficients to zero. L2 regularization (Ridge) doesn't directly set coefficients to zero; it shrinks them toward zero but rarely makes them exactly zero.

Results: The statement you provided is partially correct, but it contains a minor inaccuracy: L2 norm does not directly promote zero coefficients; it only shrinks them toward zero.


Statement: A wave transfers energy from one point to another through a medium. The amplitude of a wave is the maximum displacement of the medium from its rest position. The wavelength is the distance between two successive crests or troughs of a wave. The frequency is the number of waves that pass a given point in a second

Assement: Let's break down each part: This statement correctly identifies that waves are a means of energy transfer. Waves transmit energy without necessarily moving the entire medium. This definition of amplitude is accurate. Amplitude measures how much a wave's disturbance deviates from its equilibrium or rest position. This definition of wavelength is also correct. Wavelength is the spatial period of the wave, typically measured from crest to crest or trough to trough. This is an accurate definition of frequency. It quantifies how many wave cycles (e.g., crests or troughs) pass a fixed point per unit of time (usually per second, measured in hertz).

Results: Overall, the statement provides a concise and accurate description of key wave properties and concepts.
"""



COT_KNOWLEDGE_COMPARE = """
Statement: 
Factual knowledge:
Comparision: 

Statement: 
Factual knowledge:
Comparision: 

Statement: 
Factual knowledge:
Comparision: 
"""

COT_STEM_QA = """Question: Which terms describes the body's ability to maintain its normal state?
Thought: Homeostasis a self-regulating process by which a living organism can maintain internal stability.
Action: Finish[Homeostasis]

Question: Say the pupil of your eye has a diameter of 5 mm and you have a telescope with an aperture of 50 cm. How much more light can the telescope gather than your eye?
Thought: The area of a circle is calculated using the formula A = πr^{2}, where A represents the area and r represents the radius of the circle. The diameter (r) of your eye's pupil is 5 mm and the diameter (r) of the telescope's aperture is 50 cm (500 mm), which is 100 times as your eye's pupil (5 mm), and r^{2} is 10000 times. So 10000 times.
Action: Finish[1000 times]

Question: You are pushing a truck along a road. Would it be easier to accelerate this truck on Mars? Why? (Assume there is no friction)?
Thought: In the absence of friction, the force required to accelerate the truck on Earth or Mars would indeed be the same, given the same mass (m) and desired acceleration (a). According to Newton's second law of motion (F = ma), the force required to accelerate an object is directly proportional to its mass and acceleration. So the answer is It would be the same no matter where you are.
Action: Finish[It would be the same no matter where you are]
"""

#HUMANITY
COT_HUMANITY = """Question: Select the best translation into predicate logic. All kings are luckier than all paupers. (Kx: x is a king; Px: x is a pauper; Lxy: x is luckier than y).
A. (∀x)[Kx ⊃ (∀y)(Py ⊃ Lxy)]
B. (∀x)[Kx ⊃ (∀y)(Lxy ⊃ Py)]
C. (∀x)(∀y)[(Kx • Py) ⊃ Lyx]
D. (∀x)[(Kx • (∀y)(Py)) ⊃ Lxy]
Thought: Let's break down the statement: All kings are luckier than all paupers. Now, let's represent the components using predicates: Kx: x is a king; Px: x is a pauper; Lxy: x is luckier than y. The translation into predicate logic would be (∀x)[(Kx • (∀y)(Py)) ⊃ Lxy], so the answer is A. (∀x)[Kx ⊃ (∀y)(Py ⊃ Lxy)].
Action: Finish[A. (∀x)[Kx ⊃ (∀y)(Py ⊃ Lxy)]

Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020?  Scenario 1 | I picked up my trash after the picnic in the park.  Scenario 2 | I kept a lot of comics in my bedroom.".
A. "Wrong, Wrong"
B. "Wrong, Not wrong"
C. "Not wrong, Wrong"
D. "Not wrong, Not wrong"
Thought: According to ordinary moral standards in the US as of 2020, neither Scenario 1 nor Scenario 2 involves doing something clearly morally wrong. So, the correct choice is D. "Not wrong, Not wrong".
Action: Finish[D. "Not wrong, Not wrong"]

Question: The Hopewell were complex rank societies, but they were not a state. Hopewell culture lacked all of the following elements EXCEPT:
A. formal government
B. monumental earthworks
C. urban centers
D. a permanent military
Thought: The area of a circle is calculated using the formula A = πr^{2}, where A represents the area and r represents the radius of the circle. The diameter (r) of your eye's pupil is 5 mm and the diameter (r) of the telescope's aperture is 50 cm (500 mm), which is 100 times as your eye's pupil (5 mm), and r^{2} is 10000 times. So the answer is C. 10000 times more
Action: Finish[C. 1000 times more]

Question: According to Kant, morality requires us to:
A. perform the action that leads to the greatest total happiness
B. act only on maxims that we can will to become universal laws
C. behave only in such a way as a perfectly virtuous person would behave
D. place the interests of others above the interests of ourselves
Thought: The crucial distinction lies in Kant's emphasis on universalizable maxims (B) rather than pursuing the greatest happiness (A), solely behaving virtuously (C), or prioritizing the interests of others above oneself (D). Kant's moral philosophy centers on the idea of acting according to principles that could be consistently applied by everyone. So the answer is B. 
Action: Finish[B. act only on maxims that we can will to become universal laws]

Question: Which of the following most accurately describes Hart's response to Fuller's argument concerning the invalidity of Nazi law?
A. The Nazi law in question was validly enacted
B. The court misunderstood the legislation
C. Fuller misconstrued the purpose of the law
D. The Nazi rule of recognition was unclear
Thought: Hart argued that the Nazi law, despite its moral reprehensibility, was validly enacted within the legal system's internal criteria, which aligns with choice A. B suggests an issue with the court's understanding of the legislation. C suggests a misunderstanding of the law's purpose. D refers to the clarity of the Nazi rule of recognition. So the answer is A. The Nazi law in question was validly enacted. 
Action: Finish[A. The Nazi law in question was validly enacted]
"""

#SOCIAL
COT_SOCIAL = """Question: Which one of the following is the most appropriate definition of a 99% confidence interval?
A. 99% of the time in repeated samples, the interval would contain the true value of the parameter
B. 99% of the time in repeated samples, the interval would contain the estimated value of the parameter
C. 99% of the time in repeated samples, the null hypothesis will be rejected
D. 99% of the time in repeated samples, the null hypothesis will not be rejected when it was false
Thought: This definition in A aligns with the concept of a confidence interval, indicating the level of confidence in which the interval, constructed from sample data, is expected to contain the true value of the population parameter in repeated sampling.
Action: Finish[A. 99% of the time in repeated samples, the interval would contain the true value of the parameter]

Question: Which of the following countries does NOT have a well-known example of a relict boundary?,A. Vietnam
B. United Kingdom
C. Germany
D. Bolivia
Thought: A. Vietnam has well-known examples of relict boundaries, particularly associated with the Vietnam War. The Demilitarized Zone that separated North and South Vietnam during the conflict is a notable relict boundary. B. United Kingdom has historical relict boundaries, such as Hadrian's Wall between England and Scotland. C. Germany has relict boundaries from the Cold War, notably the former border between West and East Germany. D. Bolivia has experienced various boundary changes and conflicts, but it may not have as many well-known examples of relict boundaries compared to some other countries. So the answer is D. Bolivia.
Action: Finish[D. Bolivia]

Question: Dan read a list of 30 vocabulary words only once. If he is typical and shows the serial position effect, we would expect that the words he remembers two days later are:
A. at the beginning of the list
B. in the middle of the list
C. at the end of the list
D. distributed throughout the list
Thought: According to the serial positioning effect, words at the beginning of the list are stored in your long-term memory. Words remembered at the end of the list are in your short-term memory, which lasts only 20 + seconds and would be forgotten 2 days later. Poorest recall would occur for words in the middle of the list. So the answer is A. at the beginning of the list.
Action: Finish[A. at the beginning of the list]

Question: Which of these principles is not an element of the responsibility to protect?
A. The responsibility to prevent
B. The responsibility to react
C. The responsibility to remain sovereign
D. The responsibility to rebuild
Thought: The other three principles: prevention (A), reaction (B), and rebuilding(D)—are typically considered elements of the responsibility to protect (R2P). So the answer is C. The responsibility to remain sovereign.
Action: Finish[C. The responsibility to remain sovereign]

Question: In idealized views of science, the experimental method is said to involve:
A. testing out new research methods to see which one works best
B. isolating and measuring the effect of one variable upon another
C. using personal beliefs and values to decide what to study
D. interpreting data subjectively, drawing on theoretical paradigms
Thought: Science experiment process typically includes manipulating one variable (independent variable) and observing the effect on another variable (dependent variable) while keeping other factors constant. It aims to establish cause-and-effect relationships and test hypotheses in a controlled and systematic manner. The other options mentioned do not accurately reflect the idealized experimental method in science. So the answer is B. isolating and measuring the effect of one variable upon another. 
Action: Finish[B. isolating and measuring the effect of one variable upon another]
"""

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
ADVICE_EXAMPLES = """Claim: Stranger Things is set in Bloomington, Indiana.
Advice: When verifying the claim "Stranger Things is set in Bloomington, Indiana," beware of pitfalls. Clarify any confusion between the show's fictional setting (Hawkins) and the claimed location (Bloomington). Rely on accurate sources like official show statements, credits, and creator statements to avoid misinformation. Scrutinize the opening credits and narrative for explicit mentions of the setting. Cross-verify with creators' statements to ensure clarity. Diligent verification addresses potential pitfalls and ensures accuracy.

Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
Advice: Verify the claim meticulously, considering pitfalls like potential misinterpretation of "Beautiful," verifying the accurate timeframe (2003), confirming the specific chart (Billboard Hot 100), ensuring reliability of sources, and distinguishing between lack of contradictory information ("Not Enough Information") and direct refutation ("Refutes").

Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Advice: The claim requires verification. Pitfalls include potential misinterpretation of "work," timeframe ambiguity, and varied project types (TV, film). Be cautious of missing but critical details that would lead to a classification of "Not Enough Information" rather than "Refutes.
"""

