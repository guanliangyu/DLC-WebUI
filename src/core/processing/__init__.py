from .mouse_cpp_video_processing import process_cpp_files, process_mouse_cpp_video
from .mouse_grooming_video_processing import (
    process_grooming_files,
    process_mouse_grooming_video,
)
from .mouse_scratch_video_processing import (
    process_mouse_scratch_video,
    process_scratch_files,
)
from .mouse_social_video_processing import (
    process_mouse_social_video,
    process_social_files,
)
from .mouse_swimming_video_processing import (
    process_mouse_swimming_video,
    process_swimming_files,
)
from .three_chamber_video_processing import process_mouse_tc_video, process_tc_files

__all__ = [
    # 抓挠行为分析 / Scratch behavior analysis
    "process_mouse_scratch_video",
    "process_scratch_files",
    # 理毛行为分析 / Grooming behavior analysis
    "process_mouse_grooming_video",
    "process_grooming_files",
    # 三箱实验分析 / Three-chamber test analysis
    "process_mouse_tc_video",
    "process_tc_files",
    # CPP实验分析 / CPP test analysis
    "process_mouse_cpp_video",
    "process_cpp_files",
    # 游泳行为分析 / Swimming behavior analysis
    "process_mouse_swimming_video",
    "process_swimming_files",
    # 社交行为分析 / Social behavior analysis
    "process_mouse_social_video",
    "process_social_files",
]
