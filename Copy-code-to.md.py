import os
import shutil

# ✅ Customize these paths
SOURCE_FOLDER = r"C:\Programmier Stuff\folder 1"       # <- Where your code lives
TARGET_FOLDER = r"C:\Programmier Stuff\folder 2"   # <- Where the .md files should go

# ✅ File types you want to convert
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

def convert_to_markdown(file_path, output_path):
    ext = os.path.splitext(file_path)[1].lower()
    language = LANGUAGE_MAP.get(ext, "")  # fallback: no language

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        filename = os.path.basename(file_path)
        md_filename = os.path.splitext(filename)[0] + ".md"
        md_path = os.path.join(output_path, md_filename)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {filename}\n\n")
            f.write(f"```{language}\n{code}\n```")

        print(f"✅ Converted: {filename} → {md_filename}")
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def process_folder(source, target):
    if not os.path.exists(target):
        os.makedirs(target)

    for root, _, files in os.walk(source):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in FILE_EXTENSIONS:
                file_path = os.path.join(root, file)
                convert_to_markdown(file_path, target)

process_folder(SOURCE_FOLDER, TARGET_FOLDER)
print("\n🎉 Done! All code files have been embedded into Markdown.")
