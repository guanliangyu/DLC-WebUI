import os
from typing import List, Optional

import streamlit as st


def upload_files(
    allowed_types: List[str], upload_dir: str, key: Optional[str] = None
) -> List[str]:
    """处理文件上传
    Handle file uploads

    Args:
        allowed_types (List[str]): 允许的文件类型列表
        upload_dir (str): 上传文件保存目录
        key (Optional[str]): Streamlit组件的key

    Returns:
        List[str]: 成功上传的文件路径列表
    """
    uploaded_files = []

    try:
        files = st.file_uploader(
            "选择文件上传 / Choose files to upload",
            type=allowed_types,
            accept_multiple_files=True,
            key=key,
        )

        if files:
            os.makedirs(upload_dir, exist_ok=True)

            for file in files:
                try:
                    file_path = os.path.join(upload_dir, file.name)
                    with open(file_path, "wb") as f:
                        f.write(file.getbuffer())
                    uploaded_files.append(file_path)
                    st.success(
                        f"文件上传成功 / File uploaded successfully: {file.name}"
                    )
                except Exception as e:
                    st.error(
                        f"上传文件失败 / Failed to upload file {file.name}: {str(e)}"
                    )

    except Exception as e:
        st.error(f"文件上传过程出错 / Error during file upload: {str(e)}")

    return uploaded_files
