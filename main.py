import os
import joblib
import argparse
import numpy as np
from model import load
from mcts import MCTS
import json
from langchain import OpenAI
from tqdm import tqdm
from datetime import datetime
from agents_module import CoTAgent
from evaluate import cut_tree_final
from prompt import tutor_agent_prompt_fever, tutor_reflect_prompt_fever, tutor_agent_prompt, tutor_reflect_prompt
from demonstration import TUTOR_REFLECTION_STEM, TUTOR_STEM,  TUTOR_STEM_NOADVCIE, COT_FEVER,TUTOR_REFLECTION_FEVER
os.environ['OPENAI_API_KEY'] = ""



def create_output_directory(root, dataset_name, model_name):
    time_now = datetime.now().strftime("%d_%H%M%S")
    dic_name = 'dep_{}_wid_{}_n_{}_s_{}_e_{}_{}'.format(args.max_tree_depth,args.action_num,args.self_consistency,args.start_eid,args.end_eid,time_now)
    path = os.path.join(root, dataset_name, model_name, dic_name)
    print(path)
    os.makedirs(path, exist_ok=True)
    return path

def save_args_to_json(args, filename):
    args_dict = vars(args)
    with open(filename, 'w') as file:
        json.dump(args_dict, file, indent=4)


def main():
    # load datasets
    if args.dataset_name == "fever":
        mmlu = joblib.load(f'./data/fever_100.joblib')
    elif args.dataset_name == "humanity":
        mmlu = joblib.load(f'./data/humanity_mmlu_100.joblib')
    elif args.dataset_name == "stem":
        mmlu = joblib.load(f'./data/stem_mmlu_100.joblib')
    elif args.dataset_name == "other":
        mmlu = joblib.load(f'./data/other_mmlu_100.joblib')
    elif args.dataset_name == "social":
        mmlu = joblib.load(f'./data/social_mmlu_100.joblib')
    mmlu = mmlu.reset_index(drop=True)[args.start_eid:args.end_eid]
    # prepare model
    if args.model_type == "openai":
        llm_model = OpenAI(temperature=args.temperature,
                           max_tokens=250,
                           model_name="gpt-3.5-turbo-0125",
                           model_kwargs={"stop": "\n"},
                           # openai_api_key=os.environ['OPENAI_API_KEY']
                           )
        tokenizer = None
    else:
        llm_model, tokenizer = load(args.ckpt_dir, args.model_type)

    # print model dataset
    model_name = (args.ckpt_dir.split("/")[-1]).lower()
    print(f"Using {args.model_type}, {model_name}, {args.dataset_name}, {args.advice_type}")
    output_dir = create_output_directory(args.output_root_path,args.dataset_name, model_name)
    save_args_to_json(args, os.path.join(output_dir,'config.json'))


    # prepare cot examples and reflect_examples
    cot_examples_mapping = {
            "stem": TUTOR_STEM_NOADVCIE if args.advice_type == "none" else TUTOR_STEM,
            "humanity": TUTOR_STEM,
            "social": TUTOR_STEM,
            "other": TUTOR_STEM,
            "fever": COT_FEVER,
    }
    cot_reflection_examples_mapping = {
        "stem":  TUTOR_REFLECTION_STEM,
        "other":  TUTOR_REFLECTION_STEM,
        "humanity": TUTOR_REFLECTION_STEM,
        "social": TUTOR_REFLECTION_STEM,
        "hotpotqa": TUTOR_REFLECTION_STEM,
        "fever": TUTOR_REFLECTION_FEVER,
    }

    # cot_examples = cot_examples_mapping.get(args.dataset_name, COT_STEM)
    # cot_examples = TUTOR_STEM_5 if args.model_type == "llama" else TUTOR_STEM
    cot_examples = cot_examples_mapping[args.dataset_name]
    print(f"Using {'InDom' if args.dataset_name in cot_examples_mapping else 'OOD'} demonstrations: {args.dataset_name if args.dataset_name in cot_examples_mapping else 'STEM'}")
    reflect_examples = cot_reflection_examples_mapping[args.dataset_name]

    agent_prompt = tutor_agent_prompt if args.dataset_name != 'fever' else tutor_agent_prompt_fever
    reflect_prompt = tutor_reflect_prompt if args.dataset_name != 'fever' else tutor_reflect_prompt_fever


    for idx, row in tqdm(mmlu.iterrows(), total=mmlu.shape[0]):
        print('--------------{}--------------'.format(idx))
        cot_agent = CoTAgent(  # question and answer
            header_type=args.header_type,
            question=row['question'],
            choices=f"\nChoices:\nA. {row['A']}\nB. {row['B']}\nC. {row['C']}\nD. {row['D']}\n" if args.dataset_name != 'fever' else '' ,  # choice text
            key=row[row['answer']] if args.dataset_name != 'fever' else row['answer'],  # answer text
            action_num=args.action_num,
            dataset_name = args.dataset_name,

            model_name=model_name,
            model_type=args.model_type,
            temp=args.temperature,
            advice_type = args.advice_type,
            self_reflect_llm=llm_model,
            action_llm=llm_model,
            tokenizer=tokenizer,

            agent_prompt=agent_prompt,
            cot_examples=cot_examples,  # demonstrations
            reflect_prompt=reflect_prompt,
            reflect_examples=reflect_examples,

        )

        MCTS_agent = MCTS(
            cut_prob = args.cut_prob,
            output_trace_in_each_iter=False,
            self_consistency=args.self_consistency,
            agent=cot_agent,
            depth_limit=args.max_tree_depth,
            n_iters=args.n_trials,
            # cum_reward=sum,
            calc_q=np.mean,
            simulate_strategy='max',
            output_strategy='max_reward',
            disable_tqdm=True,
            save_path =  os.path.join(output_dir,'{}.json'.format(idx))
        )
        MCTS_agent()
    print(output_dir)
    cut_tree_final(output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ckpt_dir', default="your_model_path", type=str, required=False)
    parser.add_argument('--temperature', default=0.9, type=float, help='the diversity of generated text')
    parser.add_argument('--model_type', default="openai", type=str, required=False)
    parser.add_argument('--start_eid', default=0, type=int, required=False)
    parser.add_argument('--end_eid', default=1, type=int, required=False)
    parser.add_argument('--dataset_name', default="other", type=str, required=False)

    parser.add_argument('--n_trials', default=3, type=int, required=False, help='repeat n_trials times')
    parser.add_argument('--max_tree_depth', default=3, type=int, required=False, help='max_tree_depth')
    parser.add_argument('--action_num', default=3, type=int, required=False)
    parser.add_argument('--self_consistency', default=5, type=int, required=False, help='self_consistency')

    parser.add_argument('--output_root_path', default='./output', type=str, required=False, help='max_tree_depth')
    parser.add_argument('--advice_type', default='gene_demo', type=str, required=False, help='different advice none, fix , gene')
    parser.add_argument('--header_type', default=1, type=int, required=False, help='different header type')
    parser.add_argument('--cut_prob', default=0.6, type=float, required=False, help='repeat n_trials times')

    args = parser.parse_args()

    main()
