# Apart Research Work Sample

This repository contains my work for the Apart Research manipulation evaluations assessment.
It provides a reproducible environment for scoping risk scenarios, implementing and improving
evaluations, running model experiments, inspecting transcripts, and reporting results.

The repository may also contain a limited number of mock exercises used to verify the environment
before beginning the assessment. Mock materials will be clearly separated from submitted work.

## Setup

The project uses Python 3.11 or newer and [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env
```

Add the Anthropic and OpenAI API keys to `.env`. The `.env` file is ignored by Git and must never
be included when this repository is shared.

Run the command-line entry point:

```bash
uv run apart-assessment
```

The environment also includes [Inspect AI](https://inspect.aisi.org.uk/) for evaluations that
benefit from its task, solver, scorer, model, and logging interfaces:

```bash
uv run inspect --version
uv run inspect view
```

Inspect is available as a tool, not a required structure for every assessment task. A focused
change to a supplied evaluation may be more appropriate than a framework migration.

Run the development checks:

```bash
uv run ruff check .
uv run pytest
```

## Project structure

```text
src/apart_assessment/   Evaluation code and command-line entry point
tests/                  Offline tests
mocks/                  Optional mock exercises, kept separate from assessment work
outputs/                Generated results and run artifacts
.agents/skills/         Project-local Codex guidance for manipulation evaluations
```

The final structure will follow the assessment instructions once they are released. Evaluation
outputs should preserve enough information to reproduce each run, inspect individual transcripts,
distinguish execution failures from behavioral results, and understand the limits of any reported
aggregate.
