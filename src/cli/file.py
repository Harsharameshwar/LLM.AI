import typer
from rich import print

from src.services.ai_service import ask
from src.tools.file_tools import read_file


app = typer.Typer()


@app.command()
def explain(path: str):
    code = read_file(path)

    prompt = f"""
Explain this code:

{code}

Explain:
1. Purpose
2. Architecture
3. Important functions
4. Improvements
"""

    print(ask(prompt))


@app.command(name="ask-file")
def ask_file(path: str, question: str):
    code = read_file(path)

    prompt = f"""
Code:

{code}

Question:

{question}
"""

    print(ask(prompt))