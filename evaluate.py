import json
import os

class MCTSNode:
    def __init__(self,
                 id,  # agent
                 depth,
                 reward,
                 cum_rewards,
                 question,
                 choices,
                 key,
                 advice,
                 thought,
                 answer,
                 answer_list,
                 is_correct,
                 children,
                 answer_clean,

                 ):

        self.id = id
        self.depth = depth
        self.reward = reward
        self.cum_rewards = cum_rewards
        self.question = question
        self.choices = choices
        self.key = key
        self.advice = advice
        self.thought = thought
        self.answer = answer
        self.answer_list = answer_list
        self.is_correct = is_correct
        self.children = children
        self.answer_clean = answer_clean


def load_tree_from_json(filename):
    with open(filename, 'r') as file:
        tree_dict = json.load(file)

    def dict_to_node(node_dict, parent=None):
        node = MCTSNode(
            id=node_dict["id"],
            depth=node_dict["depth"],
            reward=node_dict["reward"],
            cum_rewards=node_dict["cum_rewards"],
            question=node_dict["question"],
            choices=node_dict["choices"],
            key=node_dict["key"],
            advice=node_dict["advice"],
            thought=node_dict["thought"],
            answer=node_dict["answer"],
            answer_list=node_dict["answer_list"],
            is_correct=node_dict["is_correct"],
            answer_clean=node_dict["answer_clean"],
            children=[]
        )
        try:
            node.gene_detail = node_dict["gene_detail"]
        except:
            pass
        if node_dict["children"]:
            node.children = [dict_to_node(child, parent=node) for child in node_dict["children"]]
        return node

    return dict_to_node(tree_dict)


def find_n_node(node, n=None):
    current = node
    if n is not None:
        for i in range(n):
            if current.children:
                current = current.children[0]
    else:
        while current.children:
            current = current.children[0]
    return current.is_correct



def most_common(lst):
    frequency = {}
    max_count = 0
    most_common_element = None

    for item in lst:

        frequency[item] = frequency.get(item, 0) + 1

        if frequency[item] > max_count:
            max_count = frequency[item]
            most_common_element = item
        elif frequency[item] == max_count and most_common_element is None:

            most_common_element = item

    return most_common_element

from collections import Counter

change = []
def cut_tree(root):

    head_answer = find_most_common_answer_clean(root, 1)

    count = 0
    stack = [root]
    while stack:
        layer = []
        while stack:
            layer.append(stack.pop())
        for node in layer:
            for child in node.children:
                stack.append(child)
        answer_list = [node.answer_clean for node in layer]
        frequency = Counter(answer_list)
        most_common = frequency.most_common(1)
        answer= most_common[0][0]
        count += 1
        # if max_node.reward > target_reward:
        #     return max_node.answer_clean == root.key
    if count > 2:
        if answer != head_answer:
            # print('yes', answer, head_answer)
            change.append(1)
        else:

            change.append(0)
    return root.key == answer

def find_most_common_answer_clean(node, target_depth):
    if node is None or target_depth < 0:
        return None

    stack = [(node, 0)]
    answer_clean_list = []

    while stack:
        current_node, current_depth = stack.pop()

        if current_depth == target_depth:
            answer_clean_list.append(current_node.answer_clean)
        elif current_depth < target_depth:
            for child in current_node.children:
                stack.append((child, current_depth + 1))

    if answer_clean_list:
        most_common_answer = most_common(answer_clean_list)
        return most_common_answer

    return None

def n_layer_common(root, target_depth):
    most_common_answer_clean = find_most_common_answer_clean(root, target_depth)
    if most_common_answer_clean is None:
        return None
    if most_common_answer_clean is not None:
        return root.key == most_common_answer_clean
    return False


def collect_answer_clean_recursive(node, answer_clean_list):
    if node is None:
        return

    answer_clean_list.append(node.answer_clean)

    for child in node.children:
        collect_answer_clean_recursive(child, answer_clean_list)


def have_key(root):
    def collect_answer_clean_recursive(node, answer_clean_list):
        if node is None:
            return

        answer_clean_list.append(node.answer_clean)

        for child in node.children:
            collect_answer_clean_recursive(child, answer_clean_list)
    answer_clean_list = []
    collect_answer_clean_recursive(root, answer_clean_list)
    if answer_clean_list:
        root_key = root.key
        if root_key in answer_clean_list:
            return True

    return False


def check_answer(directory, function_type, n=None, prob=None):
    file_list = [os.path.join(directory,file) for file in os.listdir(directory) if 'config' not in file]
    answers = []
    valid = []
    tag_list = []
    for file_path in file_list:
        # print(file_path)
        node = load_tree_from_json(file_path)
        if function_type == 'cut_tree':
            is_cor = cut_tree(node)
        elif function_type == 'n_layer_common':
            is_cor = n_layer_common(node, n)
        elif function_type == 'have_key':
            is_cor = have_key(node)
        answers.append(is_cor)
    # answers = [i for i in answers if i is not None]
    print(f'Num of total question: {len(answers)}, '
          f'correct num: {sum(answers)}, '
          f'correct rate: {float(sum(answers))/len(answers)}.')

def cut_tree_final(directory):
        global change
        print('The result of {} layer is:'.format(1))
        check_answer(directory, 'n_layer_common', 1)
        print('The last result is:')
        check_answer(directory, 'cut_tree')
        print('The have_key is:')
        check_answer(directory, 'have_key')

if __name__ == "__main__":

    cut_tree_final('./output/stem/gpt35/dep_3_wid_3_n_5_s_0_e_100_17_022616')
