from src.prompts import CODE_GENERATION_PROMPT
from src.services.ai_service import ask
from src.services.memory_service import find_relevant_files
from src.tools.file_tools import read_file
from src.utils.code_utils import clean_code_block


def generate_code(path: str, user_prompt: str) -> str:
    prompt = f"""
{CODE_GENERATION_PROMPT}

Target file:
{path}

User request:
{user_prompt}
"""

    return clean_code_block(ask(prompt))


def improve_code(code: str) -> str:
    prompt = f"""
Improve the following code.

Rules:
- Output ONLY code
- Improve readability
- Improve performance
- Preserve functionality
- Never use markdown
- Never add explanations

Code:

{code}
"""

    return clean_code_block(ask(prompt))


def refactor_code(code: str) -> str:
    prompt = f"""
Refactor the following code.

Rules:
- Output ONLY code
- Reduce duplication
- Improve architecture
- Preserve behavior
- Never use markdown
- Never add explanations

Code:

{code}
"""

    return clean_code_block(ask(prompt))


def modify_project(user_request: str) -> str:
    files = find_relevant_files(user_request)

    if not files:
        return "No relevant files found."

    context = []

    for file in files:
        try:
            code = read_file(file)

            context.append(
                f"""
FILE: {file}

--------------------
{code[:1500]}
--------------------
"""
            )

        except Exception:
            continue

    prompt = f"""
You are a senior Python software architect.

You are analyzing MY EXISTING codebase.

USER REQUEST:
{user_request}

FILES:

{chr(10).join(context)}

STRICT RULES:

- Never explain how to run Python.
- Never explain terminal commands.
- Never generate markdown.
- Never invent commands.
- Never explain CLI usage.
- Only analyze the files provided.
- Do NOT generate code.

Output EXACTLY:

RELATED FILES:
- file1
- file2

CHANGES:
- change 1
- change 2

IMPLEMENTATION STEPS:
1. ...
2. ...
3. ...
"""

    return ask(prompt)