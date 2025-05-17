import streamlit as st


def load_css_styles():
    """加载共享的CSS样式"""
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
    """,
        unsafe_allow_html=True,
    )
