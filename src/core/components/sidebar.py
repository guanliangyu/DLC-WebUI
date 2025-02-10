import streamlit as st
import os
from src.core.config import get_root_path

def render_user_info() -> None:
    """显示用户信息"""
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
    st.markdown('</div>', unsafe_allow_html=True)

def render_sidebar() -> None:
    """渲染统一的侧边栏导航"""
    with st.sidebar:
        # 如果用户已登录，显示用户信息
        if st.session_state.get("authentication_status"):
            render_user_info()
            st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # 主页导航
        st.markdown('<div class="sidebar-title">🏠 主页 / Home</div>', unsafe_allow_html=True)
        if st.button("🏠 主页 / Home"):
            st.switch_page("Home.py")
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # 视频处理导航
        st.markdown('<div class="sidebar-title">🎥 视频处理 / Video Processing</div>', unsafe_allow_html=True)
        if st.button("📽️ 视频预处理 / Video Preparation"):
            st.switch_page("pages/7_Video_Preparation.py")
        if st.button("✂️ 视频裁剪 / Video Crop"):
            st.switch_page("pages/8_Video_Crop.py")
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # 行为分析导航
        st.markdown('<div class="sidebar-title">🔍 行为分析 / Behavior Analysis</div>', unsafe_allow_html=True)
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
            
        # 如果用户已登录，显示登出按钮
        if st.session_state.get("authentication_status"):
            st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
            if st.button("🚪 退出登录 / Logout"):
                st.session_state['authentication_status'] = None
                st.session_state['name'] = None
                st.rerun() 