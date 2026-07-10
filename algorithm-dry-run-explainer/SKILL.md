---
name: algorithm-dry-run-explainer
description: Create concise example dry runs for algorithm practice solutions in this Python_problems project. Use when the user asks for a dry run, trace, walkthrough, example execution, or to add dry-run comments for a Python solution file, especially prompts like "give an example dry run of file_name.py", "trace this solution", or "add a dry run comment".
---

# Algorithm Dry Run Explainer

Analyze Python algorithm-solution files in this project and produce a short example dry run that makes the main state changes clear.

## Workflow

1. Resolve the requested file path from the project root when the user gives a bare filename.
2. Read the entire target file before choosing an example.
3. Choose a small input that exercises the main idea:
   - Prefer an input already present in comments/tests.
   - Otherwise create a representative input that fits the code's expected arguments.
4. Walk through the key state changes, not every low-value line.
5. Show important variables or data structures after each meaningful step.
6. End with the returned answer and why it matches the problem.
7. If the user asks to add the dry run to the file, insert a Python comment block near the top of the file, preferably after any summary block and before imports/classes/functions. Preserve existing code behavior.

## Comment Format

Use this shape when adding an example dry run to a Python file:

```python
# Example dry run:
# - Input: ...
# - Step 1: ...
# - Step 2: ...
# - Output: ...
```

Keep dry runs short. Use enough state detail to explain the algorithm's pattern without turning the file into a full tutorial.

## Accuracy Rules

- Do not invent constraints or examples that conflict with the implementation.
- If the function signature expects multiple inputs, show all of them.
- If the solution contains multiple independent methods, dry run the method the user asks about; otherwise choose the main solution method.
- If the code appears incomplete or buggy, say what the current code would do rather than silently correcting it.
- Do not rewrite the algorithm unless the user asks for code changes.
