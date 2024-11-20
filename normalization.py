import os
import nibabel as nib
import numpy as np

# 你提供的归一化函数
def normalise(image):
    np_img = np.clip(image, -1000., 800.).astype(np.float32)
    return np_img

def whitening(image):
    image = image.astype(np.float32)
    mean = np.mean(image)
    std = np.std(image)
    if std > 0:
        return (image - mean) / std
    else:
        return image * 0.

def normalise_zero_one(image):
    image = image.astype(np.float32)
    minimum = np.min(image)
    maximum = np.max(image)
    if maximum > minimum:
        return (image - minimum) / (maximum - minimum)
    else:
        return image * 0.

def normalise_one_one(image):
    ret = normalise_zero_one(image)
    ret *= 2.
    ret -= 1.
    return ret

# 处理函数
def process_and_save(input_dir, output_dir, normalise_func):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.nii.gz'):
            filepath = os.path.join(input_dir, filename)
            img = nib.load(filepath)
            img_data = img.get_fdata()

            # 对整个3D图像进行归一化，而不是按方向处理
            norm_data = normalise_func(img_data)

            # 保存归一化后的图像
            norm_img = nib.Nifti1Image(norm_data, img.affine, img.header)
            output_filepath = os.path.join(output_dir, filename)
            nib.save(norm_img, output_filepath)
            print(f"Saved: {output_filepath}")

# 设置输入输出目录
input_dir = './before'  # 输入文件夹路径
output_dir = './after'  # 输出文件夹路径

# 选择归一化方法
normalise_func = normalise_zero_one  # 可以替换为whitening, normalise_zero_one, normalise_one_one

# 执行处理
process_and_save(input_dir, output_dir, normalise_func)
