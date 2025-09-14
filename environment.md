# 训练环境安装：

## 参考文件：
https://github.com/OpenDriveLab/DriveLM/blob/main/challenge/llama_adapter_v2_multimodal7b/README.md#L9

## 安装命令:
conda create -n drivelm python=3.8 -y
conda activate drivelm
cd ./DriveLM/challenge/llama_adapter_v2_multimodal7b
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/ -r requirements.txt

nvcc --version
pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/ torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

conda env export > environment.yml
conda env create -f environment.yml

# 测试环境安装：

## 参考文件：
https://github.com/bckim92/language-evaluation

## 安装命令:
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt-get install oracle-java8-installer
sudo apt install libxml-parser-perl

pip install git+https://github.com/bckim92/language-evaluation.git
python -c "import language_evaluation; language_evaluation.download('coco')"

## debug:
Oracle-Java8-Installer: No installation candidate: https://askubuntu.com/questions/790671/oracle-java8-installer-no-installation-candidate

cd /etc/apt/sources.list.d
sudo rm -rf webupd8team-ubuntu-java-bionic.list
sudo apt-get update
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt install default-jre