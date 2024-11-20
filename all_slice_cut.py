import nibabel as nib
import numpy as np
import os

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


def retain_common_slices_all_axes(ct_file, mri_file, output_ct_file, output_mri_file):
    # 读取ct和mri文件
    ct_img = nib.load(ct_file)
    mri_img = nib.load(mri_file)

    # 将CT和MRI数据转换为numpy数组
    ct_data = ct_img.get_fdata()
    mri_data = mri_img.get_fdata()

    # 确保CT和MRI的形状匹配
    if ct_data.shape != mri_data.shape:
        raise ValueError("CT和MRI图像的形状不匹配，无法处理。")

    # Step 1: 找到在z轴上都有的切片
    valid_slices_z = [i for i in range(ct_data.shape[2]) if np.any(ct_data[:, :, i]) and np.any(mri_data[:, :, i])]
    ct_data = ct_data[:, :, valid_slices_z]
    mri_data = mri_data[:, :, valid_slices_z]

    # Step 2: 找到在y轴上都有的切片
    valid_slices_y = [i for i in range(ct_data.shape[1]) if np.any(ct_data[:, i, :]) and np.any(mri_data[:, i, :])]
    ct_data = ct_data[:, valid_slices_y, :]
    mri_data = mri_data[:, valid_slices_y, :]

    # Step 3: 找到在x轴上都有的切片
    valid_slices_x = [i for i in range(ct_data.shape[0]) if np.any(ct_data[i, :, :]) and np.any(mri_data[i, :, :])]
    ct_data = ct_data[valid_slices_x, :, :]
    mri_data = mri_data[valid_slices_x, :, :]

    # 创建新的NIfTI图像，保持原始的affine和header
    new_ct_img = nib.Nifti1Image(ct_data, ct_img.affine, ct_img.header)
    new_mri_img = nib.Nifti1Image(mri_data, mri_img.affine, mri_img.header)

    # 保存处理后的CT和MRI文件
    nib.save(new_ct_img, output_ct_file)
    nib.save(new_mri_img, output_mri_file)


def process_folder(folder_path):
    # 获取ct、mr、mask文件的路径
    ct_path = os.path.join(folder_path, 'ct.nii.gz')
    mr_path = os.path.join(folder_path, 'mr.nii.gz')
    mask_path = os.path.join(folder_path, 'mask.nii.gz')

    # 生成临时的masked文件路径
    masked_ct_path = os.path.join(folder_path, 'masked_ct.nii.gz')
    masked_mr_path = os.path.join(folder_path, 'masked_mr.nii.gz')

    # 调用apply_mask_with_background_fix函数
    apply_mask_with_background_fix(ct_path, mask_path, masked_ct_path)
    apply_mask_with_background_fix(mr_path, mask_path, masked_mr_path)

    # 生成最终的new文件路径
    new_ct_path = os.path.join(folder_path, 'new_ct.nii.gz')
    new_mr_path = os.path.join(folder_path, 'new_mri.nii.gz')

    # 调用retain_common_slices_all_axes函数
    retain_common_slices_all_axes(masked_ct_path, masked_mr_path, new_ct_path, new_mr_path)


def process_all_folders(root_folder):
    # 遍历大文件夹中的所有小文件夹
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # 检查是否是目录
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_name}")
            process_folder(folder_path)


# 示例调用
root_folder = './pelvis'
process_all_folders(root_folder)

