import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter


def process_mouse_cpp_video(file_path, folder_path, confidence_threshold=0.9):
    """处理单个小鼠位置偏好视频的分析结果
    Process single mouse CPP video analysis results

    Args:
        file_path (str): CSV文件路径
        folder_path (str): 输出文件夹路径
        confidence_threshold (float): 置信度阈值
    """
    try:
        # 提取基础文件名并准备输出文件路径
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        plot_file_path = os.path.join(folder_path, f"{base_name}_trajectory.png")
        total_file_path = os.path.join(folder_path, f"{base_name}_total.csv")
        segment_file_path = os.path.join(folder_path, f"{base_name}_segments.csv")

        # 加载多级表头数据
        data = pd.read_csv(file_path, header=[1, 2])
        total_frames = len(data)
        frame_rate = 30  # 假设帧率为30 FPS

        # 数据清理：根据置信度过滤数据点
        data.loc[
            data[("bodypart1", "likelihood")] <= confidence_threshold,
            [("bodypart1", "x"), ("bodypart1", "y")],
        ] = np.nan

        x = data[("bodypart1", "x")].astype(float)
        y = data[("bodypart1", "y")].astype(float)

        # 速度过滤和插值设置
        for i in range(1, total_frames):
            if not np.isnan(x[i - 1]) and not np.isnan(x[i]) and not np.isnan(y[i - 1]) and not np.isnan(y[i]):
                dx = x[i] - x[i - 1]
                dy = y[i] - y[i - 1]
                speed = np.sqrt(dx**2 + dy**2) * frame_rate
                if speed > 200:  # 速度阈值
                    x[i] = np.nan
                    y[i] = np.nan

        # 插值填充缺失值
        valid_indices = ~np.isnan(x)
        if np.any(valid_indices):
            interp_x = interp1d(
                np.flatnonzero(valid_indices),
                x[valid_indices],
                kind="linear",
                fill_value="extrapolate",
            )
            interp_y = interp1d(
                np.flatnonzero(valid_indices),
                y[valid_indices],
                kind="linear",
                fill_value="extrapolate",
            )
            x = interp_x(np.arange(total_frames))
            y = interp_y(np.arange(total_frames))

        # 应用高斯滤波平滑数据
        x_smoothed = gaussian_filter(x, sigma=2)
        y_smoothed = gaussian_filter(y, sigma=2)

        # 定义区域边界
        x_boundaries = [270, 370]  # 左、中、右区域的边界

        # 计算每5分钟段的数据
        segment_length = 5 * 60 * frame_rate  # 5分钟的帧数
        num_segments = total_frames // segment_length
        segment_data = []

        for i in range(num_segments):
            start_frame = i * segment_length
            end_frame = start_frame + segment_length

            # 提取当前时间段的数据
            segment_x = x_smoothed[start_frame:end_frame]
            segment_y = y_smoothed[start_frame:end_frame]

            # 计算在各区域的时间（秒）
            time_left = np.sum(segment_x < x_boundaries[0]) / frame_rate
            time_middle = np.sum((segment_x >= x_boundaries[0]) & (segment_x < x_boundaries[1])) / frame_rate
            time_right = np.sum(segment_x >= x_boundaries[1]) / frame_rate

            # 计算在各区域的移动距离
            dx = np.diff(segment_x)
            dy = np.diff(segment_y)
            distances = np.sqrt(dx**2 + dy**2)

            dist_left = np.sum(distances[segment_x[:-1] < x_boundaries[0]])
            dist_middle = np.sum(distances[(segment_x[:-1] >= x_boundaries[0]) & (segment_x[:-1] < x_boundaries[1])])
            dist_right = np.sum(distances[segment_x[:-1] >= x_boundaries[1]])

            segment_data.append(
                {
                    "时间段 / Time Period": f"{i*5}-{(i+1)*5}分钟 / minutes",
                    "左区域时间 / Left Time (s)": time_left,
                    "中区域时间 / Middle Time (s)": time_middle,
                    "右区域时间 / Right Time (s)": time_right,
                    "左区域距离 / Left Distance": dist_left,
                    "中区域距离 / Middle Distance": dist_middle,
                    "右区域距离 / Right Distance": dist_right,
                }
            )

        # 可视化：轨迹图
        plt.figure(figsize=(15, 10))

        # 绘制轨迹
        plt.subplot(2, 1, 1)
        plt.plot(
            x_smoothed,
            y_smoothed,
            "b-",
            alpha=0.5,
            label="运动轨迹 / Movement Trajectory",
        )
        plt.axvline(x=x_boundaries[0], color="r", linestyle="--", label="左边界 / Left Boundary")
        plt.axvline(
            x=x_boundaries[1],
            color="g",
            linestyle="--",
            label="右边界 / Right Boundary",
        )
        plt.title("小鼠位置偏好轨迹 / Mouse CPP Trajectory")
        plt.xlabel("X 坐标 / X Position")
        plt.ylabel("Y 坐标 / Y Position")
        plt.legend()
        plt.grid(True)

        # 绘制热力图
        plt.subplot(2, 1, 2)
        plt.hist2d(x_smoothed, y_smoothed, bins=50, range=[[0, 650], [0, 300]], cmap="viridis")
        plt.colorbar(label="停留时间 / Dwell Time")
        plt.axvline(x=x_boundaries[0], color="r", linestyle="--")
        plt.axvline(x=x_boundaries[1], color="g", linestyle="--")
        plt.title("位置热力图 / Position Heatmap")
        plt.xlabel("X 坐标 / X Position")
        plt.ylabel("Y 坐标 / Y Position")

        plt.tight_layout()
        plt.savefig(plot_file_path)
        plt.close()

        # 保存分段数据
        pd.DataFrame(segment_data).to_csv(segment_file_path, index=False)

        # 计算并保存总体数据
        total_data = {
            "总时长 / Total Duration (s)": total_frames / frame_rate,
            "左区域总时间 / Total Left Time (s)": np.sum(x_smoothed < x_boundaries[0]) / frame_rate,
            "中区域总时间 / Total Middle Time (s)": np.sum((x_smoothed >= x_boundaries[0]) & (x_smoothed < x_boundaries[1]))
            / frame_rate,
            "右区域总时间 / Total Right Time (s)": np.sum(x_smoothed >= x_boundaries[1]) / frame_rate,
            "左区域偏好指数 / Left Preference Index": (np.sum(x_smoothed < x_boundaries[0]) / total_frames) * 100,
            "中区域偏好指数 / Middle Preference Index": (
                np.sum((x_smoothed >= x_boundaries[0]) & (x_smoothed < x_boundaries[1])) / total_frames
            )
            * 100,
            "右区域偏好指数 / Right Preference Index": (np.sum(x_smoothed >= x_boundaries[1]) / total_frames) * 100,
        }
        pd.DataFrame([total_data]).to_csv(total_file_path, index=False)

        st.success(f"✅ 处理完成 / Processing completed: {os.path.basename(file_path)}")
        return plot_file_path, total_file_path, segment_file_path

    except Exception as e:
        st.error(f"处理文件失败 / Failed to process file: {str(e)}")
        return None


def process_cpp_files(folder_path, confidence_threshold=0.9):
    """处理文件夹中的所有位置偏好视频分析结果
    Process all CPP video analysis results in the folder

    Args:
        folder_path (str): 文件夹路径
        confidence_threshold (float): 置信度阈值
    """
    try:
        # 查找所有以"00000.csv"结尾的文件
        file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith("00000.csv")]

        if not file_paths:
            st.warning("未找到分析结果文件 / No analysis result files found")
            return

        # 处理每个文件
        processed_files_list = []
        for file_path in file_paths:
            result = process_mouse_cpp_video(file_path, folder_path, confidence_threshold)
            if result:
                processed_files_list.append(result)

        # 显示处理结果
        if processed_files_list:
            st.success(f"✅ 成功处理 {len(processed_files_list)} 个文件 / " f"Successfully processed {len(processed_files_list)} files")
            for result in processed_files_list:
                st.write(result)
        else:
            st.warning("没有成功处理的文件 / No files were successfully processed")

    except Exception as e:
        st.error(f"处理文件夹失败 / Failed to process folder: {str(e)}")
