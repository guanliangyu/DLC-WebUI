# DLC-WebUI

基于DeepLabCut的小鼠行为分析Web界面 / Web Interface for Mouse Behavior Analysis Based on DeepLabCut

## 功能特点 / Features

- 🐭 多种行为分析模式 / Multiple Analysis Modes
  - 游泳行为分析 / Swimming Analysis
  - 三箱实验分析 / Three-Chamber Test
  - 两鼠社交分析 / Two-Mouse Social Analysis
  - 位置偏好分析 / CPP Analysis

- 🖥️ 友好的用户界面 / User-Friendly Interface
  - 中英双语支持 / Bilingual Support
  - 实时进度显示 / Real-time Progress Display
  - 可视化结果展示 / Visualization Results
  - 批量处理支持 / Batch Processing Support

- 🚀 高性能计算 / High-Performance Computing
  - 多GPU支持 / Multi-GPU Support
  - 并行处理 / Parallel Processing
  - 智能资源管理 / Smart Resource Management

## 系统要求 / System Requirements

- NVIDIA GPU (建议8GB以上显存 / 8GB+ VRAM recommended)
- Windows 10/11 或 Linux
- Python 3.8
- CUDA 11.8 (通过 Conda 安装 / Installed via Conda)
- 8GB+ 系统内存 / System Memory
- 50GB+ 可用硬盘空间 / Available Disk Space

## 快速开始 / Quick Start

### 1. 安装 / Installation

**推荐方法: 使用 environment.yml (Recommended: Using environment.yml)**
```bash
# 克隆仓库 / Clone repository
git clone https://github.com/guanliangyu/DLC-WebUI.git
cd DLC-WebUI

# 使用 environment.yml 创建并激活 Conda 环境
# Create and activate Conda environment using environment.yml
conda env create -f environment.yml
conda activate dlc-webui-env
```

**备选方法: 手动设置 (Alternative: Manual Setup)**
```bash
# 克隆仓库 / Clone repository
git clone https://github.com/guanliangyu/DLC-WebUI.git
cd DLC-WebUI

# 创建并激活 Conda 环境 / Create and activate Conda environment
conda create -n dlc-webui-env python=3.8 -y
conda activate dlc-webui-env

# 安装 CUDA Toolkit / Install CUDA Toolkit
# (请根据您的系统和偏好选择合适的频道，conda-forge 通常是一个好的选择)
# (Choose the appropriate channel for your system, conda-forge is often a good choice)
conda install cudatoolkit=11.8 -c conda-forge -y 

# 安装其余依赖 / Install remaining dependencies
pip install -r requirements.txt
```

### 2. 启动应用 / Launch Application

```bash
# 启动Web界面 / Start web interface
streamlit run Home.py
```

### 3. 使用流程 / Usage Flow

1. 选择分析模式 / Select analysis mode
2. 上传视频文件 / Upload video files
3. 配置分析参数 / Configure parameters
4. 执行分析任务 / Run analysis
5. 查看和下载结果 / View and download results

## 文档 / Documentation

详细文档请参见 [docs](docs/README.md) 目录：
- [快速开始指南](docs/guides/quickstart.md)
- [功能说明](docs/guides/features.md)
- [常见问题](docs/guides/faq.md)
- [API文档](docs/api/core.md)

## 贡献 / Contributing

欢迎贡献代码和提出建议！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 许可证 / License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系我们 / Contact Us

- 问题反馈 / Issues: [GitHub Issues](https://github.com/guanliangyu/DLC-WebUI/issues)
- 邮件咨询 / Email: liangyu.guan@outlook.com
