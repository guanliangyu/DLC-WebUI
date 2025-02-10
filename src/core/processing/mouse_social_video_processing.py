import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter
from scipy.spatial.distance import pdist, squareform

def process_mouse_social_video(file_path, folder_path, confidence_threshold=0.9, close_distance=15, far_distance=35):
    """处理单个两鼠社交实验视频的分析结果
    Process single two-mouse social test video analysis results
    
    Args:
        file_path (str): CSV文件路径
        folder_path (str): 输出文件夹路径
        confidence_threshold (float): 置信度阈值
        close_distance (float): 定义近距离接触的阈值（像素）
        far_distance (float): 定义远距离的阈值（像素）
    """
    try:
        # 提取基础文件名并准备输出文件路径
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        plot_file_path = os.path.join(folder_path, f"{base_name}_trajectory.png")
        total_file_path = os.path.join(folder_path, f"{base_name}_total.csv")
        segment_file_path = os.path.join(folder_path, f"{base_name}_segments.csv")
        distance_file_path = os.path.join(folder_path, f"{base_name}_distances.csv")

        # 加载多级表头数据
        data = pd.read_csv(file_path, header=[1, 2])
        total_frames = len(data)
        frame_rate = 30  # 假设帧率为30 FPS

        # 定义关键点
        body_parts = ['nose', 'left_ear', 'right_ear', 'neck', 'body_center', 'tail_base']
        mice = ['mouse1', 'mouse2']

        # 数据清理和预处理
        for mouse in mice:
            for part in body_parts:
                # 根据置信度过滤数据点
                likelihood = data[(mouse, f'{part}_likelihood')]
                mask = likelihood < confidence_threshold
                data.loc[mask, [(mouse, f'{part}_x'), (mouse, f'{part}_y')]] = np.nan

                # 对每个坐标进行插值和平滑处理
                for coord in ['x', 'y']:
                    col = data[(mouse, f'{part}_{coord}')]
                    valid = ~col.isna()
                    if valid.any():
                        # 插值
                        interp = interp1d(np.flatnonzero(valid), col[valid], 
                                        kind='linear', fill_value='extrapolate')
                        smoothed = gaussian_filter(interp(np.arange(len(col))), sigma=2)
                        data.loc[:, (mouse, f'{part}_{coord}')] = smoothed

        # 计算两只小鼠之间的距离
        distances = {}
        for part1 in body_parts:
            for part2 in body_parts:
                x1, y1 = data[('mouse1', f'{part1}_x')], data[('mouse1', f'{part1}_y')]
                x2, y2 = data[('mouse2', f'{part2}_x')], data[('mouse2', f'{part2}_y')]
                dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                distances[f'{part1}-{part2}'] = dist

        # 保存距离数据
        pd.DataFrame(distances).to_csv(distance_file_path, index=False)

        # 分析社交互动
        nose_dist = distances['nose-nose']
        body_dist = distances['body_center-body_center']

        # 计算每5分钟段的统计数据
        segment_length = 5 * 60 * frame_rate  # 5分钟的帧数
        num_segments = total_frames // segment_length
        segment_data = []

        for i in range(num_segments):
            start_frame = i * segment_length
            end_frame = start_frame + segment_length
            
            # 提取当前时间段的数据
            segment_nose_dist = nose_dist[start_frame:end_frame]
            segment_body_dist = body_dist[start_frame:end_frame]
            
            # 计算各种互动指标
            close_interaction = np.sum(segment_nose_dist < close_distance) / frame_rate
            medium_interaction = np.sum((segment_nose_dist >= close_distance) & 
                                     (segment_nose_dist < far_distance)) / frame_rate
            far_interaction = np.sum(segment_nose_dist >= far_distance) / frame_rate
            
            # 计算平均距离和标准差
            avg_nose_dist = np.nanmean(segment_nose_dist)
            std_nose_dist = np.nanstd(segment_nose_dist)
            avg_body_dist = np.nanmean(segment_body_dist)
            std_body_dist = np.nanstd(segment_body_dist)
            
            segment_data.append({
                '时间段 / Time Period': f"{i*5}-{(i+1)*5}分钟 / minutes",
                '近距离互动时间 / Close Interaction Time (s)': close_interaction,
                '中等距离时间 / Medium Distance Time (s)': medium_interaction,
                '远距离时间 / Far Distance Time (s)': far_interaction,
                '平均鼻部距离 / Average Nose Distance': avg_nose_dist,
                '鼻部距离标准差 / Nose Distance Std': std_nose_dist,
                '平均身体距离 / Average Body Distance': avg_body_dist,
                '身体距离标准差 / Body Distance Std': std_body_dist
            })

        # 保存分段数据
        pd.DataFrame(segment_data).to_csv(segment_file_path, index=False)

        # 计算总体统计数据
        total_data = {
            '总时长 / Total Duration (s)': total_frames / frame_rate,
            '总近距离互动时间 / Total Close Interaction Time (s)': np.sum(nose_dist < close_distance) / frame_rate,
            '总中等距离时间 / Total Medium Distance Time (s)': np.sum((nose_dist >= close_distance) & 
                                                                  (nose_dist < far_distance)) / frame_rate,
            '总远距离时间 / Total Far Distance Time (s)': np.sum(nose_dist >= far_distance) / frame_rate,
            '平均鼻部距离 / Average Nose Distance': np.nanmean(nose_dist),
            '鼻部距离标准差 / Nose Distance Std': np.nanstd(nose_dist),
            '平均身体距离 / Average Body Distance': np.nanmean(body_dist),
            '身体距离标准差 / Body Distance Std': np.nanstd(body_dist)
        }
        pd.DataFrame([total_data]).to_csv(total_file_path, index=False)

        # 绘制轨迹图
        plt.figure(figsize=(15, 10))
        
        # 绘制两只小鼠的轨迹
        plt.subplot(2, 1, 1)
        plt.plot(data[('mouse1', 'body_center_x')], data[('mouse1', 'body_center_y')], 
                'b-', alpha=0.5, label='Mouse 1')
        plt.plot(data[('mouse2', 'body_center_x')], data[('mouse2', 'body_center_y')], 
                'r-', alpha=0.5, label='Mouse 2')
        plt.title('小鼠运动轨迹 / Mouse Movement Trajectories')
        plt.xlabel('X 坐标 / X Position')
        plt.ylabel('Y 坐标 / Y Position')
        plt.legend()
        plt.grid(True)

        # 绘制距离变化图
        plt.subplot(2, 1, 2)
        time_axis = np.arange(len(nose_dist)) / frame_rate / 60  # 转换为分钟
        plt.plot(time_axis, nose_dist, 'g-', label='鼻部距离 / Nose Distance')
        plt.plot(time_axis, body_dist, 'b-', label='身体距离 / Body Distance')
        plt.axhline(y=close_distance, color='r', linestyle='--', label='近距离阈值 / Close Distance Threshold')
        plt.axhline(y=far_distance, color='y', linestyle='--', label='远距离阈值 / Far Distance Threshold')
        plt.title('小鼠间距离变化 / Inter-mouse Distance Over Time')
        plt.xlabel('时间（分钟）/ Time (minutes)')
        plt.ylabel('距离（像素）/ Distance (pixels)')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.savefig(plot_file_path)
        plt.close()

        st.success(f"✅ 处理完成 / Processing completed: {os.path.basename(file_path)}")
        return plot_file_path, total_file_path, segment_file_path, distance_file_path

    except Exception as e:
        st.error(f"处理文件失败 / Failed to process file: {str(e)}")
        return None

def process_social_files(folder_path, confidence_threshold=0.9, close_distance=15, far_distance=35):
    """处理文件夹中的所有两鼠社交实验视频分析结果
    Process all two-mouse social test video analysis results in the folder
    
    Args:
        folder_path (str): 文件夹路径
        confidence_threshold (float): 置信度阈值
        close_distance (float): 定义近距离接触的阈值（像素）
        far_distance (float): 定义远距离的阈值（像素）
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
            result = process_mouse_social_video(
                file_path, 
                folder_path, 
                confidence_threshold,
                close_distance,
                far_distance
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