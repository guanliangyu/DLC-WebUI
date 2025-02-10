# 功能说明 / Features

## 行为分析模块 / Behavior Analysis Modules

### 1. 小鼠游泳分析 / Mouse Swimming Analysis
- **功能描述 / Description**
  - 分析小鼠在游泳测试中的行为轨迹和活动情况
  - 生成运动轨迹图和详细的统计数据
- **主要功能 / Main Features**
  - 轨迹可视化 / Trajectory visualization
  - 移动距离统计 / Movement distance statistics
  - 分段数据分析（每5分钟） / Segmented data analysis (every 5 minutes)
- **技术参数 / Technical Parameters**
  - 视频要求：500x500像素，30fps，MP4格式
  - 置信度阈值：0.9
  - 速度过滤阈值：200单位/帧

### 2. 三箱实验分析 / Three-Chamber Test Analysis
- **功能描述 / Description**
  - 分析小鼠在三箱实验中的社交行为和空间偏好
  - 生成区域停留时间和移动轨迹的详细数据
- **主要功能 / Main Features**
  - 区域划分分析（上、中、下区域）
  - 停留时间统计
  - 移动距离计算
  - 轨迹可视化
- **技术参数 / Technical Parameters**
  - 视频要求：500x500像素，30fps，MP4格式
  - 置信度阈值：0.9
  - 区域边界：自动识别

### 3. 两鼠社交分析 / Two-Mouse Social Analysis
- **功能描述 / Description**
  - 分析两只小鼠之间的社交互动行为
  - 计算互动距离和行为模式
- **主要功能 / Main Features**
  - 双鼠轨迹追踪
  - 互动距离分析
  - 社交行为分类（近距离、中距离、远距离）
  - 时间序列分析
- **技术参数 / Technical Parameters**
  - 视频要求：500x500像素，30fps，MP4格式
  - 置信度阈值：0.9
  - 近距离阈值：15像素
  - 远距离阈值：35像素

### 4. 位置偏好分析 / CPP Analysis
- **功能描述 / Description**
  - 分析小鼠在条件化位置偏好实验中的行为
  - 计算区域偏好指数和活动模式
- **主要功能 / Main Features**
  - 区域偏好分析（左、中、右区域）
  - 停留时间统计
  - 移动轨迹热图
  - 偏好指数计算
- **技术参数 / Technical Parameters**
  - 视频要求：650x300像素，30fps，MP4格式
  - 置信度阈值：0.9
  - 区域划分：左(0-270)，中(270-370)，右(370-650)

## 通用功能 / Common Features

### 1. GPU管理 / GPU Management
- GPU状态监控 / GPU status monitoring
- 多GPU选择支持 / Multi-GPU selection support
- 显存占用预警 / Memory usage warning

### 2. 数据处理 / Data Processing
- 数据清洗和过滤 / Data cleaning and filtering
- 插值处理 / Interpolation processing
- 高斯平滑 / Gaussian smoothing
- 分段统计分析 / Segmented statistical analysis

### 3. 结果输出 / Output Results
- 轨迹图生成 / Trajectory plot generation
- CSV数据导出 / CSV data export
- 批量处理支持 / Batch processing support
- 多种下载选项 / Multiple download options

### 4. 用户界面 / User Interface
- 中英双语支持 / Bilingual support
- 实时处理进度显示 / Real-time progress display
- 错误提示和处理 / Error handling and notification
- 文件管理系统 / File management system 