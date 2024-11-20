# import nibabel as nib
# import numpy as np
#
# def apply_mask_with_background_fix(ct_file, mask_file, output_file):
#     # 读取ct和mask文件
#     ct_img = nib.load(ct_file)
#     mask_img = nib.load(mask_file)
#
#     # 将数据转换为numpy数组
#     ct_data = ct_img.get_fdata()
#     mask_data = mask_img.get_fdata()
#
#     # 确保mask是二值化的
#     mask_data = np.where(mask_data > 0, 1, 0)
#
#     # 获取CT图像的最小值，用于背景填充
#     ct_min_value = np.min(ct_data)
#     print(f"CT image min value: {ct_min_value}")
#
#     # 创建一个副本，用来应用mask
#     masked_ct_data = np.copy(ct_data)
#
#     # 将mask外的区域设置为最小值（背景值）
#     masked_ct_data[mask_data == 0] = ct_min_value  # 或者可以直接设为0：masked_ct_data[mask_data == 0] = 0
#
#     # 创建新的NIfTI图像
#     masked_ct_img = nib.Nifti1Image(masked_ct_data, ct_img.affine, ct_img.header)
#
#     # 保存输出文件
#     nib.save(masked_ct_img, output_file)
#
# # 示例使用
# apply_mask_with_background_fix('ct_001.nii.gz', 'mr_001_brain_mask.nii.gz', 'ct_001.nii.gz')


import os
import nibabel as nib
import numpy as np

def apply_mask_with_background_fix(ct_file, mask_file, output_file):
    # 读取ct和mask文件
    ct_img = nib.load(ct_file)
    mask_img = nib.load(mask_file)

    # 将数据转换为numpy数组
    ct_data = ct_img.get_fdata()
    mask_data = mask_img.get_fdata()

    # 确保mask是二值化的
    mask_data = np.where(mask_data > 0, 1, 0)

    # 获取CT图像的最小值，用于背景填充
    ct_min_value = np.min(ct_data)
    print(f"CT image min value: {ct_min_value}")

    # 创建一个副本，用来应用mask
    masked_ct_data = np.copy(ct_data)

    # 将mask外的区域设置为最小值（背景值）
    masked_ct_data[mask_data == 0] = ct_min_value  # 或者可以直接设为0：masked_ct_data[mask_data == 0] = 0

    # 创建新的NIfTI图像
    masked_ct_img = nib.Nifti1Image(masked_ct_data, ct_img.affine, ct_img.header)

    # 保存输出文件
    nib.save(masked_ct_img, output_file)

def process_folders(ct_folder, mask_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历CT文件夹中的所有CT文件
    for ct_file in os.listdir(ct_folder):
        if ct_file.endswith('.nii.gz'):
            # 从CT文件名中提取编号
            ct_basename = ct_file.replace('.nii.gz', '')  # 去掉扩展名
            ct_id = ct_basename.replace('ct_', '')        # 提取编号（例如 001）

            # 构造对应的Mask文件名
            mask_file = f'mr_{ct_id}_brain_mask.nii.gz'

            # 检查Mask文件是否存在
            ct_path = os.path.join(ct_folder, ct_file)
            mask_path = os.path.join(mask_folder, mask_file)
            output_path = os.path.join(output_folder, ct_file)

            if os.path.exists(mask_path):
                print(f"Processing: {ct_path} with {mask_path}")
                apply_mask_with_background_fix(ct_path, mask_path, output_path)
            else:
                print(f"Skipping: {ct_path}, corresponding mask not found.")


# 文件夹路径
ct_folder = './ct'           # CT文件夹路径
mask_folder = './mask'       # Mask文件夹路径
output_folder = './newct'   # 输出文件夹路径

# 批量处理
process_folders(ct_folder, mask_folder, output_folder)
