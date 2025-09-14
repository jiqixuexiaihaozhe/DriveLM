import torch

# 1. 检查基础信息
print(f"PyTorch version: {torch.__version__}") # 应该显示 2.0.0+cu117
print(f"CUDA available: {torch.cuda.is_available()}") # 核心：检查是否可用
print(f"CUDA version used by PyTorch: {torch.version.cuda}") # 会显示 11.7

# 2. 如果CUDA可用，进行一个简单的张量运算测试
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.randn(3, 3).to(device)
    y = torch.randn(3, 3).to(device)
    z = x + y
    print(f"Test computation on GPU successful: {z}")
    print(f"Current GPU device: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is NOT available. It will fall back to CPU.")