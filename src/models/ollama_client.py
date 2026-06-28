import ollama


class OllamaClient:
    def __init__(self, model="qwen2.5-coder:3b"):
        self.model = model

    def ask(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]