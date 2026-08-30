# Apart Assessment Practice

This private repository contains original practice exercises for AI manipulation evaluation
work. The exercises are designed to develop the same underlying skills as a short research
work sample without attempting to reproduce confidential assessment material.

## Practice goals

- Turn a broad manipulation concern into a testable risk scenario.
- Identify the most important validity problem in a small evaluation.
- Make a focused improvement under time pressure.
- Run inexpensive model calls and inspect the resulting transcripts.
- Explain what the evidence supports, what it does not support, and what should happen next.

## Setup

The project uses Python 3.11 or newer and [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env
```

Add the Anthropic and OpenAI API keys to `.env`. The `.env` file is ignored by Git.

Run the starter command:

```bash
uv run apart-assessment
```

Run the development checks:

```bash
uv run ruff check .
uv run pytest
```

## Planned structure

```text
src/apart_assessment/   Shared evaluation code and command-line entry point
tests/                  Offline tests
mocks/                  Self-contained mock assessment briefs and starter materials
outputs/                Local run artifacts, when an exercise requires them
```

Each mock will include a risk-scoping task, a deliberately limited or flawed evaluation, and a
short recorded-walkthrough prompt. Model usage should remain inexpensive, and claims should be
calibrated to the number and quality of the completed runs.
