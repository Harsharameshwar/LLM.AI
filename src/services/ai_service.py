from src.models.ollama_client import OllamaClient


client = OllamaClient()


def ask(prompt: str) -> str:
    return client.ask(prompt)