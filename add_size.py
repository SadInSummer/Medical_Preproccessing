import os
import SimpleITK as sitk
import numpy as np


def add_black_slices_folder(input_folder, output_folder, target_size, axis=2):
    """
    对文件夹内的所有 nii.gz 图像，在指定轴上添加全黑 slices 以达到目标尺寸。

    参数:
        input_folder (str): 输入文件夹路径。
        output_folder (str): 输出文件夹路径。
        target_size (int): 在指定轴上扩展后的目标尺寸。
        axis (int): 要扩展的轴，0:x轴，1:y轴，2:z轴。
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".nii.gz"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 读取原始图像
            image = sitk.ReadImage(input_path)
            array = sitk.GetArrayFromImage(image)  # 转为 numpy 数组 (z, y, x)

            # 获取当前尺寸和目标尺寸
            current_size = array.shape[axis]
            if current_size >= target_size:
                print(f"跳过文件 {filename}：当前尺寸 {current_size} >= 目标尺寸 {target_size}")
                continue

            # 计算需要填充的大小
            pad_size = target_size - current_size
            pad_before = pad_size // 2
            pad_after = pad_size - pad_before

            # 构造填充参数
            pad_width = [(0, 0), (0, 0), (0, 0)]  # (z, y, x)
            pad_width[axis] = (pad_before, pad_after)

            # 填充全黑 slices
            padded_array = np.pad(array, pad_width=pad_width, mode='constant', constant_values=0)

            # 将 numpy 数组转回 SimpleITK 图像
            padded_image = sitk.GetImageFromArray(padded_array)

            # 设置新图像的元数据
            new_spacing = list(image.GetSpacing())
            new_origin = list(image.GetOrigin())
            new_direction = image.GetDirection()

            if axis == 0:
                new_origin[0] -= pad_before * new_spacing[0]
            elif axis == 1:
                new_origin[1] -= pad_before * new_spacing[1]
            elif axis == 2:
                new_origin[2] -= pad_before * new_spacing[2]

            padded_image.SetSpacing(new_spacing)
            padded_image.SetOrigin(new_origin)
            padded_image.SetDirection(new_direction)

            # 保存图像
            sitk.WriteImage(padded_image, output_path)
            print(f"已处理文件 {filename}，保存至 {output_path}，新尺寸为 {padded_array.shape[::-1]} (x, y, z)。")


# 示例用法
input_folder = "./before"  # 输入文件夹路径
output_folder = "./after"  # 输出文件夹路径
target_z_size = 224  # 目标 z 轴尺寸

add_black_slices_folder(input_folder, output_folder, target_size=target_z_size, axis=0)
