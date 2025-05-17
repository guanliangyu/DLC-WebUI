# 快速开始 / Quick Start

## 1. 系统要求 / System Requirements
- NVIDIA GPU (建议8GB以上显存)
- Windows 10/11 或 Linux
- Python 3.8
- CUDA 11.8 (通过 Conda 安装 / Installed via Conda)

## 2. 启动应用 / Launch Application
确保您已按照 [安装指南](installation.md) 完成环境配置并激活 `dlc-webui-env` 环境。
Ensure you have completed the environment setup according to the [Installation Guide](installation.md) and activated the `dlc-webui-env` environment.

```bash
# 启动应用 / Launch application
streamlit run Home.py
```

## 3. 基本使用流程 / Basic Usage Flow

### 3.1 选择分析模块 / Select Analysis Module
- 从侧边栏选择需要的行为分析模块：
  - 游泳分析 / Swimming Analysis
  - 三箱实验 / Three-Chamber Test
  - 两鼠社交 / Two Social
  - 位置偏好 / CPP

### 3.2 准备数据 / Prepare Data
1. 确保视频符合要求：
   - 正确的分辨率和帧率
   - MP4格式
   - 合适的拍摄角度
2. 选择工作目录
3. 上传视频文件

### 3.3 配置分析参数 / Configure Analysis
1. 选择GPU设备
2. 选择适当的分析模型
3. 检查GPU状态

### 3.4 执行分析 / Run Analysis
1. 点击"开始GPU分析"按钮
2. 等待分析完成
3. 查看分析日志

### 3.5 处理结果 / Process Results
1. 切换到"数据处理"标签
2. 点击"处理分析结果"按钮
3. 等待处理完成

### 3.6 下载结果 / Download Results
1. 切换到"结果下载"标签
2. 选择下载选项：
   - 下载所有文件
   - 下载除视频外的文件
   - 仅下载CSV文件

## 4. 注意事项 / Notes
- 确保GPU显存充足
- 定期查看分析进度
- 保持网络连接稳定
- 遵循视频要求规范

## 5. 常见问题处理 / Troubleshooting
- GPU显存不足：关闭其他程序或减少批处理数量
- 分析失败：检查视频格式和完整性
- 处理超时：耐心等待或刷新页面
- 下载失败：检查网络连接和磁盘空间 