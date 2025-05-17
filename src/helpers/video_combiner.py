import os


def create_video_combination_script(folder_path, selected_files, output_directory):
    """Creates a Python script to combine selected video files using ffmpeg."""
    if not selected_files:
        raise ValueError("No files provided for combination.")

    # Ensure the base output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    base_name = f"{os.path.basename(selected_files[0]).split('.')[0]}-{len(selected_files)}-combined"
    text_filename = f"{base_name}.txt"
    script_filename = f"{base_name}.py"
    output_filename = f"{base_name}.mp4"

    # Update paths for text file, script, and output video
    text_path = os.path.join(folder_path, text_filename)
    script_path = os.path.join(folder_path, script_filename)
    output_full_path = os.path.join(
        output_directory, output_filename
    )  # Output video in 'combined-video' subdirectory

    with open(text_path, "w") as txt_file:
        for file in selected_files:
            txt_file.write(f"file '{file}'\n")

    with open(script_path, "w") as py_file:
        py_file.write("import subprocess\n")
        command = [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            text_path,
            "-c",
            "copy",
            output_full_path,
        ]
        py_file.write(f"subprocess.run({command}, check=True)\n")

    return script_path


if __name__ == "__main__":
    # Example usage: Run this module directly to test the combination script creation.
    selected_files = [
        "/home/Public/DLC-Web/Scratch/video_prepare/2024-05-28/red-1.MP4",
        "/home/Public/DLC-Web/Scratch/video_prepare/2024-05-28/red-2.MP4",
        "/home/Public/DLC-Web/Scratch/video_prepare/2024-05-28/red-3.MP4",
    ]
    output_directory = "/home/Public/DLC-Web/Scratch/video_prepare/2024-05-28"
    create_video_combination_script(selected_files, output_directory)
