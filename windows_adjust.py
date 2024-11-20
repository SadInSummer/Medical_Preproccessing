# import nibabel as  nb
#
# img = nb.load('./ct.nii.gz') #读取nii格式文件
# data = img.get_fdata()
#
#
# def adjustMethod1(data_resampled,w_width,w_center):
#     val_min = w_center - (w_width / 2)
#     val_max = w_center + (w_width / 2)
#
#     data_adjusted = data_resampled.copy()
#     data_adjusted[data_resampled < val_min] = val_min
#     data_adjusted[data_resampled > val_max] = val_max
#
#     return data_adjusted
#
# w_width = 150
# w_center = 50
# data_adjusted1 = adjustMethod1(data,w_width,w_center)
#
#
# adjusted_img = nb.Nifti1Image(data_adjusted1, img.affine, img.header)
#
# # 保存为新的nii.gz文件
# nb.save(adjusted_img, './cttt.nii.gz')

import os
import nibabel as nb

def adjustMethod1(data_resampled, w_width, w_center):
    val_min = w_center - (w_width / 2)
    val_max = w_center + (w_width / 2)

    data_adjusted = data_resampled.copy()
    data_adjusted[data_resampled < val_min] = val_min
    data_adjusted[data_resampled > val_max] = val_max

    return data_adjusted

def process_all_files(input_folder, output_folder, w_width, w_center):
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有 .nii.gz 文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.nii.gz'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 加载nii.gz文件
            img = nb.load(input_path)
            data = img.get_fdata()

            # 调整数据
            data_adjusted = adjustMethod1(data, w_width, w_center)

            # 创建新的NIfTI图像
            adjusted_img = nb.Nifti1Image(data_adjusted, img.affine, img.header)

            # 保存到输出文件夹
            nb.save(adjusted_img, output_path)
            print(f"Processed and saved: {output_path}")

# 参数设置
input_folder = './before'  # 输入文件夹路径
output_folder = './after'  # 输出文件夹路径
w_width = 150
w_center = 50

# 处理文件夹中的所有文件
process_all_files(input_folder, output_folder, w_width, w_center)

