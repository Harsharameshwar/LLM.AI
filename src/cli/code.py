import typer
from rich import print

from src.services.code_service import (
    generate_code,
    improve_code,
    refactor_code,
)

from src.tools.file_tools import (
    read_file,
    write_file,
    backup_file,
)

app = typer.Typer()


@app.command()
def create(path: str, prompt: str):

    code = generate_code(path, prompt)

    write_file(path, code)

    print(f"[green]Created:[/green] {path}")


@app.command()
def improve(path: str):

    code = read_file(path)

    improved = improve_code(code)

    if not improved.strip():
        print("[red]AI returned empty content[/red]")
        return

    backup_file(path)
    write_file(path, improved)

    print(f"[green]Improved:[/green] {path}")


@app.command()
def refactor(path: str):

    code = read_file(path)

    refactored = refactor_code(code)

    if not refactored.strip():
        print("[red]AI returned empty content[/red]")
        return

    backup_file(path)
    write_file(path, refactored)

    print(f"[green]Refactored:[/green] {path}")