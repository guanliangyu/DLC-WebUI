import streamlit as st
import os
import datetime
from src.core.config import get_root_path, load_config, initialize_authenticator
from src.core.components import render_sidebar

# 设置页面配置
st.set_page_config(
    page_title="DLC-WebUI",
    page_icon="🐁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    /* 隐藏默认的页面导航 */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* 主标题样式 */
    .main-title {
        text-align: center;
        padding: 1rem 0;
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    /* Logo样式 */
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* 卡片容器样式 */
    .stCard {
        background-color: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    /* 功能区块样式 */
    .function-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1.5rem;
        border-left: 5px solid #4CAF50;
    }
    
    /* 说明文字样式 */
    .instruction-text {
        color: #666;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* 系统要求样式 */
    .system-requirements {
        background-color: #e3f2fd;
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-top: 2rem;
        border-left: 5px solid #2196F3;
    }
    
    /* 用户信息样式 */
    .user-info {
        padding: 1rem;
        background-color: #f1f8e9;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }

    /* 侧边栏样式优化 */
    .css-1d391kg {
        padding-top: 2rem;
    }
    
    /* 侧边栏标题样式 */
    .sidebar-title {
        font-size: 1rem;
        color: #2c3e50;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
    }
    
    /* 侧边栏链接样式 */
    .sidebar-link {
        text-decoration: none;
        color: #2c3e50;
        display: block;
        padding: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .sidebar-link:hover {
        color: #4CAF50;
        padding-left: 0.5rem;
    }
    
    /* 侧边栏分割线 */
    .sidebar-divider {
        margin: 1rem 0;
        border-top: 1px solid #e0e0e0;
    }

    /* 导航按钮样式 */
    .stButton button {
        width: 100%;
        text-align: left;
        padding: 0.5rem;
        margin: 0.2rem 0;
        border: none;
        background-color: transparent;
        color: #2c3e50;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #f1f8e9;
        color: #4CAF50;
        padding-left: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_app() -> None:
    """初始化应用程序"""
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None
    if 'name' not in st.session_state:
        st.session_state['name'] = None
    
    # 使用统一的侧边栏组件
    render_sidebar()

def render_user_info(authenticator) -> None:
    """显示用户信息"""
    with st.sidebar:
        st.markdown('<div class="user-info">', unsafe_allow_html=True)
        st.markdown(f"### 👤 用户信息 / User Info")
        st.write(f"欢迎 / Welcome: {st.session_state['name']}")
        st.write(f"上次操作 / Last operation:")
        
        # 读取最后的使用记录
        log_file_path = os.path.join(get_root_path(), 'logs', 'usage.txt')
        try:
            if os.path.exists(log_file_path):
                with open(log_file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if lines:
                        last_log = lines[-1].strip()
                        st.write(f"Initial log entry - {last_log}")
        except Exception as e:
            st.error(f"读取日志错误 / Error reading log: {e}")
            
        authenticator.logout("退出登录 / Logout")
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """主函数"""
    # 加载配置和初始化认证器
    config = load_config(os.path.join(get_root_path(), 'src', 'core', 'config', 'config.yaml'))
    authenticator = initialize_authenticator(config)
    
    if authenticator:
        # 将登录组件放置于侧边栏顶部
        authenticator.login(location="sidebar", fields={"Form name": "登录系统 / Login System"})
        
        # 登录状态检查
        if st.session_state["authentication_status"] is False:
            st.error('用户名或密码错误 / Username/password is incorrect')
            st.stop()  # 停止渲染本次执行，等待用户修改输入
        elif st.session_state["authentication_status"] is None:
            st.warning('请输入用户名和密码 / Please enter your username and password')
            st.stop()  # 停止渲染本次执行，也会保持登录表单可继续交互
    
    # 调用功能导航组件，此时登录组件已位于侧边栏顶部
    initialize_app()
    
    if authenticator and st.session_state.get("authentication_status"):
        # 主页内容
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                try:
                    st.image("assets/logo.png", width=120)
                except Exception:
                    st.text("Logo")
            with col2:
                st.markdown('<h1 style="font-size: 3rem; font-weight: bold; margin-bottom: 0;">欢迎使用 DeepLabCut Web 界面</h1>', unsafe_allow_html=True)
                st.markdown('<p style="font-size: 1.25rem; color: #555;">Welcome to DeepLabCut Web Interface</p>', unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # 功能区块：行为分析
        st.markdown('<div class="function-section">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 1rem;">🔍 行为分析 / Behavior Analysis</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- 🐁 小鼠抓挠 / Mouse Scratch")
            st.markdown("- 🐁 小鼠理毛 / Mouse Grooming")
            st.markdown("- 🐁 小鼠游泳 / Mouse Swimming")
        with col2:
            st.markdown("- 🏠 三箱实验 / Three Chamber")
            st.markdown("- 👥 两鼠社交 / Two Social")
            st.markdown("- 📍 位置偏好 / Mouse CPP")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 功能区块：视频处理
        st.markdown('<div class="function-section">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 1rem;">🎥 视频处理 / Video Processing</h3>', unsafe_allow_html=True)
        st.markdown("- 📽️ 视频预处理 / Video Preparation")
        st.markdown("- ✂️ 视频裁剪 / Video Crop")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 使用说明
        with st.expander("💡 使用说明 / Instructions", expanded=True):
            st.markdown("""1. 所有分析功能都需要预处理后的视频  
2. 视频要求：MP4格式，500x500像素，30帧/秒  
3. 请先使用视频预处理功能处理原始视频  
4. 处理完成后再进行相应的行为分析""")

if __name__ == "__main__":
    main()
