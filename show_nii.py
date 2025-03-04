#
# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件
#     :param file_path: 形变场文件路径
#     :return: 形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()
#     print(f"Displacement field shape: {displacement_field.shape}")
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#
#     # 设置颜色映射为 coolwarm 或其他合适的颜色映射
#     plt.imshow(slice_data, cmap='coolwarm')
#     plt.colorbar()
#     plt.title(f"Displacement field (direction={direction}, slice={slice_idx})")
#     plt.show()
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化向量场
#     :param displacement_field: 形变场数据
#     :param slice_idx: 切片索引
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     height, width = displacement_field.shape[2], displacement_field.shape[3]
#
#     x, y = np.meshgrid(
#         np.arange(0, width, step),
#         np.arange(0, height, step)
#     )
#
#     u = displacement_field[0, slice_idx, y, x]
#     v = displacement_field[1, slice_idx, y, x]
#
#     # 根据形变的强度计算颜色（将灰色用于形变小的区域）
#     magnitude = np.sqrt(u**2 + v**2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#
#     # 使用gray颜色映射并保证shape一致
#     colors = plt.cm.gray(normalized_magnitude.flatten())  # 将颜色展平，适配quiver
#
#     plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1,
#                color=colors)  # 使用灰度颜色映射
#     plt.title(f"Vector field (slice {slice_idx})")
#     plt.gca().invert_yaxis()
#     plt.show()
#
#
#
# def main():
#     # 设置形变场文件路径
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=5)
#
#
# if __name__ == "__main__":
#     main()
#
#


# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件，并调整维度顺序
#     :param file_path: 形变场文件路径
#     :return: 调整后的形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
#     print(f"Original displacement field shape: {displacement_field.shape}")
#
#     # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
#     displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
#     print(f"Reformatted displacement field shape: {displacement_field.shape}")
#
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#
#     # 设置颜色映射为 coolwarm
#     # plt.imshow(slice_data, cmap='coolwarm')
#     plt.imshow(slice_data, cmap='gray')
#     plt.colorbar()
#     plt.title(f"Displacement field (direction={direction}, slice={slice_idx})")
#     plt.show()
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化向量场
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     height, width = displacement_field.shape[2], displacement_field.shape[3]
#
#     x, y = np.meshgrid(
#         np.arange(0, width, step),
#         np.arange(0, height, step)
#     )
#
#     u = displacement_field[0, slice_idx, y, x]
#     v = displacement_field[1, slice_idx, y, x]
#
#     # 根据形变的强度计算颜色
#     magnitude = np.sqrt(u**2 + v**2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#
#     # 生成灰度颜色映射
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#
#     plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.title(f"Vector field (slice {slice_idx})")
#     plt.gca().invert_yaxis()
#     plt.show()
#
#
# def main():
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=4)
#
#
# if __name__ == "__main__":
#     main()


# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件，并调整维度顺序
#     :param file_path: 形变场文件路径
#     :return: 调整后的形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
#     print(f"Original displacement field shape: {displacement_field.shape}")
#
#     # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
#     displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
#     print(f"Reformatted displacement field shape: {displacement_field.shape}")
#
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#
#     # 设置颜色映射为 coolwarm
#     plt.imshow(slice_data, cmap='gray')
#     plt.colorbar()
#     plt.title(f"Displacement field (direction={direction}, slice={slice_idx})")
#     plt.show()
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化三个方向的向量场
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param slice_idx: 切片索引
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     height, width = displacement_field.shape[2], displacement_field.shape[3]
#
#     fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
#     directions = ['x', 'y', 'z']
#     for idx, direction in enumerate(directions):
#         ax = axes[idx]
#
#         if direction == 'x':
#             u = displacement_field[0, slice_idx, :, :]
#             v = displacement_field[1, slice_idx, :, :]
#         elif direction == 'y':
#             u = displacement_field[0, :, slice_idx, :]
#             v = displacement_field[2, :, slice_idx, :]
#         elif direction == 'z':
#             u = displacement_field[1, :, :, slice_idx]
#             v = displacement_field[2, :, :, slice_idx]
#
#         # 根据形变的强度计算颜色
#         magnitude = np.sqrt(u ** 2 + v ** 2)
#         normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#
#         # 生成灰度颜色映射
#         colors = plt.cm.gray(normalized_magnitude.flatten())
#
#         # 可视化每个方向的向量场
#         ax.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#         ax.set_title(f"Vector field ({direction} direction, slice {slice_idx})")
#         ax.invert_yaxis()
#
#     plt.tight_layout()
#     plt.show()
#
#
# def main():
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化三个方向的向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=4)
#
#
# if __name__ == "__main__":
#     main()


# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件，并调整维度顺序
#     :param file_path: 形变场文件路径
#     :return: 调整后的形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
#     print(f"Original displacement field shape: {displacement_field.shape}")
#
#     # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
#     displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
#     print(f"Reformatted displacement field shape: {displacement_field.shape}")
#
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#
#     # 设置颜色映射为 coolwarm
#     plt.imshow(slice_data, cmap='gray')
#     plt.colorbar()
#     plt.title(f"Displacement field (direction={direction}, slice={slice_idx})")
#     plt.show()
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化三个方向的向量场
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param slice_idx: 切片索引
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     height, width = displacement_field.shape[2], displacement_field.shape[3]
#
#     # 可视化 x 方向的向量场
#     plt.figure()
#     u = displacement_field[0, slice_idx, :, :]
#     v = displacement_field[1, slice_idx, :, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.title(f"Vector field (x direction, slice {slice_idx})")
#     plt.gca().invert_yaxis()
#     plt.show()
#
#     # 可视化 y 方向的向量场
#     plt.figure()
#     u = displacement_field[0, :, slice_idx, :]
#     v = displacement_field[2, :, slice_idx, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.title(f"Vector field (y direction, slice {slice_idx})")
#     plt.gca().invert_yaxis()
#     plt.show()
#
#     # 可视化 z 方向的向量场
#     plt.figure()
#     u = displacement_field[1, :, :, slice_idx]
#     v = displacement_field[2, :, :, slice_idx]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.5, color=colors)
#     plt.title(f"Vector field (z direction, slice {slice_idx})")
#     plt.gca().invert_yaxis()
#     plt.show()
#
#
# def main():
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化三个方向的向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=2)
#
#
# if __name__ == "__main__":
#     main()


# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件，并调整维度顺序
#     :param file_path: 形变场文件路径
#     :return: 调整后的形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
#     print(f"Original displacement field shape: {displacement_field.shape}")
#
#     # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
#     displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
#     print(f"Reformatted displacement field shape: {displacement_field.shape}")
#
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#
#     plt.imshow(slice_data, cmap='gray')
#     # plt.colorbar()
#     plt.axis('off')  # 不显示坐标轴
#     plt.show()
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化三个方向的向量场
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param slice_idx: 切片索引
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     depth, height, width = displacement_field.shape[1], displacement_field.shape[2], displacement_field.shape[3]
#
#     # 可视化 x 方向的向量场
#     plt.figure(figsize=(width / 50, height / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[0, slice_idx, :, :]
#     v = displacement_field[1, slice_idx, :, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#     plt.show()
#
#     # 可视化 y 方向的向量场
#     plt.figure(figsize=(width / 50, depth / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[0, :, slice_idx, :]
#     v = displacement_field[2, :, slice_idx, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#     plt.show()
#
#     # 可视化 z 方向的向量场
#     plt.figure(figsize=(height / 50, width / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[1, :, :, slice_idx]
#     v = displacement_field[2, :, :, slice_idx]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#     plt.show()
#
#
# def main():
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化三个方向的向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=4)
#
#
# if __name__ == "__main__":
#     main()

# import nibabel as nib
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def load_displacement_field(file_path):
#     """
#     加载形变场nii文件，并调整维度顺序
#     :param file_path: 形变场文件路径
#     :return: 调整后的形变场数据，形状为 (3, depth, height, width)
#     """
#     displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
#     print(f"Original displacement field shape: {displacement_field.shape}")
#
#     # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
#     displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
#     print(f"Reformatted displacement field shape: {displacement_field.shape}")
#
#     return displacement_field
#
#
# def visualize_single_component(displacement_field, direction=0, slice_idx=80):
#     """
#     可视化某方向的形变场分量
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param direction: 方向索引 (0=x, 1=y, 2=z)
#     :param slice_idx: 切片索引 (沿 depth 方向)
#     """
#     slice_data = displacement_field[direction, slice_idx, :, :]
#     plt.imshow(slice_data, cmap='gray')
#     # plt.colorbar()
#     plt.axis('off')  # 不显示坐标轴
#
#     # 调整图像边界，去掉多余的空白区域
#     plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
#     # plt.tight_layout()
#     # plt.show()
#     plt.savefig('./output.png', bbox_inches='tight', pad_inches=0, dpi=600)
#
#
# def visualize_vector_field(displacement_field, slice_idx=80, step=10):
#     """
#     可视化三个方向的向量场
#     :param displacement_field: 形变场数据 (3, depth, height, width)
#     :param slice_idx: 切片索引
#     :param step: 采样步长，用于稀疏显示向量
#     """
#     depth, height, width = displacement_field.shape[1], displacement_field.shape[2], displacement_field.shape[3]
#
#     # 可视化 x 方向的向量场
#     plt.figure(figsize=(width / 50, height / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[0, slice_idx, :, :]
#     v = displacement_field[1, slice_idx, :, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.5, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#
#     # 调整图像边界，去掉多余的空白区域
#     plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
#     plt.show()
#
#     # 可视化 y 方向的向量场
#     plt.figure(figsize=(width / 50, depth / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[0, :, slice_idx, :]
#     v = displacement_field[2, :, slice_idx, :]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#
#     # 调整图像边界，去掉多余的空白区域
#     plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
#     plt.show()
#
#     # 可视化 z 方向的向量场
#     plt.figure(figsize=(height / 50, width / 50))  # 调整显示尺寸与形变场尺寸一致
#     u = displacement_field[1, :, :, slice_idx]
#     v = displacement_field[2, :, :, slice_idx]
#     magnitude = np.sqrt(u ** 2 + v ** 2)
#     normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
#     colors = plt.cm.gray(normalized_magnitude.flatten())
#     plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
#     plt.gca().invert_yaxis()
#     plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
#     plt.axis('off')  # 不显示坐标轴
#
#     # 调整图像边界，去掉多余的空白区域
#     plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
#     plt.show()
#
#
# def main():
#     file_path = "./flowww.nii.gz"
#
#     # 加载形变场
#     displacement_field = load_displacement_field(file_path)
#
#     # 可视化单方向的形变场分量
#     visualize_single_component(displacement_field, direction=0, slice_idx=111)  # x方向
#     visualize_single_component(displacement_field, direction=1, slice_idx=111)  # y方向
#     visualize_single_component(displacement_field, direction=2, slice_idx=111)  # z方向
#
#     # 可视化三个方向的向量场
#     visualize_vector_field(displacement_field, slice_idx=111, step=4)
#
#
# if __name__ == "__main__":
#     main()


import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


def load_displacement_field(file_path):
    """
    加载形变场nii文件，并调整维度顺序
    :param file_path: 形变场文件路径
    :return: 调整后的形变场数据，形状为 (3, depth, height, width)
    """
    displacement_field = nib.load(file_path).get_fdata()  # 形状: (W, H, D, 3)
    print(f"Original displacement field shape: {displacement_field.shape}")

    # 调整通道位置: 从 (W, H, D, 3) 变为 (3, D, H, W)
    displacement_field = np.transpose(displacement_field, (3, 2, 1, 0))
    print(f"Reformatted displacement field shape: {displacement_field.shape}")

    return displacement_field


def visualize_single_component(displacement_field, direction=0, slice_idx=80, save_path="output.png"):
    """
    可视化某方向的形变场分量
    :param displacement_field: 形变场数据 (3, depth, height, width)
    :param direction: 方向索引 (0=x, 1=y, 2=z)
    :param slice_idx: 切片索引 (沿 depth 方向)
    :param save_path: 保存文件路径
    """
    slice_data = displacement_field[direction, slice_idx, :, :]
    plt.imshow(slice_data, cmap='gray')
    # plt.colorbar()
    plt.axis('off')  # 不显示坐标轴

    # 调整图像边界，去掉多余的空白区域
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=600)
    plt.close()  # 关闭图像，防止覆盖


def visualize_vector_field(displacement_field, slice_idx=80, step=10, save_prefix="output"):
    """
    可视化三个方向的向量场
    :param displacement_field: 形变场数据 (3, depth, height, width)
    :param slice_idx: 切片索引
    :param step: 采样步长，用于稀疏显示向量
    :param save_prefix: 文件名前缀
    """
    depth, height, width = displacement_field.shape[1], displacement_field.shape[2], displacement_field.shape[3]

    # 可视化 x 方向的向量场
    plt.figure(figsize=(width / 50, height / 50))  # 调整显示尺寸与形变场尺寸一致
    u = displacement_field[0, slice_idx, :, :]
    v = displacement_field[1, slice_idx, :, :]
    magnitude = np.sqrt(u ** 2 + v ** 2)
    normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
    colors = plt.cm.gray(normalized_magnitude.flatten())
    plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.5, color=colors)
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
    plt.axis('off')  # 不显示坐标轴

    # 调整图像边界，去掉多余的空白区域
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(f"{save_prefix}_x_{slice_idx}.png", bbox_inches='tight', pad_inches=0, dpi=600)
    plt.close()

    # 可视化 y 方向的向量场
    plt.figure(figsize=(width / 50, depth / 50))  # 调整显示尺寸与形变场尺寸一致
    u = displacement_field[0, :, slice_idx, :]
    v = displacement_field[2, :, slice_idx, :]
    magnitude = np.sqrt(u ** 2 + v ** 2)
    normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
    colors = plt.cm.gray(normalized_magnitude.flatten())
    plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
    plt.axis('off')  # 不显示坐标轴

    # 调整图像边界，去掉多余的空白区域
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(f"{save_prefix}_y_{slice_idx}.png", bbox_inches='tight', pad_inches=0, dpi=600)
    plt.close()

    # 可视化 z 方向的向量场
    plt.figure(figsize=(height / 50, width / 50))  # 调整显示尺寸与形变场尺寸一致
    u = displacement_field[1, :, :, slice_idx]
    v = displacement_field[2, :, :, slice_idx]
    magnitude = np.sqrt(u ** 2 + v ** 2)
    normalized_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
    colors = plt.cm.gray(normalized_magnitude.flatten())
    plt.quiver(u[::step, ::step], v[::step, ::step], angles='xy', scale_units='xy', scale=0.2, color=colors)
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal', adjustable='box')  # 保证显示的纵横比一致
    plt.axis('off')  # 不显示坐标轴

    # 调整图像边界，去掉多余的空白区域
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(f"{save_prefix}_z_{slice_idx}.png", bbox_inches='tight', pad_inches=0, dpi=600)
    plt.close()


def main():
    file_path = "./flowww.nii.gz"

    # 加载形变场
    displacement_field = load_displacement_field(file_path)

    # 可视化单方向的形变场分量并保存
    visualize_single_component(displacement_field, direction=0, slice_idx=111, save_path='./x_direction.png')  # x方向
    visualize_single_component(displacement_field, direction=1, slice_idx=111, save_path='./y_direction.png')  # y方向
    visualize_single_component(displacement_field, direction=2, slice_idx=111, save_path='./z_direction.png')  # z方向

    # 可视化三个方向的向量场并保存
    visualize_vector_field(displacement_field, slice_idx=111, step=4, save_prefix='./vector_field')


if __name__ == "__main__":
    main()

