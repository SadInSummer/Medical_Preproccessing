# #修改了size和voxel size
#
# import os
# import SimpleITK as sitk
#
#
# # def resample_to_target_size(input_path, output_path, target_size):
# #     # 读取原始图像
# #     image = sitk.ReadImage(input_path)
# #
# #     # 获取原始图像的尺寸和空间分辨率
# #     original_size = image.GetSize()  # 原始图像尺寸 (z, y, x)
# #     original_spacing = image.GetSpacing()  # 原始空间分辨率
# #
# #     # 计算新的空间分辨率，使得重采样后的图像尺寸为 target_size
# #     new_spacing = []
# #     for i in range(3):
# #         new_spacing.append(original_spacing[i] * (original_size[i] / target_size[i]))
# #
# #     # 计算新的尺寸
# #     new_size = target_size  # 目标尺寸
# #
# #     # 执行重采样
# #     image_resampled = sitk.Resample(image, new_size, sitk.Transform(), sitk.sitkLinear,
# #                                     image.GetOrigin(), new_spacing, image.GetDirection(),
# #                                     -1000.0, sitk.sitkFloat32)
# #
# #     # 保存重采样后的图像
# #     sitk.WriteImage(image_resampled, output_path)
# #
# #
# # def process_folder(input_folder, output_folder, target_size):
# #     os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹
# #
# #     # 遍历文件夹中的所有 .nii.gz 文件
# #     for filename in os.listdir(input_folder):
# #         if filename.endswith('.nii.gz'):
# #             input_path = os.path.join(input_folder, filename)
# #             output_path = os.path.join(output_folder, filename)
# #
# #             # 调用重采样函数
# #             resample_to_target_size(input_path, output_path, target_size)
# #             print(f'Resampled: {filename} -> {output_path}')
# #
# #
# # if __name__ == "__main__":
# #     input_folder = './before'  # 输入文件夹路径
# #     output_folder = './after'  # 输出文件夹路径
# #     target_size = (160, 192, 160)  # 指定的目标尺寸
# #     process_folder(input_folder, output_folder, target_size)
#
#
#
# # 修改了size和voxel size
# # 1会丢一点
# import os
# import SimpleITK as sitk
#
#
# def resample_to_target_size_keep_spacing(input_path, output_path, target_size):
#     # 读取原始图像
#     image = sitk.ReadImage(input_path)
#
#     # 获取原始图像的方向、原点和空间分辨率（spacing）
#     original_spacing = image.GetSpacing()  # 保持原始 spacing 不变
#     origin = image.GetOrigin()
#     direction = image.GetDirection()
#
#     # 获取原始图像的尺寸
#     original_size = image.GetSize()
#
#     # 目标尺寸
#     new_size = target_size
#
#     # 计算新的原点，使得图像内容居中
#     new_origin = [
#         origin[i] + (original_size[i] - new_size[i]) * original_spacing[i] / 2
#         for i in range(3)
#     ]
#
#     # 执行重采样，保持原始 spacing 和原点
#     resampler = sitk.ResampleImageFilter()
#     resampler.SetSize(new_size)
#     resampler.SetOutputSpacing(original_spacing)  # 使用原始 spacing
#     resampler.SetOutputDirection(direction)
#     resampler.SetOutputOrigin(new_origin)  # 修改原点，使得内容居中
#     resampler.SetInterpolator(sitk.sitkLinear)  # 线性插值
#     resampler.SetDefaultPixelValue(-1000.0)  # 默认为 CT 图像的背景值
#
#     # 进行重采样
#     resampled_image = resampler.Execute(image)
#
#     # 保存重采样后的图像
#     sitk.WriteImage(resampled_image, output_path)
#
#
# def process_folder_keep_spacing(input_folder, output_folder, target_size):
#     os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹
#
#     # 遍历文件夹中的所有 .nii.gz 文件
#     for filename in os.listdir(input_folder):
#         if filename.endswith('.nii.gz'):
#             input_path = os.path.join(input_folder, filename)
#             output_path = os.path.join(output_folder, filename)
#
#             # 调用重采样函数
#             resample_to_target_size_keep_spacing(input_path, output_path, target_size)
#             print(f'Resampled: {filename} -> {output_path}')
#
#
# if __name__ == "__main__":
#     input_folder = './before'  # 输入文件夹路径
#     output_folder = './after'  # 输出文件夹路径
#     target_size = (80, 192, 160)  # 指定的目标尺寸
#     process_folder_keep_spacing(input_folder, output_folder, target_size)


import os
import SimpleITK as sitk


def resample_to_target_size(input_path, output_path, target_size):
    # 读取原始图像
    image = sitk.ReadImage(input_path)

    # 获取原始图像的尺寸和空间分辨率
    original_size = image.GetSize()  # 原始图像尺寸 (z, y, x)
    original_spacing = image.GetSpacing()  # 原始空间分辨率

    # 计算新的空间分辨率，使得重采样后的图像尺寸为 target_size
    new_spacing = []
    for i in range(3):
        new_spacing.append(original_spacing[i] * (original_size[i] / target_size[i]))

    # 计算新的尺寸
    new_size = target_size  # 目标尺寸

    # 执行重采样
    image_resampled = sitk.Resample(image, new_size, sitk.Transform(), sitk.sitkLinear,
                                    image.GetOrigin(), new_spacing, image.GetDirection(),
                                    -1000.0, sitk.sitkFloat32)

    # 保存重采样后的图像
    sitk.WriteImage(image_resampled, output_path)


def process_folder(input_folder, output_folder, target_size):
    os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹

    # 遍历文件夹中的所有 .nii.gz 文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.nii.gz'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 调用重采样函数
            resample_to_target_size(input_path, output_path, target_size)
            print(f'Resampled: {filename} -> {output_path}')


if __name__ == "__main__":
    input_folder = './before'  # 输入文件夹路径
    output_folder = './after'  # 输出文件夹路径
    target_size = (160, 192, 80)  # 指定的目标尺寸
    process_folder(input_folder, output_folder, target_size)


