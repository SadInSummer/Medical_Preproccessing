# import cv2
# import numpy as np
#
#
# def overlay_segmentation(image_path, mask_path, output_path, color=(0, 0, 255), alpha=0.5, bg_alpha=1.0):
#     """
#     将分割标签（白色部分）叠加到原图上，并以指定颜色显示。
#     :param image_path: 原始图片路径
#     :param mask_path: 分割标签路径
#     :param output_path: 输出图片路径
#     :param color: 叠加颜色，默认红色 (B, G, R)
#     :param alpha: 前景叠加透明度，默认0.5
#     :param bg_alpha: 背景透明度，默认1.0（不透明）
#     """
#     # 读取原图和分割标签
#     image = cv2.imread(image_path)
#     mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
#
#     # 创建颜色叠加层
#     overlay = np.zeros_like(image)
#     overlay[:, :] = color
#
#     # 只在白色（前景）区域应用颜色
#     mask_binary = (mask > 128).astype(np.uint8)  # 二值化
#     mask_colored = cv2.merge([mask_binary * color[0], mask_binary * color[1], mask_binary * color[2]])
#
#     # 叠加图片（前景透明度）
#     blended = cv2.addWeighted(image, bg_alpha, mask_colored, alpha, 0)
#
#     # 保存结果
#     cv2.imwrite(output_path, blended)
#
#
# # 示例调用
# overlay_segmentation("./fixed111.png", "./fixed-seg111.png", "./output.png", color=(255, 0, 0), alpha=0.5, bg_alpha=1)

# import cv2
# import numpy as np
#
#
# def overlay_segmentation(image_path, mask_path, output_path, color=(0, 0, 255), alpha=0.5, bg_alpha=1.0,
#                          contour_color=(255, 255, 255), contour_thickness=2):
#     """
#     将分割标签（白色部分）叠加到原图上，并以指定颜色显示，并添加外轮廓。
#     :param image_path: 原始图片路径
#     :param mask_path: 分割标签路径
#     :param output_path: 输出图片路径
#     :param color: 叠加颜色，默认红色 (B, G, R)
#     :param alpha: 前景叠加透明度，默认0.5
#     :param bg_alpha: 背景透明度，默认1.0（不透明）
#     :param contour_color: 轮廓颜色，默认白色 (B, G, R)
#     :param contour_thickness: 轮廓线宽度，默认2
#     """
#     # 读取原图和分割标签
#     image = cv2.imread(image_path)
#     mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
#
#     # 创建颜色叠加层
#     overlay = np.zeros_like(image)
#     overlay[:, :] = color
#
#     # 只在白色（前景）区域应用颜色
#     mask_binary = (mask > 128).astype(np.uint8)  # 二值化
#     mask_colored = cv2.merge([mask_binary * color[0], mask_binary * color[1], mask_binary * color[2]])
#
#     # 叠加图片（前景透明度）
#     blended = cv2.addWeighted(image, bg_alpha, mask_colored, alpha, 0)
#
#     # 计算轮廓
#     contours, _ = cv2.findContours(mask_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # 在叠加图像上绘制轮廓
#     cv2.drawContours(blended, contours, -1, contour_color, contour_thickness)
#
#     # 保存结果
#     cv2.imwrite(output_path, blended)
#
#
# # 示例调用
# overlay_segmentation("./ww.png", "./warped-seg111.png", "./www.png", color=(0, 255, 0), alpha=1, bg_alpha=1,
#                      contour_color=(255, 255, 255), contour_thickness=3)


import cv2
import numpy as np


def overlay_contours(image_path, mask_path, output_path, contour_color=(255, 255, 255), contour_thickness=2):
    """
    仅在原图上显示分割标签的外轮廓。
    :param image_path: 原始图片路径
    :param mask_path: 分割标签路径
    :param output_path: 输出图片路径
    :param contour_color: 轮廓颜色，默认白色 (B, G, R)
    :param contour_thickness: 轮廓线宽度，默认2
    """
    # 读取原图和分割标签
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # 检查是否成功加载
    if image is None:
        raise FileNotFoundError(f"无法加载图像: {image_path}")
    if mask is None:
        raise FileNotFoundError(f"无法加载分割标签: {mask_path}")

    # 计算轮廓
    mask_binary = (mask > 128).astype(np.uint8)  # 二值化
    contours, _ = cv2.findContours(mask_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 在原图上绘制轮廓
    cv2.drawContours(image, contours, -1, contour_color, contour_thickness)

    # 保存结果
    cv2.imwrite(output_path, image)


# 示例调用
overlay_contours("./ww.bmp", "./warped-seg104.png", "./res.bmp", contour_color=(0, 255, 0), contour_thickness=5)