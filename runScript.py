import os

#os.system("main.py --model_name= 12heads_linevul_model.bin  --output_dir=./saved_models  --model_type=roberta  --tokenizer_name=microsoft/codebert-base  --model_name_or_path=microsoft/codebert-base --do_test --do_local_explanation  --top_k_constant=10 --reasoning_method=attention --test_data_file='/Users/puneet/Documents/Uni Related/Semester 4/Internship/ML Model/testflaw1.csv'  --block_size 512  --eval_batch_size 197")
import subprocess

csvpath = '/Users/puneet/Documents/Uni Related/Semester 4/Internship/ML Model/testflaw1.csv'
output = subprocess.check_output("python main.py --model_name=12heads_linevul_model.bin  --output_dir=./saved_models  --model_type=roberta  --tokenizer_name=microsoft/codebert-base  --model_name_or_path=microsoft/codebert-base --do_test --do_local_explanation  --top_k_constant=10 --reasoning_method=attention --block_size 512  --eval_batch_size 197 --test_data_file='/Users/puneet/Documents/Uni Related/Semester 4/Internship/ML Model/testflaw1.csv'", shell=True)
print(output)

