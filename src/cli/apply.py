import typer
from rich import print

from src.services.apply_service import (
    plan_changes,
    apply_changes,
)

app = typer.Typer()


@app.command()
def preview(
    request: str = typer.Argument(...)
):
    print("[yellow]Planning changes...[/yellow]\n")

    result = plan_changes(request)

    print(result)


@app.command()
def run(
    request: str = typer.Argument(...)
):
    print("[yellow]Applying changes...[/yellow]\n")

    modified = apply_changes(request) or []

    if not modified:
        print("\n[yellow]No files were modified.[/yellow]")
        return

    print("\n[green]Modified Files:[/green]\n")

    for file in modified:
        print(f"✓ {file}")