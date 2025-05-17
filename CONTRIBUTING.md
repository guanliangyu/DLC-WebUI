# 贡献指南 / Contributing Guidelines

感谢您对本项目的关注！以下是参与贡献的指南。

## 开始之前 / Before You Start

1. 确保您已经：
   - 阅读了项目的 README.md
   - 查看了现有的 Issues 和 Pull Requests
   - 了解项目的基本架构和功能

## 如何贡献 / How to Contribute

### 1. 提交问题 / Submitting Issues

- 使用清晰的标题
- 提供详细的问题描述
- 包含复现步骤（如果适用）
- 附上相关的日志或截图

### 2. 提交代码 / Submitting Code

1. Fork 项目
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

### 3. 代码规范 / Code Standards

- 遵循 PEP 8 规范
- 使用有意义的变量和函数名
- 添加必要的注释和文档
- 确保代码通过所有测试

### 4. 提交 Pull Request / Pull Request Process

1. 更新 README.md（如果需要）
2. 更新文档（如果需要）
3. 确保 CI 测试通过
4. 等待审核和合并

## 开发设置 / Development Setup

建议使用 Conda 和项目提供的 `environment.yml` 文件来创建和管理开发环境。
It is recommended to use Conda and the `environment.yml` file provided by the project to create and manage the development environment.

```bash
# 克隆仓库 (如果尚未克隆) / Clone repository (if not already cloned)
git clone https://github.com/guanliangyu/DLC-WebUI.git
cd DLC-WebUI

# 使用 environment.yml 创建并激活 Conda 环境
# Create and activate Conda environment using environment.yml
conda env create -f environment.yml
conda activate dlc-webui-env
```

## 测试 / Testing

```bash
# 运行测试
pytest

# 检查代码格式
black .
isort .

# 类型检查
mypy src
```

## 问题反馈 / Getting Help

如果您在贡献过程中遇到任何问题，可以：

- 在 Issues 中提问
- 发送邮件至 liangyu.guan@outlook.com
- 查看项目 Wiki

## 行为准则 / Code of Conduct

- 保持友善和专业的交流态度
- 尊重其他贡献者的观点和建议
- 关注问题的技术本质

## 贡献流程 / Contributing Process

### 1. 问题反馈 / Issue Reporting

- 使用GitHub Issues提交问题
- 清晰描述问题现象和复现步骤
- 提供相关的系统环境信息
- 如果可能，附上截图或错误日志

### 2. 功能建议 / Feature Requests

- 详细描述新功能的用途和价值
- 提供可能的实现方案
- 说明对现有功能的影响

### 3. 代码贡献 / Code Contributing

1. Fork项目到自己的仓库
2. 创建新的特性分支
3. 编写代码和测试
4. 提交Pull Request

## 开发规范 / Development Standards

### 1. 代码风格 / Code Style

- 遵循PEP 8规范
- 使用4空格缩进
- 文件使用UTF-8编码
- 函数和类添加文档字符串

### 2. 命名规范 / Naming Conventions

- 类名使用驼峰命名法
- 函数和变量使用小写字母加下划线
- 常量使用大写字母加下划线
- 私有成员以下划线开头

### 3. 注释规范 / Comment Guidelines

- 所有函数都应有文档字符串
- 复杂逻辑需要添加注释说明
- 注释使用中英双语
- 保持注释的简洁和必要性

### 4. 提交规范 / Commit Guidelines

- 提交信息使用英文
- 简要说明改动内容
- 一次提交只做一件事
- 保持提交历史的清晰

## 测试要求 / Testing Requirements

- 新功能必须包含测试用例
- 修复bug时添加相应的测试
- 确保所有测试通过
- 保持测试覆盖率

## 文档要求 / Documentation Requirements

- 更新相关的文档
- 保持中英双语说明
- 添加必要的示例代码
- 确保文档的准确性

## 版本发布 / Release Process

- 遵循语义化版本规范
- 更新版本日志
- 标注重要的变更
- 进行充分的测试

## 联系方式 / Contact

- GitHub Issues: [问题反馈](https://github.com/guanliangyu/DLC-WebUI/issues)
- Email: liangyu.guan@outlook.com

再次感谢您的贡献！/ Thank you for your contribution!

## 开发规范 / Development Standards

### 目录结构 / Directory Structure
```
DLC-WebUI/
├── src/                # 源代码目录 / Source code directory
│   ├── core/          # 核心功能 / Core functionality
│   │   ├── config/   # 配置管理 / Configuration management
│   │   ├── gpu/      # GPU相关 / GPU related
│   │   ├── utils/    # 通用工具和辅助函数 / Common utilities and helpers
│   │   ├── processors/ # 数据处理和分析 / Data processing and analysis
│   │   └── models/   # 模型定义 / Model definitions
│   ├── ui/           # 界面相关 / UI related
│   │   ├── pages/    # 页面组件 / Page components
│   │   ├── components/ # 可复用组件 / Reusable components
│   │   ├── layouts/  # 页面布局 / Page layouts
│   │   └── styles/   # CSS样式 / CSS styles
│   └── common/       # 通用定义 / Common definitions
│       ├── constants.py
│       ├── types.py
│       └── exceptions.py
├── data/             # 数据目录 / Data directory
│   ├── scratch/      # 抓挠行为数据 / Scratch behavior data
│   ├── grooming/     # 理毛行为数据 / Grooming behavior data
│   ├── swimming/     # 游泳行为数据 / Swimming behavior data
│   ├── three_chamber/ # 三箱实验数据 / Three-chamber data
│   ├── two_social/   # 社交行为数据 / Social behavior data
│   ├── cpp/          # CPP实验数据 / CPP data
│   ├── video_prepare/ # 视频预处理数据 / Video preparation data
│   ├── temp/         # 临时文件 / Temporary files
│   └── results/      # 分析结果 / Analysis results
├── models/           # 模型目录 / Model directory
├── logs/            # 日志目录 / Log directory
├── docs/            # 文档 / Documentation
├── tests/           # 测试 / Tests
│   ├── unit/        # 单元测试 / Unit tests
│   ├── integration/ # 集成测试 / Integration tests
│   └── e2e/         # 端到端测试 / End-to-end tests
└── scripts/         # 工具脚本 / Utility scripts
```

### 代码规范 / Code Standards

1. **类型提示 / Type Hints**
   - 使用Python类型注解 / Use Python type annotations
   - 为所有函数参数和返回值添加类型提示 / Add type hints for all function parameters and return values
   ```python
   from typing import List, Optional, Dict
   
   def process_video(video_path: str, threshold: float = 0.999) -> Optional[Dict]:
       pass
   ```

2. **文档规范 / Documentation Standards**
   - 使用中英双语注释 / Use bilingual comments (Chinese and English)
   - 为所有类和函数添加文档字符串 / Add docstrings for all classes and functions
   ```python
   def analyze_behavior(data: pd.DataFrame) -> Dict:
       """分析行为数据
       Analyze behavior data
       
       Args:
           data: 包含行为数据的DataFrame / DataFrame containing behavior data
           
       Returns:
           分析结果字典 / Dictionary of analysis results
       
       Raises:
           ProcessingError: 当处理失败时 / When processing fails
       """
       pass
   ```

3. **错误处理 / Error Handling**
   - 使用自定义异常类 / Use custom exception classes
   - 提供详细的错误信息 / Provide detailed error messages
   ```python
   class ProcessingError(Exception):
       """视频处理错误 / Video processing error"""
       pass
   ```

4. **日志记录 / Logging**
   - 使用不同级别的日志 / Use different log levels
   - 包含必要的上下文信息 / Include necessary context information
   ```python
   import logging
   logger = logging.getLogger(__name__)
   logger.info("开始处理视频 / Start processing video: %s", video_path)
   ```

### 测试规范 / Testing Standards

1. **单元测试 / Unit Tests**
   - 使用pytest框架 / Use pytest framework
   - 测试覆盖率要求90%以上 / Test coverage should be above 90%
   ```python
   def test_process_video():
       result = process_video("test.mp4")
       assert result is not None
   ```

2. **集成测试 / Integration Tests**
   - 测试组件间的交互 / Test interactions between components
   - 模拟真实使用场景 / Simulate real usage scenarios

3. **端到端测试 / End-to-End Tests**
   - 测试完整的用户流程 / Test complete user workflows
   - 包含UI交互测试 / Include UI interaction tests

### Git 工作流 / Git Workflow

1. **分支管理 / Branch Management**
   - main: 主分支，用于发布 / Main branch for releases
   - develop: 开发分支 / Development branch
   - feature/*: 功能分支 / Feature branches
   - bugfix/*: 修复分支 / Bugfix branches

2. **提交规范 / Commit Conventions**
   ```
   <type>(<scope>): <subject>

   <body>

   <footer>
   ```
   类型 / Types:
   - feat: 新功能 / New feature
   - fix: 修复bug / Bug fix
   - docs: 文档更新 / Documentation updates
   - style: 代码格式 / Code style changes
   - refactor: 重构 / Code refactoring
   - test: 测试相关 / Test related
   - chore: 构建过程或辅助工具的变动 / Build process or auxiliary tool changes

3. **Pull Request 流程 / Pull Request Process**
   - 创建功能分支 / Create feature branch
   - 编写代码和测试 / Write code and tests
   - 提交PR请求 / Create pull request
   - 代码审查 / Code review
   - 合并到develop分支 / Merge to develop branch

### 性能优化 / Performance Optimization

1. **GPU资源管理 / GPU Resource Management**
   - 合理分配GPU资源 / Properly allocate GPU resources
   - 及时释放GPU内存 / Release GPU memory timely

2. **异步处理 / Asynchronous Processing**
   - 使用异步函数处理耗时操作 / Use async functions for time-consuming operations
   - 实现并行处理 / Implement parallel processing

3. **缓存机制 / Caching Mechanism**
   - 缓存常用数据 / Cache frequently used data
   - 实现结果缓存 / Implement result caching

### 安全规范 / Security Standards

1. **配置管理 / Configuration Management**
   - 使用环境变量存储敏感信息 / Use environment variables for sensitive information
   - 加密存储用户凭证 / Encrypt stored user credentials

2. **输入验证 / Input Validation**
   - 验证所有用户输入 / Validate all user inputs
   - 防止路径遍历 / Prevent path traversal

3. **权限控制 / Access Control**
   - 实现用户认证 / Implement user authentication
   - 控制资源访问权限 / Control resource access permissions

### 发布流程 / Release Process

1. **版本号规范 / Version Numbering**
   - 主版本号.次版本号.修订号 / Major.Minor.Patch
   - 遵循语义化版本规范 / Follow semantic versioning

2. **发布检查清单 / Release Checklist**
   - 所有测试通过 / All tests pass
   - 文档更新完成 / Documentation updated
   - 更新日志完善 / Changelog updated
   - 依赖列表更新 / Dependencies updated 