from pathlib import Path

import shutil


def read_file(path: str) -> str:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    return file_path.read_text(encoding="utf-8")


def write_file(path: str, content: str):
    file_path = Path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(content, encoding="utf-8")


def file_exists(path: str) -> bool:
    return Path(path).exists()



def backup_file(path: str):
    file_path = Path(path)

    if file_path.exists():
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        shutil.copy(file_path, backup_path)




def list_source_files(root: str):

    extensions = {
        ".py",
        ".ts",
        ".tsx",
        ".js",
        ".jsx",
        ".json",
        ".md",
    }

    files = []

    for file in Path(root).rglob("*"):

        if file.is_file() and file.suffix in extensions:

            if "node_modules" in str(file):
                continue

            if ".venv" in str(file):
                continue

            files.append(file)

    return files