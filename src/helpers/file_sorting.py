import os
from typing import List, Optional


def sort_directory_files(directory: str, file_extension: Optional[str] = None) -> List[str]:
    """Return sorted file names from ``directory`` filtered by extension."""
    try:
        if file_extension:
            files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
        else:
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        files.sort()
        return files
    except Exception as e:
        print(f"Error sorting files in directory: {directory}, {str(e)}")
        return []
