import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_obsidian_links(text):
    # Handle links with display text first: [[Page|Display]]
    text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', text)
    # Handle regular links: [[Page]]
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        cleaned_content = clean_obsidian_links(content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    # Setup tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Let user pick a file
    file_path = filedialog.askopenfilename(
        title="Select a Markdown file",
        filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
    )

    if not file_path:
        print("No file selected.")
        return

    # Ask for confirmation
    filename = os.path.basename(file_path)
    confirm = messagebox.askyesno("Confirm Deletion", f"Do you really want to delete all links from \"{filename}\"?")

    if confirm:
        process_file(file_path)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
