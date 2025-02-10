import streamlit as st
import os
import tempfile
import shutil
import zipfile
import hashlib

def create_download_button(directory, pattern="*", key=None):
    """Creates a download button for files in a specified directory matching the pattern."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Simplify the zip filename to avoid long names
        if isinstance(pattern, list):
            # Hash the string representation of the list to get a unique short name
            hash_object = hashlib.sha1(str(pattern).encode())
            hex_dig = hash_object.hexdigest()[:10]  # Get first 10 characters of the hash
            zip_filename = f"files_{hex_dig}.zip"
        else:
            pattern_clean = pattern.replace('*', 'all').replace('.', '')
            zip_filename = f"{pattern_clean}_files.zip"

        zip_path = os.path.join(tmpdirname, zip_filename)

        # Define the function to check file inclusion based on extensions
        def include_file(file):
            if isinstance(pattern, list):
                return any(file.endswith(ext) for ext in pattern)
            return True if pattern == "*" else file.endswith(pattern)

        # Create the zip file with the filtered files
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    if include_file(filename):
                        file_path = os.path.join(foldername, filename)
                        zipf.write(file_path, arcname=os.path.relpath(file_path, start=directory))

        # Create the download button using the zip file
        with open(zip_path, "rb") as f:
            btn_key = key if key else "download_btn"
            st.write("Click the button below to download results")
            st.download_button(f"Download {zip_filename}", f, file_name=zip_filename, key=btn_key)

# Example usage in a Streamlit app
def filter_and_zip_files(directory, excluded_ext=None, included_ext=None):
    """Utility to create zip for specific file types."""
    pattern = included_ext if included_ext else "*"
    if excluded_ext:
        all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        pattern = [f for f in all_files if not any(f.endswith(ext) for ext in excluded_ext)]
    create_download_button(directory, pattern=pattern)
