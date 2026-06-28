import typer
from rich import print

from src.services.debug_service import (
    run_build,
    analyze_error,
)
from src.services.debug_service import fix_project

app = typer.Typer()

@app.command()
def build(
    command: str = typer.Argument(
        "npm run build",
        help="Command to execute",
    )
):
    """Run a build command."""

    result = run_build(command)

    if result["success"]:
        print("[green]Build successful[/green]")
        print(result["stdout"])
        return

    print("[red]Build failed[/red]")
    print(result["stderr"])


@app.command()
def analyze(
    command: str = typer.Argument(
        "npm run build",
        help="Command to analyze",
    )
):
    """Run build and analyze failures."""

    result = run_build(command)

    if result["success"]:
        print("[green]Build successful[/green]")
        return

    print("[yellow]Analyzing build errors...[/yellow]\n")

    analysis = analyze_error(result["stderr"])

    print(analysis)

@app.command()
def fix(
    path: str = typer.Argument(
        ".",
        help="Project directory",
    )
):
    print("[yellow]Analyzing project...[/yellow]")

    result = fix_project(path)

    print(result)