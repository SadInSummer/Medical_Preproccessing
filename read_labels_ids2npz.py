import SimpleITK as sitk
import numpy as np

# 读取 nii.gz 文件
nii_file = './mr_180.nii.gz'
image = sitk.ReadImage(nii_file)

# 转换为 NumPy 数组
image_array = sitk.GetArrayFromImage(image)

# 获取标签（唯一值）并去掉 0 值
labels = np.unique(image_array)
labels = labels[labels != 0]  # 去掉 0 标签

# 打印标签
print(f"Labels in the file (excluding 0): {labels}")

# 创建字典并保存标签
data_dict = {'labels': labels}

# 保存标签字典到 npz 文件
np.savez('./label_mind.npz', **data_dict)

print(f"Labels saved to './label_mind.npz'")
