# Managed by LLM AI

from src.services.ai_service import ask
from src.tools.terminal_tools import run_command
from src.services.project_service import analyze_project

def run_build(command: str = "npm run build") -> dict:
    return run_command(command)


def analyze_error(error: str) -> str:
    prompt = f"""
You are a senior software engineer.

Analyze the following build error.

Provide:

1. Root cause
2. Affected technology
3. Suggested fix
4. Files that might need changes

Error:

{error}
"""

    return ask(prompt)





def fix_project(project_path: str):

    project = analyze_project(project_path)

    build_command = project["build_command"]

    if not build_command:
        return "No build command found."

    result = run_command(
        build_command,
        cwd=project_path,
    )

    if result.success:
        return "✅ Build successful."

    prompt = f"""
You are an expert software engineer.

Project Type:
{project["type"]}

Technologies:
{project["technologies"]}

Build Error:

{result.stderr}

Provide:

1. Root Cause
2. Exact Fix
3. Files that should be modified
4. Why this happened
"""

    return ask(prompt)
