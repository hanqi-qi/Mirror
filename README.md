# Mirror

# Introduction
This repository is used in our paper:

Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning

Please cite our paper and kindly give a star for this repository if you use this code.

## Requirements

* Python 3.10.13
* PyTorch 2.1.0
* transformers 4.34.1


## Evaluate

For ChatGPT, we use the following command to evaluate the model:

```
python main.py -dataset_name social --ckpt_dir "gpt35" --model_type openai --max_tree_depth 3 --action_num 3 --self_consistency 5 --start_eid 0 --end_eid 100 --advice_type gene_demo --header_type 0  --n_trials 3  --cut_prob 0.8
```

For Llama2 or Vicuna, we use the following command to evaluate the model:

```
python main.py -dataset_name social --ckpt_dir your_llama_path --model_type llama --max_tree_depth 3 --action_num 3 --self_consistency 5 --start_eid 0 --end_eid 100 --advice_type gene_demo --header_type 0  --n_trials 3  --cut_prob 0.4
```
