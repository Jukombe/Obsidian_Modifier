import os

# Path to your Obsidian Vault
VAULT_PATH = r"vault path"

# Define subfolders and associated hashtags
TAG_FOLDERS = {
    "folder name"
}

# Define root folders in which index files should be created (recursively)
INDEX_ROOT_FOLDERS = [
    "folder name"
]

def determine_tag_for_folder(folder_path):
    relative_path = os.path.relpath(folder_path, VAULT_PATH)
    parts = relative_path.split(os.sep)
    for part in parts:
        if part in TAG_FOLDERS:
            return TAG_FOLDERS[part]
    return ""

def should_create_index(folder_path):
    relative_path = os.path.relpath(folder_path, VAULT_PATH)
    parts = relative_path.split(os.sep)
    return any(part in INDEX_ROOT_FOLDERS for part in parts)

def add_tag_to_file(file_path, tag):
    try:
        with open(file_path, "r+", encoding="utf-8") as file:
            content = file.read()
            if not content.startswith(tag):
                file.seek(0, 0)
                file.write(f"{tag}\n{content}")
                print(f"  -> Tag '{tag}' added to '{file_path}'.")
            else:
                print(f"  -> Tag '{tag}' already present in '{file_path}'.")
    except Exception as e:
        print(f"  -> Error adding tag to '{file_path}': {e}")

def create_index_file(folder_path):
    folder_name = os.path.basename(folder_path)

    if folder_path == VAULT_PATH:
        print(f"\nSkipping main directory: {folder_name}")
        return

    index_name = f"{folder_name}.md"
    index_path = os.path.join(folder_path, index_name)
    links = []

    print(f"\nCreating index file for folder: {folder_name}")

    header_tag = determine_tag_for_folder(folder_path)
    if header_tag:
        print(f"  -> Tag '{header_tag}' will be written at the top of the file '{index_name}'.")
    else:
        print(f"  -> No tag found or required for '{folder_name}'.")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if item.endswith(".md") and not item.startswith('.') and len(item) > 3:
            if item != index_name:
                link = f"- [[{item}]]"
                links.append(link)
                print(f"  -> Markdown file found and linked: {item}")

                if not (item.endswith(".ecxalidraw.md") or item.endswith(".excalidraw.md")):
                    if header_tag:
                        add_tag_to_file(item_path, header_tag)

        elif item.endswith(".PDF") and not item.startswith('.'):
            link = f"- [{item}]({item})"
            links.append(link)
            print(f"  -> PDF file found and linked: {item}")

        elif item.endswith(".canvas") and not item.startswith('.'):
            link = f"- [[{item}]]"
            links.append(link)
            print(f"  -> Canvas file found and linked: {item}")

        elif item.endswith(".py") and not item.startswith('.'):
            link = f"- [[{item}]]"
            links.append(link)
            print(f"  -> Python file found and linked: {item}")

        elif item.endswith(".css") and not item.startswith('.'):
            link = f"- [[{item}]]"
            links.append(link)
            print(f"  -> CSS file found and linked: {item}")

        elif item.endswith(".bat") and not item.startswith('.'):
            link = f"- [[{item}]]"
            links.append(link)
            print(f"  -> Batch file found and linked: {item}")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path) and not item.startswith('.'):
            subfolder_index = f"{item}/{item}.md"
            subfolder_index_path = os.path.join(folder_path, subfolder_index.replace("/", os.sep))
            if os.path.exists(subfolder_index_path):
                link = f"- [[{subfolder_index}]]"
                links.append(link)
                print(f"  -> Folder index found and linked: {subfolder_index}")
            else:
                print(f"  -> No index file found in folder: '{item}'.")

    try:
        with open(index_path, "w", encoding="utf-8") as f:
            if header_tag:
                f.write(f"{header_tag}\n")
                print(f"  -> Tag '{header_tag}' successfully written to '{index_name}'.")
            f.write("## Linked Files and Folders\n")
            f.write("\n".join(links))
            f.write("\n")
    except Exception as e:
        print(f"  -> Error writing the file: '{index_name}': {e}")

def process_vault(vault_path):
    for root, dirs, files in os.walk(vault_path):
        if should_create_index(root):
            create_index_file(root)

process_vault(VAULT_PATH)
print("\nIndex files and tags have been created and updated.")
