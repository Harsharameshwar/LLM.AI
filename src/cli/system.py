import typer
from rich import print

from src.tools.terminal_tools import run_command


app = typer.Typer()


@app.command()
def run(command: str):

    result = run_command(command)

    print(result["stdout"])

    if result["stderr"]:
        print(result["stderr"])


@app.command()
def version():
    print("LLM AI v0.1")