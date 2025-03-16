all_slice_cut.py is used to get the common slices of different nii.gz.


Resampling.py is used to resize nii.gz. (splicing change)
crop is used to resize,keep the splicing.

ROI_extract_follow_mask.py is to segment under mask.

add_size.py add blank slices into one alxil.


voxel_size.py get the voxel size of nii.gz. (the image is ITK guides to get spacing or voxel size)
![image](https://github.com/user-attachments/assets/9145b10f-519f-4d90-9218-01cafef7b128)


show_nii：input flow.nii and visualize the different slice and give the vector field.

read_npz.py/read.py/read_labels_ids2npz.py are used to read segment labels to generation .npz.

light.py is used to compare lightness between two images.

shfuu.py is used to shufflue data.
