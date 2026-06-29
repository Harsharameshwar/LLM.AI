# Managed by LLM AI

import typer
from rich import print

from src.services.ai_service import ask


app = typer.Typer()


@app.command()
def chat():
    """Start interactive chat."""

    print("[green]LLM AI v0.1[/green]")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You > ")

        if prompt.lower() == "exit":
            break

        response = ask(prompt)

        print(f"\n[cyan]LLM >[/cyan]\n{response}\n")
