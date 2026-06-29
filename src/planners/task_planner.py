from src.services.ai_service import ask


def create_plan(user_request: str) -> str:

    prompt = f"""
You are an expert software architect.

User Request:
{user_request}

Convert this into a precise software engineering task.

Return EXACTLY:

TASK:
<one sentence>

SEARCH_TERMS:
- term1
- term2
- term3

GOAL:
<expected result>

Do not explain anything else.
"""

    return ask(prompt)