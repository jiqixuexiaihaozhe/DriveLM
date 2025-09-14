# 数据下载：
subset of image data: https://huggingface.co/datasets/OpenDriveLab/DriveLM

full nuScenes dataset: https://www.nuscenes.org/download

llama_adapter_v2_multimodal7b
├── data/
│   ├── QA_dataset_nus/
│   │   ├── v1_1_train_nus.json
│   ├── nuscenes/
│   │   ├── samples/


git lfs install

git clone git@hf.co:datasets/OpenDriveLab/DriveLM

# 数据预处理：
Extract Data：
输入文件参考：/workspace/dataset/mmvlm/DriveLM/challenge/data/QA_dataset_nus/train_sample.json

cd /workspace/dataset/mmvlm/DriveLM/challenge/
python extract_data.py
输出文件参考：/workspace/dataset/mmvlm/DriveLM/challenge/test.json

Convert Data：
python convert_data.py
输出文件参考：/workspace/dataset/mmvlm/DriveLM/challenge/test_eval.json

Convert Data：
python convert2llama.py
输出文件参考：/workspace/dataset/mmvlm/DriveLM/challenge/test_llama.json