import os
import subprocess

import streamlit as st


def create_and_start_analysis(
    folder_path, selected_files, config_path, gpu_count, current_time, use_gpus=None
):
    if use_gpus is None:
        use_gpus = list(range(gpu_count))  # Use all GPUs by default

    st.write(
        f"Debug: {len(selected_files)} files for {len(use_gpus)} GPUs"
    )  # Debug output to check the counts

    # Check if there are more GPUs than files, and issue a warning if necessary
    if len(selected_files) < len(use_gpus):
        st.warning(
            "Not enough files for the number of GPUs. Some GPUs will not be used."
        )
        use_gpus = use_gpus[
            : len(selected_files)
        ]  # Reduce the number of GPUs to the number of files

    files_per_gpu = len(selected_files) // len(use_gpus)
    remaining_files = len(selected_files) % len(use_gpus)

    file_groups = []
    start = 0
    processes = []  # To keep track of subprocesses for each GPU
    for i in range(len(use_gpus)):
        end = start + files_per_gpu + (1 if i < remaining_files else 0)
        file_groups.append(selected_files[start:end])
        start = end

    for group_num, files_group in enumerate(file_groups):
        if not files_group:
            continue
        gpu_index = use_gpus[group_num]
        run_py_path_group = os.path.join(folder_path, f"run_gpu{gpu_index}.py")
        start_script_path_group = os.path.join(
            folder_path, f"start_analysis_gpu{gpu_index}.py"
        )
        log_file_path = os.path.join(folder_path, f"output_gpu{gpu_index}.log")

        # Create run.py content
        analyze_videos_code = f"deeplabcut.analyze_videos('{config_path}', {files_group}, videotype='mp4', shuffle=1, trainingsetindex=0, gputouse={gpu_index}, save_as_csv=True)"
        create_labeled_video_code = (
            f"deeplabcut.create_labeled_video('{config_path}', {files_group})"
        )

        content = f"""
import deeplabcut

{analyze_videos_code}

{create_labeled_video_code}
"""
        with open(run_py_path_group, "w") as file:
            file.write(content)

        # Create start_analysis.py content
        start_content = f"""
import subprocess

subprocess.run(['python', '{run_py_path_group}'], check=True)
"""
        with open(start_script_path_group, "w") as file:
            file.write(start_content)

        # Start the analysis without waiting here
        with open(log_file_path, "w") as log_file:
            process = subprocess.Popen(
                ["python", start_script_path_group],
                stdout=log_file,
                stderr=subprocess.STDOUT,
            )
            processes.append(
                (process, gpu_index)
            )  # Append tuple of process and GPU index

    # Optionally wait for all processes to complete after starting all
    for process, gpu_index in processes:
        process.wait()  # Now wait for each process to complete
        if process.returncode != 0:
            st.error(f"Error encountered while running analysis on GPU{gpu_index}")

    # Logging action in a general log file
    general_log_file_path = os.path.join(folder_path, "general_log.txt")
    with open(general_log_file_path, "a") as general_log_file:
        for _, gpu_index in processes:
            general_log_file.write(
                f"{current_time} Analysis started on GPU{gpu_index}\n"
            )


def fetch_last_lines_of_logs(folder_path, gpu_count):
    last_lines = {}
    for group_num in range(gpu_count):
        log_file_path = os.path.join(folder_path, f"output_gpu{group_num}.log")
        try:
            with open(log_file_path, "r") as log_file:
                lines = log_file.readlines()
                last_line = lines[-1] if lines else "No entries in log."
        except FileNotFoundError:
            last_line = "Log file not found."
        last_lines[f"GPU{group_num} Log"] = last_line
    return last_lines
