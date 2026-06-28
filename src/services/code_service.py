from src.prompts import CODE_GENERATION_PROMPT
from src.services.ai_service import ask


def generate_code(path: str, user_prompt: str) -> str:
    prompt = f"""
{CODE_GENERATION_PROMPT}

Target file:
{path}

User request:
{user_prompt}
"""

    return ask(prompt)


def improve_code(code: str) -> str:
    prompt = f"""
Improve the following code.

Rules:
- Output ONLY code
- Improve readability
- Improve performance
- Preserve functionality

Code:

{code}
"""

    return ask(prompt)


def refactor_code(code: str) -> str:
    prompt = f"""
Refactor the following code.

Rules:
- Output ONLY code
- Reduce duplication
- Improve architecture
- Preserve behavior

Code:

{code}
"""

    return ask(prompt)