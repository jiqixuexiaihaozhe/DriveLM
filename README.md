# Environment:
environment.md

# Dataset Download:
dataset_download.md

# Model Download:
model_download.md

# dirvelm Task:
## train:
cd ./DriveLM/challenge/llama_adapter_v2_multimodal7b
bash ./exps/finetune.sh

## val:
cd ./DriveLM/challenge/
python evaluation_nogpt.py

## inference:
cd ./DriveLM/challenge/llama_adapter_v2_multimodal7b
python demo.py 

## vis:
cd ./DriveLM/challenge/llama_adapter_v2_multimodal7b
task_vis.ipynb