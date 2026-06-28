from pathlib import Path
import json


def analyze_project(project_path: str) -> dict:
    path = Path(project_path)

    result = {
        "type": "Unknown",
        "technologies": [],
        "build_command": None,
        "run_command": None,
    }

    # Node.js / React
    if (path / "package.json").exists():

        result["type"] = "NodeJS"

        with open(path / "package.json", encoding="utf-8") as f:
            package = json.load(f)

        dependencies = {
            **package.get("dependencies", {}),
            **package.get("devDependencies", {}),
        }

        if "react" in dependencies:
            result["technologies"].append("React")

        if "typescript" in dependencies:
            result["technologies"].append("TypeScript")

        if "vite" in dependencies:
            result["technologies"].append("Vite")

        if "@mui/material" in dependencies:
            result["technologies"].append("Material UI")

        result["build_command"] = "npm run build"
        result["run_command"] = "npm run dev"

        return result

    # Modern Python (pyproject.toml)
    if (path / "pyproject.toml").exists():

        result["type"] = "Python"

        content = (path / "pyproject.toml").read_text(
            encoding="utf-8"
        ).lower()

        if "typer" in content:
            result["technologies"].append("Typer")

        if "rich" in content:
            result["technologies"].append("Rich")

        if "ollama" in content:
            result["technologies"].append("Ollama")

        result["build_command"] = "python -m compileall src"
        result["run_command"] = "python -m src.cli.main"

        return result

    # Legacy Python
    if (path / "requirements.txt").exists():

        result["type"] = "Python"

        requirements = (
            path / "requirements.txt"
        ).read_text(encoding="utf-8").lower()

        if "fastapi" in requirements:
            result["technologies"].append("FastAPI")

        if "typer" in requirements:
            result["technologies"].append("Typer")

        if "rich" in requirements:
            result["technologies"].append("Rich")

        result["build_command"] = "python -m compileall src"
        result["run_command"] = "python main.py"

        return result

    return result