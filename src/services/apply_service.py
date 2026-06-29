import ast
from pathlib import Path

from src.planners.task_planner import create_plan
from src.services.ai_service import ask
from src.services.memory_service import find_relevant_files
from src.services.project_service import build_project


from src.tools.file_tools import (
    backup_file,
    list_source_files,
    read_file,
    write_file,
    restore_backup
)
from src.utils.code_utils import clean_code_block


def find_explicit_file(user_request: str) -> str | None:
    """
    Detect if the user explicitly mentioned a filename.
    Example:
        'Add logging to terminal_tools.py'
    """

    request = user_request.lower()

    files = list_source_files(".")

    for file in files:
        if file.name.lower() in request:
            return str(file)

    return None


def plan_changes(user_request: str) -> str:

    plan = create_plan(user_request)

    explicit_file = find_explicit_file(user_request)

    if explicit_file:
        files = [explicit_file]
    else:
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
{code[:2000]}
--------------------
"""
            )

        except Exception:
            continue

    prompt = f"""
You are a senior Python software architect.

USER REQUEST:
{user_request}

TASK PLAN:
{plan}

FILES:

{chr(10).join(context)}

STRICT RULES:

- Analyze ONLY the provided files.
- Do NOT generate code.
- Do NOT explain terminal commands.
- Do NOT invent new files.
- Do NOT suggest unrelated modifications.

Return EXACTLY in this format:

FILES TO MODIFY:
- file1
- file2

CHANGES:

file1:
- change 1
- change 2

file2:
- change 1

IMPLEMENTATION ORDER:

1. ...
2. ...
3. ...
"""

    return ask(prompt)


def apply_changes(user_request: str):

    explicit_file = find_explicit_file(user_request)

    if explicit_file:
        print(f"\n[SAFE MODE] Explicit file detected: {explicit_file}\n")
        files = [explicit_file]
    else:
        print("\n[SAFE MODE] Using semantic search\n")
        files = find_relevant_files(user_request)

    if not files:
        return []

    modified_files = []

    for file in files:

        try:

            print(f"Processing: {file}")

            original_code = read_file(file)

            prompt = f"""
You are editing EXACTLY ONE FILE.

FILE PATH:
{file}

USER REQUEST:
{user_request}

STRICT RULES:

1. Modify ONLY this file.
2. Preserve all existing functionality.
3. Do NOT rewrite unrelated code.
4. Do NOT add explanations.
5. Do NOT use markdown.
6. Output ONLY valid source code.
7. If no changes are needed, return the original code unchanged.

CURRENT FILE CONTENT:

{original_code}
"""

            updated_code = clean_code_block(ask(prompt))

            if not updated_code.strip():
                print(f"Skipped {file}: empty response")
                continue

            if updated_code.strip() == original_code.strip():
                print(f"Skipped {file}: no changes needed")
                continue

            # Validate Python files before saving
            if Path(file).suffix == ".py":
                try:
                    ast.parse(updated_code)
                except SyntaxError as e:
                    print(f"Skipped {file}: invalid Python generated")
                    print(e)
                    continue

            backup_file(file)
            write_file(file, updated_code)

            modified_files.append(file)

            print(f"Updated: {file}")

        except Exception as e:

            print(f"Failed: {file}")
            print(e)

    # ==========================
    # Build verification starts HERE
    # OUTSIDE the for-loop
    # ==========================

    if not modified_files:
        return []

    print("\nRunning build verification...\n")

    build_result = build_project(".")

    if build_result is None:
        print("No build command found. Skipping verification.")
        return modified_files

    if build_result.success:
        print("✓ Build successful")
        return modified_files

    print("✗ Build failed\n")

    print(build_result.stderr)

    print("\nRestoring backups...\n")

    for file in modified_files:

        try:
            restore_backup(file)
            print(f"✓ Restored: {file}")

        except Exception as e:
            print(f"Failed restoring {file}")
            print(e)

    print("\nRollback complete.")

    return []

    