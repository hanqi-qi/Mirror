import math
from copy import deepcopy
from typing import Optional, Callable
import itertools
import json
import numpy as np
from tqdm import trange


class MCTSNode:
    id_iter = itertools.count()

    @classmethod
    def reset_id(cls):
        cls.id_iter = itertools.count()

    def __init__(self,
                 state,  # agent
                 action,
                 reward: float = 0,
                 parent: "Optional[MCTSNode]" = None,
                 is_terminal: bool = False,
                 calc_q: Callable[[list[float]], float] = np.mean):
        self.id = next(MCTSNode.id_iter)
        self.cum_rewards: list[float] = []
        self.is_terminal = is_terminal
        # self.node_agent = node_agent
        self.reward = reward
        self.action = action
        self.state = state
        self.parent = parent
        self.self_consistency = 0
        self.children: 'Optional[list[MCTSNode]]' = None
        self.calc_q = calc_q
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.answer_list = []
    # noinspection PyPep8Naming
    @property
    def Q(self) -> float:
        if self.state is None:
            return self.fast_reward
        else:
            return self.calc_q(self.cum_rewards)

    def to_dict(self):

        return {
            "id": self.id,
            "depth": self.depth,
            "reward": self.reward,
            "cum_rewards": self.cum_rewards,
            "question": self.state.question,
            "choices": self.state.choices,
            "key": self.state.key,
            "advice": self.state.reflect_advice,
            "thought": self.state.thought_or_reflection,
            "answer": self.state.answer,
            "answer_clean": self.state.clean_answer,
            "answer_list": self.answer_list,
            "is_correct": self.state.is_correct,
            'gene_detail' : self.state.generate_output,
            "children": [child.to_dict() for child in self.children] if self.children else None
        }


#
def save_tree_to_json(root, filename):
    tree_dict = root.to_dict()
    with open(filename, 'w') as file:
        json.dump(tree_dict, file, indent=4)

class MCTS:
    def __init__(self,
                 cut_prob : float = 1,
                 output_trace_in_each_iter: bool = False,
                 self_consistency: int = 1,
                 agent=None,
                 w_exp: float = 1.,
                 depth_limit: int = 5,
                 n_iters: int = 10,
                 cum_reward: Callable[[list[float]], float] = np.mean,
                 calc_q: Callable[[list[float]], float] = np.mean,
                 simulate_strategy: str | Callable[[list[float]], int] = 'max',
                 output_strategy: str = 'max_reward',
                 disable_tqdm: bool = True,
                 save_path: str = ''
                 ):

        # self.world_model = None
        self.cut_prob = cut_prob
        self.agent = agent
        self.search_config = None
        self.self_consistency = self_consistency
        # record trace
        self.output_trace_in_each_iter = output_trace_in_each_iter
        # the weight of exploration in UCT
        self.w_exp = w_exp
        self.depth_limit = depth_limit
        self.n_iters = n_iters
        # how to calculate cum_reward
        self.cum_reward = cum_reward
        #  calc_q: the way to calculate the Q value from histories. Defaults: np.mean
        self.calc_q = calc_q
        self.save_path = save_path
        default_simulate_strategies: dict[str, Callable[[list[float]], int]] = {
            'max': lambda x: np.argmax(x),
            'sample': lambda x: np.random.choice(len(x), p=x),
            'random': lambda x: np.random.choice(len(x)),
        }
        self.simulate_choice: Callable[[list[float]], int] = default_simulate_strategies.get(simulate_strategy,
                                                                                             simulate_strategy)
        assert output_strategy in ['max_reward', 'follow_max', 'max_visit', 'max_iter', 'last_iter',
                                   'last_terminal_iter']
        self.output_strategy = output_strategy
        # self.uct_with_fast_reward = uct_with_fast_reward
        self._output_iter: list[MCTSNode] = None
        self._output_cum_reward = -math.inf
        self.trace_in_each_iter: list[list[MCTSNode]] = None
        self.root: Optional[MCTSNode] = None
        self.disable_tqdm = disable_tqdm

    def visualize_tree_symbols(self,node, prefix=""):
        tree_str = ""

        if prefix == "":
            tree_str += "●\n"
        else:
            tree_str += prefix[:-3] + "└── ●\n"

        if node.children:
            for i, child in enumerate(node.children):
                if i < len(node.children) - 1:
                    tree_str += self.visualize_tree_symbols(child, prefix + "|   ")
                else:
                    tree_str += self.visualize_tree_symbols(child, prefix + "    ")

        return tree_str

    def _is_terminal_with_depth_limit(self, node: MCTSNode):
        return node.is_terminal or node.depth >= self.depth_limit

    def iterate(self, node: MCTSNode) -> list[MCTSNode]:
        # return a select path
        path = self._select(node)
        # not reach terminal
        if not self._is_terminal_with_depth_limit(path[-1]) and not self.stop_flag:
            self._expand(path[-1])
            self._simulate(path)
            path_all = [path + [child] for child in path[-1].children]
            for _path in path_all:
                cum_reward = self._back_propagate(_path)
        return path

    def _select(self, node: MCTSNode) -> list[MCTSNode]:
        path = []
        while True:
            path.append(node)
            if node.children is None or len(node.children) == 0 or self._is_terminal_with_depth_limit(node):
                return path
            node = self._sub_select(node)

    def _uct(self, node: MCTSNode) -> float:
        value = node.Q + self.w_exp * np.sqrt(np.log(len(node.parent.cum_rewards)) / max(1, len(node.cum_rewards)))
        return value

    def _sub_select(self, node: MCTSNode) -> MCTSNode:
        return max(node.children, key=self._uct)

    def _expand_child(self, node, action_list):
        node_list = []
        answer_list = []
        for action in action_list:
            for i in range(self.self_consistency):
                child_agent = deepcopy(node.state)
                child = MCTSNode(state=child_agent, action=action, parent=node, calc_q=self.calc_q)
                child.state.do_action(action)
                # child.reward = child.state.get_reward()
                node_list.append(child)
                answer_list.append(child.state.clean_answer)
                if child.state.clean_answer != node.state.clean_answer:
                    child.reward = 1
                else:
                    child.reward = 0

        probability_dict = {}
        for item in answer_list:
            probability_dict[item] = probability_dict.get(item, 0) + 1
        for key in probability_dict:
            probability_dict[key] = probability_dict[key] / len(answer_list)
        for i in range(len(node_list)):
            node_list[i].reward += probability_dict[node_list[i].state.clean_answer]
            node_list[i].self_consistency = probability_dict[node_list[i].state.clean_answer]


        return node_list

    def _expand(self, node: MCTSNode):
        print("----------------expand------------")
        actions = node.state.get_actions(node.self_consistency)
        children = self._expand_child(node, actions)
        node.children = children
        if max([node.self_consistency for node in children]) >= self.cut_prob:
            self.stop_flag = True

    def _simulate(self, path: list[MCTSNode]):
        node = path[-1]
        while True:

            if node.depth + 1 < self.depth_limit and not self.stop_flag:
                # choose child node
                rewards = [child.reward for child in node.children]
                chosen_index = self.simulate_choice(rewards)

                # back_propagation remain child
                remaining_children = [child for i, child in enumerate(node.children) if i != chosen_index]
                for child_remain in remaining_children:
                    self._back_propagate(path+[child_remain])

                # expand
                node = node.children[chosen_index]
                self._expand(node)
                path.append(node)
            else:
                print(self.visualize_tree_symbols(self.root))
                return

    def _back_propagate(self, path: list[MCTSNode]):
        rewards = []
        cum_reward = -math.inf
        for node in reversed(path):
            rewards.append(node.reward)
            cum_reward = self.cum_reward(rewards[::-1]) # np.mean
            node.cum_rewards.append(cum_reward)
        return cum_reward

    def _dfs_max_reward(self, path: list[MCTSNode]) -> tuple[float, list[MCTSNode]]:
        cur = path[-1]
        if cur.is_terminal:
            return self.cum_reward([node.reward for node in path[1:]]), path
        if cur.children is None:
            return -math.inf, path
        visited_children = [x for x in cur.children if x.state is not None]
        if len(visited_children) == 0:
            return -math.inf, path
        return max((self._dfs_max_reward(path + [child]) for child in visited_children), key=lambda x: x[0])

    def _get_root(self, node):
        node_list = []
        answer_list = []
        for i in range(self.self_consistency):
            root = MCTSNode(state=deepcopy(self.agent), action=None, parent=node, calc_q=self.calc_q)
            root.state.initial()
            node_list.append(root)
            answer_list.append(root.state.clean_answer)
        probability_dict = {}
        for item in answer_list:
            probability_dict[item] = probability_dict.get(item, 0) + 1
        for key in probability_dict:
            probability_dict[key] = probability_dict[key] / len(answer_list)
        for i in range(len(node_list)):
            node_list[i].reward = probability_dict[node_list[i].state.clean_answer]
            node_list[i].self_consistency = probability_dict[node_list[i].state.clean_answer]
            # node_list[i].cum_rewards.append() = probability_dict[node_list[i].state.clean_answer]
        for _node in node_list:
            self._back_propagate([node, _node])

        return node_list
    def search(self):
        self._output_cum_reward = -math.inf
        self._output_iter = None
        # create root node
        self.root = MCTSNode(state=self.agent, action=None, parent=None, calc_q=self.calc_q)
        self.root.children = self._get_root(self.root)

        if max([node.self_consistency for node in self.root.children]) >= self.cut_prob:
            return

        for _ in trange(self.n_iters, disable=self.disable_tqdm, desc='MCTS iteration', leave=False):
            path = self.iterate(self.root)

    def __call__(self):
        MCTSNode.reset_id()
        self.stop_flag = False

        self.search()
        save_tree_to_json(self.root, self.save_path)

        return