import os
import tkinter as tk
from tkinter import filedialog

def choose_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder = filedialog.askdirectory(title="Select the parent folder")
    return folder

def delete_index_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        folder_name = os.path.basename(root)
        index_filename = f"{folder_name}.md"
        index_path = os.path.join(root, index_filename)

        if os.path.isfile(index_path):
            try:
                os.remove(index_path)
                print(f"✅ Deleted index file: {index_path}")
            except Exception as e:
                print(f"❌ Error deleting {index_path}: {e}")
        else:
            print(f"ℹ️ No index file found in: {root}")

# Open Explorer and get the folder
selected_folder = choose_folder()

if selected_folder:
    print(f"\n🔍 Selected folder: {selected_folder}")
    delete_index_files(selected_folder)
    print("\n✅ Done cleaning up index files.")
else:
    print("\n❌ No folder selected. Aborting.")
