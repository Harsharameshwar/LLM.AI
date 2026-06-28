import typer
from rich import print

from src.services.project_service import analyze_project


app = typer.Typer()


@app.command()
def analyze(
    path: str = typer.Argument(
        ".",
        help="Project directory to analyze",
    )
):
    info = analyze_project(path)

    print(f"\n[green]Project Type:[/green] {info['type']}")

    print("\n[cyan]Technologies:[/cyan]")

    if info["technologies"]:
        for tech in info["technologies"]:
            print(f"✓ {tech}")
    else:
        print("No technologies detected")

    print(f"\nBuild: {info['build_command']}")
    print(f"Run:   {info['run_command']}")