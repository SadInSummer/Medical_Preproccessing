import nibabel as nib
import numpy as np

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

# 示例使用
retain_common_slices_all_axes('masked_ct.nii.gz', 'masked_mr.nii.gz', 'new_ct.nii.gz', 'new_mri.nii.gz')
