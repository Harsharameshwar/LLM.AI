import typer
from rich import print

from src.services.memory_service import (
    index_project,
    search_project,
)


app = typer.Typer()


@app.command()
def index(
    path: str = typer.Argument(
        ".",
        help="Project directory",
    )
):
    print("[yellow]Indexing project...[/yellow]\n")

    index_project(path)


@app.command()
def search(
    query: str = typer.Argument(
        ...,
        help="Search query",
    )
):

    result = search_project(query)

    documents = result["documents"][0]
    metadata = result["metadatas"][0]

    print("\n[green]Results:[/green]\n")

    for doc, meta in zip(documents, metadata):

        print(f"📄 {meta['path']}\n")