import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


def load_displacement_field(file_path):
    """
    加载形变场nii文件
    :param file_path: 形变场文件路径
    :return: 形变场数据，形状为 (3, depth, height, width)
    """
    displacement_field = nib.load(file_path).get_fdata()
    print(f"Displacement field shape: {displacement_field.shape}")
    return displacement_field


def visualize_single_component(displacement_field, direction=0, slice_idx=80):
    """
    可视化某方向的形变场分量
    :param displacement_field: 形变场数据
    :param direction: 方向索引 (0=x, 1=y, 2=z)
    :param slice_idx: 切片索引
    """
    slice_data = displacement_field[direction, slice_idx, :, :]
    plt.imshow(slice_data, cmap='jet')
    plt.colorbar()
    plt.title(f"Displacement field (direction={direction}, slice={slice_idx})")
    plt.show()


def visualize_vector_field(displacement_field, slice_idx=80, step=10):
    """
    可视化向量场
    :param displacement_field: 形变场数据
    :param slice_idx: 切片索引
    :param step: 采样步长，用于稀疏显示向量
    """
    # 获取形变场的大小
    height, width = displacement_field.shape[2], displacement_field.shape[3]

    # 确保生成的索引不超出范围
    x, y = np.meshgrid(
        np.arange(0, width, step),  # x 方向的索引
        np.arange(0, height, step)  # y 方向的索引
    )

    # 获取 x 和 y 的位移量
    u = displacement_field[0, slice_idx, y, x]
    v = displacement_field[1, slice_idx, y, x]

    plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1)
    plt.title(f"Vector field (slice {slice_idx})")
    plt.gca().invert_yaxis()  # 确保方向与医学图像一致
    plt.show()



def main():
    # 设置形变场文件路径
    file_path = "./flow.nii.gz"

    # 加载形变场
    displacement_field = load_displacement_field(file_path)

    # 可视化单方向的形变场分量
    visualize_single_component(displacement_field, direction=0, slice_idx=80)  # x方向
    visualize_single_component(displacement_field, direction=1, slice_idx=80)  # y方向
    visualize_single_component(displacement_field, direction=2, slice_idx=80)  # z方向

    # 可视化向量场
    visualize_vector_field(displacement_field, slice_idx=80, step=3)


if __name__ == "__main__":
    main()
