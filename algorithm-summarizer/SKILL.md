---
name: algorithm-summarizer
description: Add summary comments for algorithm practice solutions in this Python_problems project. Use when the user asks to summarize, explain, document, or add comments for the problem solved in a Python file, especially prompts like "summarize the problem solved in file_name.py", "detail the approach", "what algorithm/pattern is this", or "tack the summary as a comment in the file".
---

# Algorithm Summarizer

Analyze Python algorithm-solution files in this project and add a compact, accurate top-of-file comment explaining the problem, approach, algorithm, pattern, and complexity.

## Workflow

1. Resolve the requested file path from the project root when the user gives a bare filename.
2. Read the entire target file before summarizing.
3. Identify the solved problem from, in order:
   - Existing comments, docstrings, function names, class names, examples, and variable names.
   - The control flow and data structures in the implementation.
   - The filename, only as supporting evidence.
4. Explain the approach at the level needed for interview review:
   - State the core idea in one or two sentences.
   - List the main algorithm steps in execution order.
   - Name the dominant pattern, such as sliding window, binary search, DFS/BFS, dynamic programming, greedy, heap, monotonic stack/queue, prefix sum, union-find, backtracking, topological sort, two pointers, bit manipulation, or simulation.
   - Include time and space complexity with variables defined from the code.
5. Insert the summary as a top-of-file Python comment block before imports/classes/functions unless the user explicitly asks for chat-only output. Preserve existing code behavior.

## Comment Format

Use this shape when adding a summary to a Python file:

```python
# Problem summary:
# - ...
#
# Approach:
# - ...
#
# Pattern:
# - ...
#
# Complexity:
# - Time: ...
# - Space: ...
```

Keep comments concise enough to be useful during review. Prefer precise bullets over long paragraphs.

## Accuracy Rules

- Do not claim the exact LeetCode title unless it appears in the file or is obvious from the implementation and filename.
- If multiple patterns appear, name the primary pattern first and mention supporting techniques second.
- If the file contains multiple independent solutions, summarize each one separately.
- If the implementation appears incomplete, buggy, or exploratory, say so and summarize what the code currently does.
- Do not rewrite the algorithm unless the user asks for code changes.
- Do not add broad tutorial material; focus on the specific file.
