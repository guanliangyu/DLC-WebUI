# 核心API文档 / Core API Documentation

## 视频处理模块 / Video Processing Modules

### 1. 游泳行为分析 / Swimming Behavior Analysis

#### `process_mouse_swimming_video(file_path, folder_path, confidence_threshold=0.9)`
- **功能**: 处理单个小鼠游泳视频的分析结果
- **参数**:
  - `file_path` (str): CSV文件路径
  - `folder_path` (str): 输出文件夹路径
  - `confidence_threshold` (float): 置信度阈值
- **返回值**: 
  - `tuple`: (轨迹图路径, 总体数据路径, 分段数据路径)

#### `process_swimming_files(folder_path, confidence_threshold=0.9, min_distance=15, max_distance=35)`
- **功能**: 处理文件夹中的所有游泳视频分析结果
- **参数**:
  - `folder_path` (str): 文件夹路径
  - `confidence_threshold` (float): 置信度阈值
  - `min_distance` (float): 最小移动距离
  - `max_distance` (float): 最大移动距离

### 2. 三箱实验分析 / Three-Chamber Test Analysis

#### `process_mouse_tc_video(file_path, folder_path, confidence_threshold=0.9)`
- **功能**: 处理单个小鼠三箱实验视频的分析结果
- **参数**:
  - `file_path` (str): CSV文件路径
  - `folder_path` (str): 输出文件夹路径
  - `confidence_threshold` (float): 置信度阈值
- **返回值**: 
  - `tuple`: (轨迹图路径, 总体数据路径, 分段数据路径)

#### `process_tc_files(folder_path, confidence_threshold=0.9)`
- **功能**: 处理文件夹中的所有三箱实验视频分析结果
- **参数**:
  - `folder_path` (str): 文件夹路径
  - `confidence_threshold` (float): 置信度阈值

### 3. 社交行为分析 / Social Behavior Analysis

#### `process_mouse_social_video(file_path, folder_path, confidence_threshold=0.9, close_distance=15, far_distance=35)`
- **功能**: 处理单个两鼠社交实验视频的分析结果
- **参数**:
  - `file_path` (str): CSV文件路径
  - `folder_path` (str): 输出文件夹路径
  - `confidence_threshold` (float): 置信度阈值
  - `close_distance` (float): 近距离阈值
  - `far_distance` (float): 远距离阈值
- **返回值**: 
  - `tuple`: (轨迹图路径, 总体数据路径, 分段数据路径, 距离数据路径)

#### `process_social_files(folder_path, confidence_threshold=0.9, close_distance=15, far_distance=35)`
- **功能**: 处理文件夹中的所有社交实验视频分析结果
- **参数**:
  - `folder_path` (str): 文件夹路径
  - `confidence_threshold` (float): 置信度阈值
  - `close_distance` (float): 近距离阈值
  - `far_distance` (float): 远距离阈值

### 4. 位置偏好分析 / CPP Analysis

#### `process_mouse_cpp_video(file_path, folder_path, confidence_threshold=0.9)`
- **功能**: 处理单个小鼠位置偏好视频的分析结果
- **参数**:
  - `file_path` (str): CSV文件路径
  - `folder_path` (str): 输出文件夹路径
  - `confidence_threshold` (float): 置信度阈值
- **返回值**: 
  - `tuple`: (轨迹图路径, 总体数据路径, 分段数据路径)

#### `process_cpp_files(folder_path, confidence_threshold=0.9)`
- **功能**: 处理文件夹中的所有位置偏好视频分析结果
- **参数**:
  - `folder_path` (str): 文件夹路径
  - `confidence_threshold` (float): 置信度阈值

## 数据处理功能 / Data Processing Functions

### 1. 数据清洗 / Data Cleaning
- 置信度过滤
- 速度阈值过滤
- 异常值处理

### 2. 数据平滑 / Data Smoothing
- 高斯滤波
- 插值处理
- 轨迹优化

### 3. 统计分析 / Statistical Analysis
- 时间分段统计
- 区域偏好计算
- 行为模式分类

### 4. 可视化 / Visualization
- 轨迹图生成
- 热力图绘制
- 时间序列图表 