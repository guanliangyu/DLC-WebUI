# 工具函数文档 / Utility Functions Documentation

## GPU工具 / GPU Utilities

### 1. GPU状态监控 / GPU Status Monitoring

#### `display_gpu_usage()`
- **功能**: 显示当前GPU使用状态
- **返回值**: 
  - `bool`: 是否存在高显存占用

#### `setup_gpu_selection()`
- **功能**: 设置GPU选择界面
- **返回值**: 
  - `tuple`: (GPU数量, 选中的GPU列表)

## 文件管理 / File Management

### 1. 文件操作 / File Operations

#### `filter_and_zip_files(folder_path, excluded_ext=None, included_ext=None)`
- **功能**: 过滤并压缩指定文件夹中的文件
- **参数**:
  - `folder_path` (str): 文件夹路径
  - `excluded_ext` (list): 要排除的文件扩展名
  - `included_ext` (list): 要包含的文件扩展名

#### `setup_working_directory(root_directory)`
- **功能**: 设置工作目录并管理文件选择
- **参数**:
  - `root_directory` (str): 根目录路径
- **返回值**: 
  - `tuple`: (工作目录路径, 选中的文件列表)

## 分析辅助 / Analysis Helpers

### 1. 分析控制 / Analysis Control

#### `create_and_start_analysis(folder_path, selected_files, config_path, gpu_count, current_time, selected_gpus)`
- **功能**: 创建并启动分析任务
- **参数**:
  - `folder_path` (str): 工作目录路径
  - `selected_files` (list): 选中的文件列表
  - `config_path` (str): 配置文件路径
  - `gpu_count` (int): GPU数量
  - `current_time` (str): 当前时间
  - `selected_gpus` (list): 选中的GPU列表

#### `fetch_last_lines_of_logs(folder_path, gpu_count)`
- **功能**: 获取最新的日志内容
- **参数**:
  - `folder_path` (str): 工作目录路径
  - `gpu_count` (int): GPU数量
- **返回值**: 
  - `dict`: GPU编号对应的日志内容

## 配置管理 / Configuration Management

### 1. 路径配置 / Path Configuration

#### `get_root_path()`
- **功能**: 获取项目根目录路径
- **返回值**: 
  - `str`: 根目录路径

#### `get_data_path()`
- **功能**: 获取数据目录路径
- **返回值**: 
  - `str`: 数据目录路径

#### `get_models_path()`
- **功能**: 获取模型目录路径
- **返回值**: 
  - `str`: 模型目录路径

## 界面组件 / UI Components

### 1. 页面组件 / Page Components

#### `render_sidebar()`
- **功能**: 渲染侧边栏
- **说明**: 显示导航菜单和用户信息

#### `load_css_styles()`
- **功能**: 加载CSS样式
- **说明**: 设置页面样式和主题

## 数据处理工具 / Data Processing Tools

### 1. 数据转换 / Data Conversion

#### `convert_to_csv(data, output_path)`
- **功能**: 将数据转换为CSV格式
- **参数**:
  - `data` (DataFrame): 待转换的数据
  - `output_path` (str): 输出文件路径

### 2. 数据验证 / Data Validation

#### `validate_video_format(file_path)`
- **功能**: 验证视频格式是否符合要求
- **参数**:
  - `file_path` (str): 视频文件路径
- **返回值**: 
  - `bool`: 是否符合要求 