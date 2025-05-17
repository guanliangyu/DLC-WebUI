import GPUtil
import streamlit as st


def get_gpu_utilization():
    """Return GPU utilization information as a list of dictionaries."""
    gpus = GPUtil.getGPUs()
    usage_info = []
    for gpu in gpus:
        usage_info.append(
            {
                "id": gpu.id,
                "memory_util": gpu.memoryUtil,
                "gpu_util": gpu.load,
                "total_memory": gpu.memoryTotal,
                "used_memory": gpu.memoryUsed,
            }
        )
    return usage_info


def display_gpu_usage():
    gpu_info = get_gpu_utilization()
    high_memory_usage = False

    if gpu_info:
        st.write("### GPU Utilization:")
        for info in gpu_info:
            st.write(
                f"GPU {info['id']}: {info['gpu_util']*100:.1f}% load,"
                f" Memory Usage: {info['used_memory']}/{info['total_memory']} MB"
            )
            if info["memory_util"] > 0.75:
                high_memory_usage = True
    else:
        st.write("No GPU found or GPU utilization not available.")

    return high_memory_usage
