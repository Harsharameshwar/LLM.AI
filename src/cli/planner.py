import typer
from rich import print

from src.planners.task_planner import create_plan


app = typer.Typer()


@app.command()
def plan(
    request: str = typer.Argument(...)
):
    print("[yellow]Creating plan...[/yellow]\n")

    result = create_plan(request)

    print(result)