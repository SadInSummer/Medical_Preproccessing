import nibabel as nib

# 读取 NIfTI 文件
file_path = "./after/ct.nii.gz"
img = nib.load(file_path)

# 获取头信息
header = img.header

# 查看 voxel size
voxel_size = header.get_zooms()

print("Voxel size:", voxel_size)
