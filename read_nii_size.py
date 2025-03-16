# import os
# import nibabel as nib
# from collections import defaultdict
#
#
# def count_nii_shapes(folder_path):
#     """计算指定文件夹下不同尺寸的 NIfTI 文件数量"""
#     shape_counts = defaultdict(int)
#     nii_files = [f for f in os.listdir(folder_path) if f.endswith('.nii') or f.endswith('.nii.gz')]
#
#     if not nii_files:
#         print("未找到 NIfTI 文件。")
#         return
#
#     for file in nii_files:
#         file_path = os.path.join(folder_path, file)
#         img = nib.load(file_path)
#         shape = img.shape
#         shape_counts[shape] += 1
#
#     print("不同尺寸的 NIfTI 文件数量:")
#     for shape, count in shape_counts.items():
#         print(f"{shape}: {count} 个")
#
#
# # 指定文件夹路径
# folder_path = "./IXI-T2"
# count_nii_shapes(folder_path)


import os
import nibabel as nib
import shutil
from collections import defaultdict


def count_nii_shapes(folder_path):
    """计算指定文件夹下不同尺寸的 NIfTI 文件数量，并将尺寸最多的文件移动到新文件夹"""
    shape_counts = defaultdict(int)
    shape_files = defaultdict(list)
    nii_files = [f for f in os.listdir(folder_path) if f.endswith('.nii') or f.endswith('.nii.gz')]

    if not nii_files:
        print("未找到 NIfTI 文件。")
        return

    for file in nii_files:
        file_path = os.path.join(folder_path, file)
        img = nib.load(file_path)
        shape = img.shape
        shape_counts[shape] += 1
        shape_files[shape].append(file_path)

    print("不同尺寸的 NIfTI 文件数量:")
    max_shape = max(shape_counts, key=shape_counts.get)
    for shape, count in shape_counts.items():
        print(f"{shape}: {count} 个")

    print(f"尺寸最多的文件尺寸: {max_shape}")

    # 创建目标文件夹
    target_folder = os.path.join(folder_path, "./xxx-t1")
    os.makedirs(target_folder, exist_ok=True)

    # 移动文件
    for file_path in shape_files[max_shape]:
        shutil.move(file_path, os.path.join(target_folder, os.path.basename(file_path)))

    print(f"已将 {len(shape_files[max_shape])} 个文件移动到 {target_folder}")


# 指定文件夹路径
folder_path = "./IXI-T1"
count_nii_shapes(folder_path)