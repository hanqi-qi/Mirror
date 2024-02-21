from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import torch

def load(ckpt_dir, model_type):
    n_gpus = torch.cuda.device_count()
    print("Run on %d gpu(s)"%n_gpus)
    if model_type == 'llama':
        # we use tensor parallel for loading llama
        tokenizer = LlamaTokenizer.from_pretrained(ckpt_dir, use_fast=False, padding_side="left")
        # model = LlamaForCausalLM.from_pretrained(ckpt_dir,load_in_8bit=True, device_map="auto",low_cpu_mem_usage = True, torch_dtype=torch.float16)
        model = LlamaForCausalLM.from_pretrained(ckpt_dir,load_in_8bit=False, device_map="auto",low_cpu_mem_usage = True, torch_dtype=torch.float16)
        # model = tp.tensor_parallel(model, [i for i in range(n_gpus)])
    elif model_type == "alpaca":
        model = pipeline(model="declare-lab/flan-alpaca-gpt4-xl",device=0)
        tokenizer = None
        # tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, use_fast=False, padding_side="left")
        print("Alpaca Loaded!")
    else:
        # however, tensor parallel for running falcon will occur bugs
        tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, use_fast=False, padding_side="left")
        model = AutoModelForCausalLM.from_pretrained(ckpt_dir, device_map = 'auto', torch_dtype=torch.bfloat16, trust_remote_code=True)

    if tokenizer is not None:
        tokenizer.pad_token_id = 0 if tokenizer.pad_token_id is None else tokenizer.pad_token_id
        tokenizer.bos_token_id = 1
    model.eval()
    return model, tokenizer

def prepare_input(tokenizer, prompts):
    input_tokens = tokenizer(prompts, return_tensors="pt")
    input_tokens = {k:input_tokens[k] for k in input_tokens if k in ["input_ids", "attention_mask"]}
    for t in input_tokens:
        if torch.is_tensor(input_tokens[t]):
            input_tokens[t] = input_tokens[t].to('cuda')

    return input_tokens

def process_result(output_sequence):
    #parse the thought from end to the start, until "Thought&Action" are both complete
    result = output_sequence[0].split("Action: ")[-1].split("\n")[0]
    return result

def llm_generate(model, tokenizer, prompts, temp, model_name, generated_tokens=None):
    answers = []
    if tokenizer is None:
        print("tokenizer is none")
        with torch.no_grad():
            output_sequence = model(prompts,max_length=-1,max_new_tokens=300, do_sample=False)
            answers.extend([seq['generated_text'] for seq in output_sequence])
    else:

        input_len = len(prompts.split(" "))
        input_tokens = tokenizer([prompts], return_tensors="pt").to("cuda")
        outputs = model.generate(**input_tokens, max_new_tokens=300,temperature=temp, output_scores=True,do_sample=True)
        output_sequence = tokenizer.decode(outputs[0], skip_special_tokens=True)
        generated_tokens = " ".join(output_sequence.split(" ")[input_len+1:])
        last_word = prompts.split("\n")[-1].strip().replace(':','')
        if "llama" in model_name or 'Llama' in model_name or 'bf521496' in model_name:
            if "70b" in model_name:
                input_len += 1

            if last_word == 'Advice':
                generated_tokens = " ".join(output_sequence.split(" ")[input_len-3:])
                response = generated_tokens.split("Question:")[0].strip().split("Advice:")[1].replace('(END OF EXAMPLE)','').strip()
            else:
                response = generated_tokens.split("\n")[0] #collect the first sentence as output.
        elif "vicuna" in model_name:
            generated_tokens = " ".join(output_sequence.split(" ")[input_len:])
            last_word = prompts.split("\n")[-1].strip().replace(':','')
            enerated_tokens = " ".join(output_sequence.split(" ")[input_len-3:])
            if last_word == 'Advice':
                generated_tokens = " ".join(output_sequence.split(" ")[input_len-3:])
                response = generated_tokens.split("Question:")[0].strip().split("Advice:")[1].replace('(END OF EXAMPLE)','').strip()
            else:
                response = generated_tokens.split("\n")[0]
    return output_sequence, response

