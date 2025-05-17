import os
from typing import Dict, Optional

import streamlit as st


def display_logs(folder_path: str, num_lines: int = 20) -> None:
    """显示日志内容
    Display log contents

    Args:
        folder_path (str): 日志文件所在目录
        num_lines (int): 要显示的最后几行数量
    """
    try:
        log_files = [f for f in os.listdir(folder_path) if f.endswith(".log")]

        if not log_files:
            st.info("未找到日志文件 / No log files found")
            return

        for log_file in log_files:
            log_path = os.path.join(folder_path, log_file)
            with st.expander(f"日志文件 / Log file: {log_file}", expanded=True):
                try:
                    with open(log_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        if lines:
                            last_lines = (
                                lines[-num_lines:] if len(lines) > num_lines else lines
                            )
                            st.code("".join(last_lines))
                        else:
                            st.info("日志文件为空 / Log file is empty")
                except Exception as e:
                    st.error(f"读取日志文件失败 / Failed to read log file: {str(e)}")

    except Exception as e:
        st.error(f"显示日志失败 / Failed to display logs: {str(e)}")


def get_last_log_entries(folder_path: str, num_lines: int = 20) -> Dict[str, str]:
    """获取日志文件的最后几行
    Get the last few lines of log files

    Args:
        folder_path (str): 日志文件所在目录
        num_lines (int): 要获取的行数

    Returns:
        Dict[str, str]: 包含日志文件名和内容的字典
    """
    log_contents = {}
    try:
        for file in os.listdir(folder_path):
            if file.endswith(".log"):
                file_path = os.path.join(folder_path, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        last_lines = (
                            lines[-num_lines:] if len(lines) > num_lines else lines
                        )
                        log_contents[file] = "".join(last_lines)
                except Exception as e:
                    log_contents[file] = f"Error reading log file: {str(e)}"
    except Exception as e:
        st.error(f"读取日志文件时出错 / Error reading log files: {str(e)}")

    return log_contents
