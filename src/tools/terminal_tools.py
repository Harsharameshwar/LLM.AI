import subprocess

from src.types import CommandResult


def run_command(command: str, cwd: str | None = None) -> CommandResult:

    print(f"> {command}")

    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    return CommandResult(
        success=result.returncode == 0,
        stdout=result.stdout,
        stderr=result.stderr,
        code=result.returncode,
    )