import typer

from src.cli.chat import app as chat_app
from src.cli.file import app as file_app
from src.cli.code import app as code_app
from src.cli.system import app as system_app
from src.cli.project import app as project_app
from src.cli.debug import app as debug_app
from src.cli.memory import app as memory_app
from src.cli.planner import app as planner_app
from src.cli.apply import app as apply_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(chat_app, name="chat")
app.add_typer(file_app, name="file")
app.add_typer(code_app, name="code")
app.add_typer(system_app, name="system")
app.add_typer(project_app, name="project")
app.add_typer(debug_app, name="debug")
app.add_typer(memory_app, name="memory")
app.add_typer(planner_app, name="planner")
app.add_typer(apply_app, name="apply")


if __name__ == "__main__":
    app()