from src.memory.vector_store import VectorStore
from src.tools.file_tools import (
    read_file,
    list_source_files,
)


store = VectorStore()


def index_project(path: str):

    files = list_source_files(path)

    count = 0

    for file in files:

        try:

            content = read_file(str(file))

            if not content.strip():
                continue

            store.add(
                str(file),
                content[:10000],
            )

            print(f"✓ {file}")

            count += 1

        except Exception as e:

            print(f"Failed: {file} -> {e}")

    print(f"\nIndexed {count} files.")


def search_project(query: str):

    result = store.search(query)

    return result