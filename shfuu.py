import os
import random
import shutil

# 原始和目标文件夹路径
source_folder = "./voll"  # 修改为你的源文件夹路径
target_folder = "./vol"  # 修改为你的目标文件夹路径

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 获取所有nii.gz文件
files = [f for f in os.listdir(source_folder) if f.startswith("ct_") and f.endswith(".nii.gz")]

# 随机打乱文件顺序
random.shuffle(files)

# 重新命名并复制到目标文件夹
for idx, file in enumerate(files, start=1):
    new_name = f"ct_{idx:03d}.nii.gz"
    source_path = os.path.join(source_folder, file)
    target_path = os.path.join(target_folder, new_name)
    shutil.copy2(source_path, target_path)
    print(f"Copied {file} -> {new_name}")

print("All files have been shuffled and renamed successfully!")
