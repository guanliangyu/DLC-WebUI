import os
from typing import List


def list_directories(path: str) -> List[str]:
    """Return a list of subdirectories within ``path``."""
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
