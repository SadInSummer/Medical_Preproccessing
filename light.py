# import cv2
# import numpy as np
#
#
# def calculate_brightness_mean(image_path):
#     # 读取图像
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#
#     # 检查图像是否成功加载
#     if image is None:
#         raise ValueError("图像加载失败，请检查路径是否正确。")
#
#     # 计算图像的亮度均值
#     brightness_mean = np.mean(image)
#
#     return brightness_mean
#
#
# # 示例使用
# image_path = './1.png'  # 替换为实际图像路径
# brightness = calculate_brightness_mean(image_path)
# print(f"图像的亮度均值为: {brightness}")
#
#
# image_path2 = './MRI.png'  # 替换为实际图像路径
# brightness = calculate_brightness_mean(image_path2)
# print(f"图像的亮度均值为: {brightness}")
#
# image_path3 = './PET.png'  # 替换为实际图像路径
# brightness = calculate_brightness_mean(image_path3)
# print(f"图像的亮度均值为: {brightness}")

import cv2
import numpy as np


def calculate_histogram(image_path):
    # 读取图像并转换为灰度图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("图像加载失败，请检查路径是否正确。")

    # 计算灰度直方图
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    # 将直方图进行归一化处理
    histogram = cv2.normalize(histogram, histogram).flatten()
    return histogram


def compare_histograms(image_path1, image_path2):
    # 计算两个图像的灰度直方图
    histogram1 = calculate_histogram(image_path1)
    histogram2 = calculate_histogram(image_path2)

    # 计算直方图差异，使用交叉熵作为差异度量
    histogram_diff = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_BHATTACHARYYA)

    print(f"两个图像的灰度直方图差异（Bhattacharyya距离）: {histogram_diff}")


# 示例使用
image_path1 = './1.png'  # 替换为第一个图像路径
image_path2 = './MRI.png'  # 替换为第二个图像路径
compare_histograms(image_path1, image_path2)

