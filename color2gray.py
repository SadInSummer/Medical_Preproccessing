import os
from PIL import Image


def convert_images_to_grayscale(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 获取文件的完整路径
        input_image_path = os.path.join(input_folder, filename)
        # 忽略文件夹以及非图像文件
        if os.path.isdir(input_image_path) or not any(
                input_image_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp']):
            continue

        # 打开图像
        image = Image.open(input_image_path)
        # 将图像转换为灰度图
        grayscale_image = image.convert("L")

        # 构建输出图像路径
        output_image_path = os.path.join(output_folder, filename)
        # 保存灰度图
        grayscale_image.save(output_image_path)


# 指定输入文件夹和输出文件夹的路径
input_folder = "./color"
output_folder = "./gray"

# 将输入文件夹中的所有图像转换为灰度图，并保存到输出文件夹中
convert_images_to_grayscale(input_folder, output_folder)
