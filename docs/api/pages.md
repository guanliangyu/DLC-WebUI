# 页面组件文档 / Page Components Documentation

## 主页面 / Main Pages

### 1. 游泳分析页面 / Swimming Analysis Page
- **文件**: `pages/3_Mouse_Swimming.py`
- **功能**: 分析小鼠游泳行为
- **组件**:
  - GPU状态显示
  - 模型选择器
  - 文件上传器
  - 分析控制面板
  - 结果处理器
  - 下载管理器

### 2. 三箱实验页面 / Three-Chamber Test Page
- **文件**: `pages/4_Three_Chamber.py`
- **功能**: 分析小鼠社交行为和空间偏好
- **组件**:
  - GPU配置面板
  - 视频选择器
  - 分析启动器
  - 数据处理器
  - 结果导出器

### 3. 两鼠社交页面 / Two-Mouse Social Page
- **文件**: `pages/5_Two_Social.py`
- **功能**: 分析两只小鼠的社交互动
- **组件**:
  - GPU管理器
  - 文件管理器
  - 分析控制器
  - 结果处理器
  - 数据导出器

### 4. 位置偏好页面 / CPP Page
- **文件**: `pages/6_Mouse_CPP.py`
- **功能**: 分析小鼠位置偏好行为
- **组件**:
  - GPU选择器
  - 文件上传器
  - 分析面板
  - 数据处理器
  - 结果下载器

## 共享组件 / Shared Components

### 1. 文件管理组件 / File Management Components
- **模块**: `src/ui/components/file_manager.py`
- **功能**:
  - 工作目录设置
  - 文件选择
  - 文件过滤
  - 路径管理

### 2. GPU管理组件 / GPU Management Components
- **模块**: `src/core/utils/gpu_utils.py`
- **功能**:
  - GPU状态监控
  - 显存占用检测
  - GPU选择界面
  - 多GPU管理

### 3. 分析控制组件 / Analysis Control Components
- **模块**: `src/core/helpers/analysis_helper.py`
- **功能**:
  - 分析任务创建
  - 进度监控
  - 日志管理
  - 错误处理

### 4. 结果处理组件 / Result Processing Components
- **模块**: `src/core/processing/`
- **功能**:
  - 数据清洗
  - 统计分析
  - 可视化生成
  - 结果导出

## 页面布局 / Page Layout

### 1. 标准布局 / Standard Layout
- **标题区**: 页面标题和说明
- **配置区**: GPU和模型设置
- **操作区**: 分析控制和处理
- **结果区**: 数据展示和下载

### 2. 标签页组织 / Tab Organization
- **视频分析**: 配置和执行分析
- **数据处理**: 处理分析结果
- **结果下载**: 导出和下载数据

## 交互功能 / Interactive Features

### 1. 用户提示 / User Prompts
- 错误提示
- 警告信息
- 成功反馈
- 操作指引

### 2. 进度显示 / Progress Display
- 分析进度条
- 处理状态指示
- 日志实时更新
- 任务完成通知

### 3. 数据展示 / Data Display
- 统计图表
- 数据表格
- 可视化结果
- 分析报告

## 多语言支持 / Multilingual Support

### 1. 界面语言 / Interface Language
- 中文界面元素
- 英文界面元素
- 双语标签
- 语言切换 