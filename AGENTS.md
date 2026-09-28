# AGENTS.md

## Working scope

- Use coding agents only from a dedicated Git worktree or fresh clone that contains no private or ignored research data.
- Keep routine agent edits within `src/`, `notebooks/`, and `tests/`.
- Edit `pyproject.toml`, `uv.lock`, `config/`, `.github/`, and project documentation only when the task requires it.
- Do not add new top-level directories or change the repository's data-handling policy without explicit user approval.

## Sensitive data boundary

- Never read, list, search, inspect metadata for, hash, copy, summarize, upload, or modify anything under `data/raw/private/`.
- Exclude `data/raw/private/` from recursive file discovery and searches, even if the directory is present.
- Treat that path as out of scope unless the user explicitly authorizes access for the current task.
- Never place private data or excerpts from it in prompts, logs, notebooks, tests, fixtures, results, commits, or generated artifacts.
- Use synthetic, anonymized, or explicitly approved sample data when code needs representative inputs.
- These instructions reduce accidental access but are not an access-control mechanism. Private data must not be present in the agent worktree or clone.

## Project conventions

- Use `uv` for Python, dependency management, and command execution.
- Keep `pyproject.toml` and `uv.lock` synchronized; do not introduce `requirements.txt` or another package manager unless explicitly requested.
- Treat `data/raw/` as immutable and write derived datasets to `data/processed/`.
- Do not force-add files ignored by `.gitignore`.
- Write generated research outputs to the appropriate directory under `results/`.

## Verification

Before handing off code changes, run:

```bash
uv run ruff check .
uv run pytest
```
