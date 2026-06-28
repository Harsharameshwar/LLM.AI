import chromadb


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=".reva_memory")

        self.collection = self.client.get_or_create_collection(
            name="project_files"
        )

    def add(self, file_path: str, content: str):

        self.collection.upsert(
            ids=[file_path],
            documents=[content],
            metadatas=[
                {
                    "path": file_path,
                }
            ],
        )

    def search(self, query: str, limit: int = 5):

        result = self.collection.query(
            query_texts=[query],
            n_results=limit,
        )

        return result