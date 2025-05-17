# 安装指南 / Installation Guide

## 系统要求 / System Requirements

### 硬件要求 / Hardware Requirements
- CPU: 4核或以上 / 4 cores or more
- 内存: 16GB或以上 / 16GB RAM or more
- GPU: NVIDIA GPU with 8GB或以上显存 / NVIDIA GPU with 8GB VRAM or more
- 硬盘空间: 50GB或以上 / 50GB disk space or more

### 软件要求 / Software Requirements
- 操作系统 / Operating System:
  - Windows 10/11
  - Ubuntu 20.04/22.04
  - macOS 12或以上 / macOS 12 or later
- Python 3.8
- CUDA 11.8 (通过 Conda 安装 / Installed via Conda)
- cuDNN (通常随 Conda cudatoolkit 一并安装 / Usually installed with Conda cudatoolkit)

## 安装步骤 / Installation Steps

### 1. 克隆项目 / Clone Project
```bash
git clone https://github.com/guanliangyu/DLC-WebUI.git
cd DLC-WebUI
```

### 2. 安装环境和依赖 / Install Environment and Dependencies

**推荐方法: 使用 environment.yml (Recommended: Using environment.yml)**
```bash
# 使用 environment.yml 创建并激活 Conda 环境
# Create and activate Conda environment using environment.yml
conda env create -f environment.yml
conda activate dlc-webui-env
```

**备选方法: 手动设置 (Alternative: Manual Setup)**

**2.1. 安装Python环境 / Install Python Environment**
```bash
# 使用conda创建环境 / Create environment with conda
conda create -n dlc-webui-env python=3.8 -y
conda activate dlc-webui-env
```

**2.2. 安装CUDA和cuDNN / Install CUDA and cuDNN**
```bash
# 通过 Conda 安装 CUDA Toolkit (通常包含 cuDNN)
# Install CUDA Toolkit via Conda (usually includes cuDNN)
# (请根据您的系统和偏好选择合适的频道，conda-forge 通常是一个好的选择)
# (Choose the appropriate channel for your system, conda-forge is often a good choice)
conda install cudatoolkit=11.8 -c conda-forge -y
```

**2.3. 安装其余依赖 / Install Remaining Dependencies**
```bash
# 使用pip安装依赖 / Install dependencies with pip
pip install -r requirements.txt
```

### 3. 配置设置 / Configure Settings
# (此项目当前版本不需要额外的配置文件 / This project version does not currently require additional configuration files)

## 验证安装 / Verify Installation

### 1. 运行测试 / Run Tests
```bash
pytest tests/
```

### 2. 启动应用 / Start Application
```bash
# 在已激活的 dlc-webui-env 环境下运行 / Run in the activated dlc-webui-env environment
streamlit run Home.py
```

### 3. 访问Web界面 / Access Web Interface
- 打开浏览器访问 / Open browser and visit: http://localhost:8501

## 常见问题 / Common Issues

### 1. CUDA相关问题 / CUDA Related Issues
- 确保CUDA版本与PyTorch兼容 / Ensure CUDA version is compatible with PyTorch
- 检查环境变量设置 / Check environment variables

### 2. 依赖安装问题 / Dependency Installation Issues
- 使用清华镜像源加速下载 / Use Tsinghua mirror for faster download
- 检查Python版本兼容性 / Check Python version compatibility

### 3. 运行时错误 / Runtime Errors
- 检查GPU驱动版本 / Check GPU driver version
- 验证文件权限设置 / Verify file permissions

## 更新说明 / Update Notes

### 版本更新 / Version Updates
- 定期检查新版本 / Check for new versions regularly
- 按照更新日志进行升级 / Follow changelog for upgrades

### 数据备份 / Data Backup
- 更新前备份数据 / Backup data before updates
- 保存自定义配置 / Save custom configurations 