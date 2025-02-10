import os
import pandas as pd
import numpy as np
import streamlit as st
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter

def process_mouse_grooming_video(file_path, folder_path, paw_probability_threshold=0.8):
    """处理单个小鼠理毛视频的分析结果
    Process single mouse grooming video analysis results
    
    Args:
        file_path (str): CSV文件路径
        folder_path (str): 输出文件夹路径
        paw_probability_threshold (float): 置信度阈值
    """
    try:
        # 提取基础文件名并准备输出文件路径
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        scalar_output_file_path = os.path.join(folder_path, f"{base_name}_Scalar.csv")
        
        # 加载多级表头数据
        data = pd.read_csv(file_path, header=[1, 2])
        
        total_frames = len(data)
        frame_rate = 30  # 假设帧率为30 FPS
        
        # 每帧的时间（秒）
        time_seconds = np.arange(total_frames) / frame_rate
        
        # 计算位移向量和标量积的函数（不带平滑）
        def calculate_displacement_and_scalar_product(data, ear):
            # 根据置信度过滤数据
            data.loc[data[(ear, 'likelihood')] <= paw_probability_threshold, [(ear, 'x'), (ear, 'y')]] = np.nan
            
            x = data[(ear, 'x')].astype(float)
            y = data[(ear, 'y')].astype(float)
            
            frames = np.arange(total_frames)
            interp_x = interp1d(frames[~x.isna()], x.dropna(), kind='linear', bounds_error=False, fill_value="extrapolate")
            interp_y = interp1d(frames[~y.isna()], y.dropna(), kind='linear', bounds_error=False, fill_value="extrapolate")
            x_interpolated = interp_x(frames)
            y_interpolated = interp_y(frames)
            
            dx = np.diff(x_interpolated, prepend=x_interpolated[0])
            dy = np.diff(y_interpolated, prepend=y_interpolated[0])
            
            displacement_vectors = np.stack([dx, dy], axis=1)
            scalar_products = [np.dot(displacement_vectors[i], displacement_vectors[i-1]) if i > 0 else 0 for i in range(total_frames)]
            
            return displacement_vectors, scalar_products
        
        # 计算左右耳的位移和标量积
        left_ear_displacement, left_ear_scalar_products = calculate_displacement_and_scalar_product(data, 'Leftear')
        right_ear_displacement, right_ear_scalar_products = calculate_displacement_and_scalar_product(data, 'Rightear')
        
        # 将时间、位移向量和标量积组合成DataFrame
        scalar_data_with_time = pd.DataFrame({
            'Time (s)': time_seconds,
            'LeftEarDisplacementX': left_ear_displacement[:, 0],
            'LeftEarDisplacementY': left_ear_displacement[:, 1],
            'LeftEarScalarProduct': left_ear_scalar_products,
            'RightEarDisplacementX': right_ear_displacement[:, 0],
            'RightEarDisplacementY': right_ear_displacement[:, 1],
            'RightEarScalarProduct': right_ear_scalar_products
        })
        
        # 保存组合数据到CSV文件
        scalar_data_with_time.to_csv(scalar_output_file_path, index=False)
        
        # 将时间从秒转换为分钟以便分析
        scalar_data_with_time['Time (min)'] = scalar_data_with_time['Time (s)'] / 60.0
        
        def analyze_intervals(output_base_name, interval_minutes, apply_filter=False):
            """分析特定时间间隔内的行为
            Analyze behavior in specific time intervals"""
            def count_frames_in_range(interval_minutes, range_min, range_max):
                max_time = scalar_data_with_time['Time (min)'].max()
                interval_counts = []
                for start_min in np.arange(0, max_time, interval_minutes):
                    end_min = start_min + interval_minutes
                    interval_data = scalar_data_with_time[
                        (scalar_data_with_time['Time (min)'] >= start_min) & 
                        (scalar_data_with_time['Time (min)'] < end_min)
                    ]
                    left_count = interval_data[
                        (interval_data['LeftEarScalarProduct'] >= range_min) & 
                        (interval_data['LeftEarScalarProduct'] <= range_max)
                    ].shape[0]
                    right_count = interval_data[
                        (interval_data['RightEarScalarProduct'] >= range_min) & 
                        (interval_data['RightEarScalarProduct'] <= range_max)
                    ].shape[0]
                    total_count = left_count + right_count
                    
                    # 应用过滤器：将小于15的计数设为0
                    if apply_filter and total_count < 15:
                        left_count, right_count, total_count = 0, 0, 0
                    
                    interval_counts.append([start_min, end_min, left_count, right_count, total_count])
                return pd.DataFrame(
                    interval_counts, 
                    columns=['Start Min', 'End Min', 'LeftEar Count', 'RightEar Count', 'Total Count']
                )
            
            counts = count_frames_in_range(interval_minutes, -50, -10)
            output_path_suffix = f"_{interval_minutes*10}min"
            if apply_filter:
                output_path_suffix += "-filter"
            output_path = os.path.join(folder_path, f"{output_base_name}{output_path_suffix}.csv")
            counts.to_csv(output_path, index=False)
            return counts
        
        # 执行0.1分钟间隔的分析
        _0_1min_counts = analyze_intervals(base_name, 0.1)
        
        # 执行带过滤的0.1分钟间隔分析
        _0_1min_filtered_counts = analyze_intervals(base_name, 0.1, apply_filter=True)
        
        # 将过滤后的0.1分钟间隔计数聚合成5分钟间隔
        def aggregate_into_5min_intervals(filtered_counts):
            filtered_counts['5Min Interval'] = (filtered_counts['Start Min'] // 5).astype(int)
            aggregated_counts = filtered_counts.groupby('5Min Interval')['Total Count'].sum().reset_index()
            aggregated_counts['Start Min'] = aggregated_counts['5Min Interval'] * 5
            aggregated_counts['End Min'] = (aggregated_counts['5Min Interval'] + 1) * 5
            return aggregated_counts[['Start Min', 'End Min', 'Total Count']]
        
        _5min_aggregated_counts = aggregate_into_5min_intervals(_0_1min_filtered_counts)
        _5min_aggregated_output_path = os.path.join(folder_path, f"{base_name}_5min_aggregated.csv")
        _5min_aggregated_counts.to_csv(_5min_aggregated_output_path, index=False)
        
        # 计算计数非零的总有效时间
        total_effective_time = _0_1min_filtered_counts[_0_1min_filtered_counts['Total Count'] > 0]['End Min'].sum() - \
                             _0_1min_filtered_counts[_0_1min_filtered_counts['Total Count'] > 0]['Start Min'].sum()
        
        # 保存总有效时间到CSV文件
        total_time_output_path = os.path.join(folder_path, f"{base_name}_total_effective_time.csv")
        with open(total_time_output_path, 'w') as f:
            f.write(f"Total Effective Time (min): {total_effective_time}")
        
        st.success(f"✅ 处理完成 / Processing completed: {os.path.basename(file_path)}")
        return scalar_output_file_path, _5min_aggregated_output_path
        
    except Exception as e:
        st.error(f"处理文件失败 / Failed to process file: {str(e)}")
        return None

def process_grooming_files(folder_path, paw_probability_threshold=0.8, min_distance=10, max_distance=25):
    """处理文件夹中的所有理毛视频分析结果
    Process all grooming video analysis results in the folder
    
    Args:
        folder_path (str): 文件夹路径
        paw_probability_threshold (float): 置信度阈值
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
            result = process_mouse_grooming_video(
                file_path, 
                folder_path, 
                paw_probability_threshold
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