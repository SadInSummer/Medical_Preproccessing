# # 修改size
# import SimpleITK as sitk
#
# # 读取原始 NIfTI 文件
# input_file = "./after/mr_001.nii.gz"
# output_file = "./mr_0001.nii.gz"
#
# image = sitk.ReadImage(input_file)
#
# # 获取当前的 spacing 和 size
# original_spacing = image.GetSpacing()
# original_size = image.GetSize()
#
# print("Original Spacing:", original_spacing)
# print("Original Size:", original_size)
#
# # 定义新的 spacing
# new_spacing = (1.0, 1.0, 1.0)  # 新的 voxel size
#
# # 计算新的 size，保持物理尺寸不变
# new_size = [
#     int(round(original_size[i] * (original_spacing[i] / new_spacing[i])))
#     for i in range(3)
# ]
#
# print("New Spacing:", new_spacing)
# print("New Size:", new_size)
#
# # 使用 SimpleITK 的 Resample 函数调整 spacing
# resampler = sitk.ResampleImageFilter()
# resampler.SetOutputSpacing(new_spacing)
# resampler.SetSize(new_size)
# resampler.SetOutputDirection(image.GetDirection())
# resampler.SetOutputOrigin(image.GetOrigin())
# resampler.SetInterpolator(sitk.sitkLinear)  # 可根据需要调整插值方式
#
# resampled_image = resampler.Execute(image)
#
# # 保存调整后的图像
# sitk.WriteImage(resampled_image, output_file)
#
# print("Resampling completed. New file saved as:", output_file)


# 不修改size，有种被拉宽的感觉
import SimpleITK as sitk

# 读取原始 NIfTI 文件
input_file = "./after/mr_001.nii.gz"
output_file = "./mr_00001.nii.gz"

image = sitk.ReadImage(input_file)

# 获取原始 spacing 和 size
original_spacing = image.GetSpacing()
original_size = image.GetSize()

print("Original Spacing:", original_spacing)
print("Original Size:", original_size)

# 修改 spacing（仅修改元数据，不插值）
new_spacing = (1.0, 1.0, 1.0)  # 新的 spacing

# 替换 spacing 信息
image.SetSpacing(new_spacing)

# 保存新的图像文件
sitk.WriteImage(image, output_file)

print("Spacing updated without resizing. New file saved as:", output_file)
