import os

# ✅ Set your source and destination folders
SOURCE_FOLDER = r"D:\Path\To\Your\Code"
TARGET_FOLDER = r"D:\Path\To\Your\Markdowns"

# ✅ Supported file extensions
FILE_EXTENSIONS = [".py", ".html", ".css", ".js", ".ts", ".json", ".sh", ".bat"]

# Mapping extensions to language names for markdown code blocks
LANGUAGE_MAP = {
    ".py": "python",
    ".html": "html",
    ".css": "css",
    ".js": "javascript",
    ".ts": "typescript",
    ".json": "json",
    ".sh": "bash",
    ".bat": "batch"
}

def convert_code_to_markdown(input_file_path, output_md_path, language):
    try:
        with open(input_file_path, "r", encoding="utf-8") as code_file:
            code = code_file.read()

        with open(output_md_path, "w", encoding="utf-8") as md_file:
            filename = os.path.basename(input_file_path)
            md_file.write(f"# {filename}\n\n")
            md_file.write(f"```{language}\n{code}\n```")

        print(f"✅ {input_file_path} → {output_md_path}")
    except Exception as e:
        print(f"❌ Error with {input_file_path}: {e}")

def process_folder_recursive(source_root, target_root):
    for root, _, files in os.walk(source_root):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in FILE_EXTENSIONS:
                rel_path = os.path.relpath(root, source_root)  # relative subfolder path
                output_dir = os.path.join(target_root, rel_path)
                os.makedirs(output_dir, exist_ok=True)

                input_file_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0] + ".md"
                output_md_path = os.path.join(output_dir, base_name)

                language = LANGUAGE_MAP.get(ext, "")
                convert_code_to_markdown(input_file_path, output_md_path, language)

# Run it
process_folder_recursive(SOURCE_FOLDER, TARGET_FOLDER)
print("\n🎉 All code files converted and saved with folder structure.")
