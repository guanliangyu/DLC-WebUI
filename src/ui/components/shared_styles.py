import os

import streamlit as st

from src.core.config import get_root_path


def load_custom_css():
    """加载自定义CSS样式 / Load custom CSS styles"""
    st.markdown(
        """
    <style>
        /* 隐藏默认的页面导航 */
        [data-testid="stSidebarNav"] {
            display: none;
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
        
        /* 用户信息样式 */
        .user-info {
            padding: 1rem;
            background-color: #f1f8e9;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def add_navigation_and_user_info():
    """添加导航栏和用户信息 / Add navigation and user info"""
    with st.sidebar:
        st.markdown(
            '<div class="sidebar-title">📊 功能导航 / Navigation</div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        # 使用按钮实现导航
        if st.button("🏠 主页 / Home"):
            st.switch_page("app.py")
        if st.button("🐁 小鼠抓挠 / Mouse Scratch"):
            st.switch_page("pages/1_Mouse_Scratch.py")
        if st.button("🐁 小鼠理毛 / Mouse Grooming"):
            st.switch_page("pages/2_Mouse_Grooming.py")
        if st.button("🐁 小鼠游泳 / Mouse Swimming"):
            st.switch_page("pages/3_Mouse_Swimming.py")
        if st.button("🏠 三箱实验 / Three Chamber"):
            st.switch_page("pages/4_Three_Chamber.py")
        if st.button("👥 两鼠社交 / Two Social"):
            st.switch_page("pages/5_Two_Social.py")
        if st.button("📍 位置偏好 / Mouse CPP"):
            st.switch_page("pages/6_Mouse_CPP.py")
        if st.button("📽️ 视频预处理 / Video Preparation"):
            st.switch_page("pages/7_Video_Preparation.py")
        if st.button("✂️ 视频裁剪 / Video Crop"):
            st.switch_page("pages/8_Video_Crop.py")

        # 添加用户信息显示
        st.markdown('<div class="user-info">', unsafe_allow_html=True)
        st.markdown(f"### 👤 用户信息 / User Info")
        if "name" in st.session_state:
            st.write(f"欢迎 / Welcome: {st.session_state['name']}")
        st.write(f"上次操作 / Last operation:")

        # 读取最后的使用记录
        log_file_path = os.path.join(get_root_path(), "logs", "usage.txt")
        try:
            if os.path.exists(log_file_path):
                with open(log_file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if lines:
                        last_log = lines[-1].strip()
                        st.write(f"Initial log entry - {last_log}")
        except Exception as e:
            st.error(f"读取日志错误 / Error reading log: {e}")
        st.markdown("</div>", unsafe_allow_html=True)
