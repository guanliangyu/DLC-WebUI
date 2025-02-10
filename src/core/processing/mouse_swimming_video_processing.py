import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter

def process_mouse_swimming_video(file_path, folder_path, confidence_threshold=0.9):
    """处理单个小鼠游泳视频的分析结果
    Process single mouse swimming video analysis results
    
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
        data.loc[data[('Head', 'likelihood')] <= confidence_threshold, [('Head', 'x'), ('Head', 'y')]] = np.nan

        x = data[('Head', 'x')].astype(float)
        y = data[('Head', 'y')].astype(float)

        # 速度过滤和插值设置
        for i in range(1, total_frames):
            if not np.isnan(x[i-1]) and not np.isnan(x[i]) and not np.isnan(y[i-1]) and not np.isnan(y[i]):
                dx = x[i] - x[i-1]
                dy = y[i] - y[i-1]
                speed = np.sqrt(dx**2 + dy**2) * frame_rate
                if speed > 200:  # 速度阈值
                    x[i] = np.nan
                    y[i] = np.nan

        # 插值填充缺失值
        valid_indices = ~np.isnan(x)
        if np.any(valid_indices):
            interp_x = interp1d(np.flatnonzero(valid_indices), x[valid_indices], kind='linear', fill_value="extrapolate")
            interp_y = interp1d(np.flatnonzero(valid_indices), y[valid_indices], kind='linear', fill_value="extrapolate")
            x = interp_x(np.arange(total_frames))
            y = interp_y(np.arange(total_frames))

        # 应用高斯滤波平滑数据
        x_smoothed = gaussian_filter(x, sigma=2)
        y_smoothed = gaussian_filter(y, sigma=2)

        # 计算总移动距离
        total_distance = np.sum(np.sqrt(np.diff(x_smoothed)**2 + np.diff(y_smoothed)**2))

        # 计算每5分钟段的距离
        segment_length = 5 * 60 * frame_rate  # 5分钟的帧数
        num_segments = total_frames // segment_length
        segment_distances = {}
        
        for i in range(num_segments):
            start_frame = i * segment_length
            end_frame = start_frame + segment_length
            segment_distance = np.sum(np.sqrt(
                np.diff(x_smoothed[start_frame:end_frame])**2 + 
                np.diff(y_smoothed[start_frame:end_frame])**2
            ))
            segment_distances[f"{i*5}-{(i+1)*5}分钟 / minutes"] = segment_distance

        # 可视化：轨迹图
        plt.figure(figsize=(10, 10))
        plt.plot(x_smoothed, y_smoothed, 'b-', label='游泳轨迹 / Swimming Trajectory')
        plt.scatter(x_smoothed[0], y_smoothed[0], c='green', s=100, label='起点 / Start')
        plt.scatter(x_smoothed[-1], y_smoothed[-1], c='red', s=100, label='终点 / End')
        plt.title('小鼠游泳轨迹 / Mouse Swimming Trajectory')
        plt.xlabel('X 坐标 / X Position')
        plt.ylabel('Y 坐标 / Y Position')
        plt.legend()
        plt.axis('equal')
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        plt.grid(True)
        plt.savefig(plot_file_path)
        plt.close()

        # 保存分段距离数据
        pd.DataFrame.from_dict(
            segment_distances, 
            orient='index', 
            columns=['距离 / Distance']
        ).to_csv(segment_file_path)

        # 保存总体数据
        with open(total_file_path, 'w', encoding='utf-8') as f:
            f.write(f"视频总时长 / Total video duration: {total_frames / frame_rate} 秒/seconds\n")
            f.write(f"总移动距离 / Total distance moved: {total_distance} 单位/units\n")

        st.success(f"✅ 处理完成 / Processing completed: {os.path.basename(file_path)}")
        return plot_file_path, total_file_path, segment_file_path

    except Exception as e:
        st.error(f"处理文件失败 / Failed to process file: {str(e)}")
        return None

def process_swimming_files(folder_path, confidence_threshold=0.9, min_distance=15, max_distance=35):
    """处理文件夹中的所有游泳视频分析结果
    Process all swimming video analysis results in the folder
    
    Args:
        folder_path (str): 文件夹路径
        confidence_threshold (float): 置信度阈值
        min_distance (float): 最小移动距离
        max_distance (float): 最大移动距离
    """
    try:
        # 查找所有以"00000.csv"结尾的文件
        file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                     if f.endswith("00000.csv")]
        
        if not file_paths:
            st.warning("未找到分析结果文件 / No analysis result files found")
            return
            
        # 处理每个文件
        processed_files_list = []
        for file_path in file_paths:
            result = process_mouse_swimming_video(
                file_path, 
                folder_path, 
                confidence_threshold
            )
            if result:
                processed_files_list.append(result)
                
        # 显示处理结果
        if processed_files_list:
            st.success(f"✅ 成功处理 {len(processed_files_list)} 个文件 / Successfully processed {len(processed_files_list)} files")
            for result in processed_files_list:
                st.write(result)
        else:
            st.warning("没有成功处理的文件 / No files were successfully processed")
            
    except Exception as e:
        st.error(f"处理文件夹失败 / Failed to process folder: {str(e)}") 