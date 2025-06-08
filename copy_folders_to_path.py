import shutil
import os

def copy_folders(destination_path, source_folders):
    destination_path = os.path.abspath(destination_path)

    for source_folder in source_folders:
        source_folder_path = os.path.abspath(source_folder)
        folder_name = os.path.basename(source_folder_path.rstrip("/"))
        destination_full_path = os.path.join(destination_path, folder_name)

        if os.path.exists(destination_full_path):
            print(f"Folder '{folder_name}' already exists. Skip.")
            continue

        try:
            shutil.copytree(source_folder_path, destination_full_path)
            print(f"copied: '{source_folder_path}' → '{destination_full_path}'")
        except Exception as e:
            print(f"failed to copy '{folder_name}': {e}")

# Paths here:
destination = "Path/to/destination"
sources = [
    "Path/to/source",
    "Path/to/source",
]

copy_folders(destination, sources)

