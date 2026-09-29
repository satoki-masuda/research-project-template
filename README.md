# Project Title

Short description of the research project.

## Overview

Describe the following:

- research question
- project objective
- main analysis or methodology
- expected outputs

## Project structure

```text
.
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
├── data/
│   ├── raw/
│   │   └── schema/
│   └── processed/
│       └── schema/
├── notebooks/
│   ├── exploratory/
│   └── reports/
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── analysis/
│   └── visualization/
├── tests/
├── config/
├── results/
│   ├── models/
│   ├── figures/
│   └── tables/
├── manuscripts/
├── slides/
│   ├── assets/
│   ├── themes/
│   │   └── research.css
│   ├── dist/              # generated; not tracked
│   └── slides.md
├── AGENTS.md
├── .gitignore
├── LICENSE
├── package.json
├── package-lock.json
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## Directory conventions

| Directory | Purpose |
| --- | --- |
| `data/raw/` | Original source data. Never edit it manually. |
| `data/raw/schema/` | Version-controlled schemas and data dictionaries for original inputs. |
| `data/processed/` | Analysis-ready data derived from raw data. |
| `data/processed/schema/` | Version-controlled schemas and data dictionaries for derived datasets. |
| `notebooks/exploratory/` | Exploration, prototyping, and one-off checks. |
| `notebooks/reports/` | Finalized, narrative analyses and reports. |
| `src/data/` | Reusable loading, validation, cleaning, and preprocessing code. |
| `src/analysis/` | Statistical analysis, modeling, and analytical code. |
| `src/visualization/` | Reusable plotting and visualization code. |
| `tests/` | Automated tests for reusable code. |
| `config/` | Version-controlled parameters and non-secret configuration. |
| `results/models/` | Generated model artifacts. |
| `results/figures/` | Generated figures. |
| `results/tables/` | Generated tables. |
| `manuscripts/` | Manuscript sources, bibliography files, and LaTeX support files. |
| `slides/` | Marp slide source, local assets, and the shared research theme. |

## Data and manuscript policy

- Everything under `data/` is ignored by Git, except `.gitkeep` files that preserve the directory structure and the contents of `data/raw/schema/` and `data/processed/schema/`.
- Treat `data/raw/` as immutable. Create derived datasets in `data/processed/`.
- Document original inputs in `data/raw/schema/` and derived datasets in `data/processed/schema/`. Include column names, types, nullability, constraints, and descriptions, but never include real records, secrets, identifiers, or sensitive sample values.
- Store sensitive raw data, when needed, under `data/raw/private/`. Never make that directory available in a coding-agent workspace.
- Under `manuscripts/`, Git tracks only `.tex`, `.bib`, `.cls`, `.sty`, and `.gitkeep` files.
- Do not commit secrets. Put local environment values in `.env`; provide safe examples in `.env.example` when needed.

## Coding-agent workflow

Use Codex or another coding agent only in a dedicated Git worktree or a fresh clone that contains tracked project files but no private research data. Keep the primary checkout, where private data may exist, separate from the agent workspace.

For example, create a task-specific worktree from the repository's primary checkout:

```bash
git worktree add ../project-codex -b codex/task main
cd ../project-codex
uv sync --locked --dev
```

A fresh clone in a separate location is also suitable. Before starting an agent, verify that `data/raw/private/` and other sensitive ignored files are absent from that workspace. Agents may use the tracked metadata in the schema directories; use synthetic, anonymized, or explicitly approved sample data when actual records are needed for development and tests.

`AGENTS.md` defines the expected agent scope: routine work stays in `src/`, `notebooks/`, and `tests/`, with project configuration and documentation changed only when necessary. It also prohibits any access to `data/raw/private/`. These instructions help prevent mistakes, but they are not a security boundary; separation of the private data from the agent workspace is the actual protection.

## Environment

This project uses [uv](https://docs.astral.sh/uv/) to manage Python, dependencies, and the lockfile. Keep `pyproject.toml`, `uv.lock`, and `.python-version` under version control.

```bash
uv sync --locked --dev
```

The template includes a baseline research stack:

- data and scientific computing: NumPy, pandas, SciPy, scikit-learn, and statsmodels
- tabular file support: openpyxl
- visualization: Matplotlib and seaborn
- geospatial analysis: GeoPandas and Shapely
- graph analysis: NetworkX
- research utilities: jpholiday and tqdm
- notebook environment: Jupyter and ipykernel

Run project commands inside the managed environment:

```bash
uv run pytest
uv run ruff check .
```

Add a runtime dependency with `uv add PACKAGE`; add a development dependency with `uv add --dev PACKAGE`.

## Slides

Slides are written in Markdown with Marp. Node.js 20 or later is required.

```bash
npm ci
npm run slides:preview
```

Edit `slides/slides.md`, place images in `slides/assets/`, and adjust the shared style in `slides/themes/research.css`. Build all distribution formats with:

```bash
npm run slides:build
```

The generated HTML, PDF, and PowerPoint files are written to the ignored `slides/dist/` directory. Each build removes old files first. GitHub Actions also builds the same files and stores them as a downloadable workflow artifact.

## Reproducible workflow

1. Place original inputs in `data/raw/` without modifying them.
2. Document input structure in `data/raw/schema/` without copying real records or sensitive values.
3. Put reusable processing and analysis logic in `src/`.
4. Keep exploratory work in `notebooks/exploratory/`; move finalized narratives to `notebooks/reports/`.
5. Write generated datasets to `data/processed/` and document their structure in `data/processed/schema/`.
6. Write generated outputs to `results/`.
7. Record parameters in `config/`, add tests in `tests/`, and commit source files together with `uv.lock`.

## License

This project is licensed under the MIT License. See `LICENSE`.
