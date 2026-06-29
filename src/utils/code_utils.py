import re


def clean_code_block(text: str) -> str:
    """
    Remove markdown code fences produced by LLMs.
    """

    text = text.strip()

    # Remove opening fence
    text = re.sub(
        r"^```[\w+-]*\n",
        "",
        text,
    )

    # Remove closing fence
    text = re.sub(
        r"\n```$",
        "",
        text,
    )

    return text.strip()