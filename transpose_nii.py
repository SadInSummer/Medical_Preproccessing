import nibabel as nib
import numpy as np

# 定义输入和输出路径
input_path = "./flow.nii.gz"
output_path = "./new_flow.nii.gz"

# 读取原始形变场nii文件
img = nib.load(input_path)
deformation_array = img.get_fdata()  # 获取形变场数据 (3, 160, 192, 160)

# 调整维度顺序为 (160, 192, 160, 3)
transposed_array = np.transpose(deformation_array, (1, 2, 3, 0))

# 创建新的NIfTI对象
transposed_img = nib.Nifti1Image(transposed_array, affine=img.affine, header=img.header)

# 保存新的形变场nii文件
nib.save(transposed_img, output_path)

print(f"Transposed deformation field saved to {output_path}")
