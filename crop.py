import os
import nibabel as nib
import numpy as np


# 裁剪函数：保持原始图像的内容居中
def crop_image_centered(image, target_size):
    """
    裁剪图像到目标大小，并尽量保持原图中心位置。

    参数:
    - image: 输入的3D图像 (numpy array)
    - target_size: 目标大小 (depth, height, width)

    返回:
    - cropped_image: 裁剪后的图像
    """
    original_shape = image.shape
    target_depth, target_height, target_width = target_size

    # 找到非零区域
    def find_bounds(data):
        non_zero = np.where(data > 0)
        min_index = np.min(non_zero)
        max_index = np.max(non_zero) + 1
        return min_index, max_index

    z_min, z_max = find_bounds(np.max(np.max(image, axis=1), axis=1))
    y_min, y_max = find_bounds(np.max(np.max(image, axis=0), axis=1))
    x_min, x_max = find_bounds(np.max(np.max(image, axis=0), axis=0))

    # 计算非零区域中心
    z_center = (z_min + z_max) // 2
    y_center = (y_min + y_max) // 2
    x_center = (x_min + x_max) // 2

    # 计算裁剪区域的起始和结束位置
    z_start = max(0, z_center - target_depth // 2)
    y_start = max(0, y_center - target_height // 2)
    x_start = max(0, x_center - target_width // 2)

    z_end = z_start + target_depth
    y_end = y_start + target_height
    x_end = x_start + target_width

    # 确保裁剪范围不超出原始图像
    z_start = max(0, min(z_start, original_shape[0] - target_depth))
    y_start = max(0, min(y_start, original_shape[1] - target_height))
    x_start = max(0, min(x_start, original_shape[2] - target_width))

    z_end = z_start + target_depth
    y_end = y_start + target_height
    x_end = x_start + target_width

    # 裁剪图像
    cropped_image = image[z_start:z_end, y_start:y_end, x_start:x_end]
    return cropped_image


# 归一化函数
def normalize_image(image, normalization_type="minmax"):
    """
    对图像进行归一化处理。

    参数:
    - image: 输入的3D图像 (numpy array)
    - normalization_type: 归一化类型 ("minmax" 或 "zscore")

    返回:
    - normalized_image: 归一化后的图像
    """
    if normalization_type == "minmax":
        # 将图像值归一化到 [0, 1]
        min_val = np.min(image)
        max_val = np.max(image)
        if max_val > min_val:  # 避免除以零
            normalized_image = (image - min_val) / (max_val - min_val)
        else:
            normalized_image = image  # 如果最大值等于最小值，不做归一化
    elif normalization_type == "zscore":
        # Z-Score 标准化 (均值为0，标准差为1)
        mean_val = np.mean(image)
        std_val = np.std(image)
        if std_val > 0:  # 避免除以零
            normalized_image = (image - mean_val) / std_val
        else:
            normalized_image = image  # 如果标准差为0，不做归一化
    else:
        raise ValueError("Unsupported normalization type. Choose 'minmax' or 'zscore'.")

    return normalized_image

# 遍历文件夹并处理每个 nii.gz 文件
data_path = './after'
target_size = (160, 192, 160)
output_root = './tttt'

for root, dirs, files in os.walk(data_path):
    for file in files:
        if file.endswith(".nii.gz"):
            file_path = os.path.join(root, file)

            # 加载 NIfTI 文件
            nii_image = nib.load(file_path)
            image_data = nii_image.get_fdata()  # 获取图像数据

            print(f"正在处理文件: {file}")
            print(f"原始图像形状: {image_data.shape}")

            # 裁剪图像
            cropped_data = crop_image_centered(image_data, target_size)
            print(f"裁剪后图像形状: {cropped_data.shape}")

            # 归一化图像
            normalized_data = normalize_image(cropped_data, normalization_type="minmax")
            print(f"归一化完成，数据范围: [{np.min(normalized_data)}, {np.max(normalized_data)}]")

            # 保存裁剪后的文件
            cropped_nii = nib.Nifti1Image(normalized_data, nii_image.affine, nii_image.header)
            output_path = os.path.join(output_root, f"{file}")
            nib.save(cropped_nii, output_path)
            print(f"裁剪后的文件已保存到: {output_path}")