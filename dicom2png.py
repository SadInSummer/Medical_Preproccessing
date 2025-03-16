import SimpleITK as sitK
import numpy as np
import cv2
import os


def convert_from_dicom_to_png(img, low_window, high_window, save_path):
    lungwin = np.array([low_window * 1., high_window * 1.])
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])  # 归一化
    newimg = (newimg * 255).astype('uint8')  # 扩展像素值到【0，255】
    cv2.imwrite(save_path, newimg)


ds_array = sitK.ReadImage('./1-05.dcm')
img_array = sitK.GetArrayFromImage(ds_array)
shape = img_array.shape
img_array = np.reshape(img_array, (shape[1], shape[2]))
high = np.max(img_array)
low = np.min(img_array)
convert_from_dicom_to_png(img_array, low, high, './1.png')

