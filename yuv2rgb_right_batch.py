# import numpy as np
# import cv2
#
#
# def imsave(image, path):
#     # Convert the image to uint8 before saving with OpenCV
#     image = (image)
#     cv2.imwrite(path, image)
#
# def rgb2yuv(rgb):
#     rgb = rgb.astype(np.float32)
#
#     m = [[0.299, 0.587, 0.114], [-0.147, -0.289, 0.436], [0.615, -0.515, -0.100]]
#     shape1 = rgb.shape
#     yuv = np.empty(shape1, dtype=np.float32)
#     for i in range(3):
#         yuv[:, :, i] = rgb[:, :, 0]*m[i][0] + rgb[:, :, 1]*m[i][1] + rgb[:, :, 2]*m[i][2]
#     return yuv
#
# def yuv2rgb(yuv):
#
#     mtxYUVtoRGB = np.array([[1.0000, -0.0000, 1.1398],
#                             [1.0000, -0.3946, -0.5805],
#                             [1.0000,  2.0320, -0.0005]])
#
#     # mtxYUVtoRGB = np.array([[1.0000, -0.000, 1.140],
#     #                         [1.0000, -0.395, -0.581],
#     #                         [1.0000,  2.032, -0.000]])
#
#
#     rgb = np.zeros(yuv.shape)
#     for i in range(3):
#         rgb[:, :, i] = yuv[:, :, 0] * mtxYUVtoRGB[i, 0] + yuv[:, :, 1] * mtxYUVtoRGB[i, 1] + yuv[:, :, 2] * mtxYUVtoRGB[i, 2]
#     return rgb
#
# #读彩色的那个图像
# img_rgb_gfp = cv2.imread('./PET/1.png', cv2.COLOR_BGR2RGB).astype(np.float32)
# img_yuv = rgb2yuv(img_rgb_gfp)
# img_yuv_y = img_yuv[:, :, 0]
# img_yuv_u = img_yuv[:, :, 1]*0.8
# img_yuv_v = img_yuv[:, :, 2]*0.8
#
# #读融合后的那个图像
# res_l = cv2.imread('./gray/1.png',cv2.IMREAD_GRAYSCALE).astype(np.float32)
# res_l = res_l.squeeze()
# h, w = res_l.shape
# res_l = np.reshape(res_l, [h, w, 1])
# # res_l = 255*(res_l - np.min(res_l)) / (np.max(res_l) - np.min(res_l))
# img_yuv_u = np.reshape(img_yuv_u, [h, w, 1])
# img_yuv_v = np.reshape(img_yuv_v, [h, w, 1])
# res_yuv = np.concatenate([res_l, img_yuv_u, img_yuv_v], axis=-1)
# res_rgb = yuv2rgb(res_yuv)
# imsave((res_rgb),'./color/1.png')
#
#
#
#
#
#
#
#
#
#
#
#

import os
import numpy as np
import cv2

def imsave(image, path):
    # Convert the image to uint8 before saving with OpenCV
    image = (image)
    cv2.imwrite(path, image)

def rgb2yuv(rgb):
    rgb = rgb.astype(np.float32)

    m = [[0.299, 0.587, 0.114], [-0.147, -0.289, 0.436], [0.615, -0.515, -0.100]]
    shape1 = rgb.shape
    yuv = np.empty(shape1, dtype=np.float32)
    for i in range(3):
        yuv[:, :, i] = rgb[:, :, 0]*m[i][0] + rgb[:, :, 1]*m[i][1] + rgb[:, :, 2]*m[i][2]
    return yuv

def yuv2rgb(yuv):
    mtxYUVtoRGB = np.array([[1.0000, -0.0000, 1.1398],
                            [1.0000, -0.3946, -0.5805],
                            [1.0000,  2.0320, -0.0005]])

    rgb = np.zeros(yuv.shape)
    for i in range(3):
        rgb[:, :, i] = yuv[:, :, 0] * mtxYUVtoRGB[i, 0] + yuv[:, :, 1] * mtxYUVtoRGB[i, 1] + yuv[:, :, 2] * mtxYUVtoRGB[i, 2]
    return rgb

def process_images(pet_folder, gray_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pet_files = [f for f in os.listdir(pet_folder) if os.path.isfile(os.path.join(pet_folder, f))]
    gray_files = [f for f in os.listdir(gray_folder) if os.path.isfile(os.path.join(gray_folder, f))]

    for pet_file, gray_file in zip(pet_files, gray_files):
        img_rgb_gfp = cv2.imread(os.path.join(pet_folder, pet_file), cv2.COLOR_BGR2RGB).astype(np.float32)
        img_yuv = rgb2yuv(img_rgb_gfp)
        img_yuv_y = img_yuv[:, :, 0]
        img_yuv_u = img_yuv[:, :, 1] * 0.8
        img_yuv_v = img_yuv[:, :, 2] * 0.8

        res_l = cv2.imread(os.path.join(gray_folder, gray_file), cv2.IMREAD_GRAYSCALE).astype(np.float32)
        res_l = res_l.squeeze()
        h, w = res_l.shape
        res_l = np.reshape(res_l, [h, w, 1])
        img_yuv_u = np.reshape(img_yuv_u, [h, w, 1])
        img_yuv_v = np.reshape(img_yuv_v, [h, w, 1])
        res_yuv = np.concatenate([res_l, img_yuv_u, img_yuv_v], axis=-1)
        res_rgb = yuv2rgb(res_yuv)
        output_path = os.path.join(output_folder, pet_file)
        imsave(res_rgb, output_path)

# Define your folders
pet_folder = './PET'
gray_folder = './gray'
output_folder = './color'

# Process the images
process_images(pet_folder, gray_folder, output_folder)

