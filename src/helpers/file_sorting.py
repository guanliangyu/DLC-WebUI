import os


def sort_directory_files(directory, file_extension=None):
    """Sorts and returns files from the specified directory optionally filtered by file extension."""
    try:
        if file_extension:
            files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
        else:
            files = [
                f
                for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))
            ]
        files.sort()
        return files
    except Exception as e:
        print(f"Error sorting files in directory: {directory}, {str(e)}")
        return []
