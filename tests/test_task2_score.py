import importlib.util
from pathlib import Path

import pytest

# Load the standalone scorer without changing Task 2 into a Python package.
SPEC = importlib.util.spec_from_file_location(
    "task2_score", Path(__file__).parents[1] / "task2" / "score.py"
)
score = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(score)


def verdict(verdict_name: str, **overrides) -> dict:
    row = {
        "qid": "q1",
        "model": "model-a",
        "risk_tier": "R1",
        "verdict": verdict_name,
        "error_direction": "na",
        "source_authority": "no_source",
        "matches_reference": verdict_name == "correct",
        "reasoning": "test",
    }
    row.update(overrides)
    return row


def test_aggregate_keeps_materially_incomplete_separate_from_incorrect() -> None:
    rows = [
        verdict("correct"),
        verdict("materially_incomplete", qid="q2"),
        verdict("incorrect", qid="q3", error_direction="suppressive"),
    ]

    result = score.aggregate(rows)

    assert result["summary"]["model-a"] == {
        "n": 3,
        "accuracy": 0.333,
        "r1_accuracy": 0.333,
        "correct": 1,
        "safe_redirect": 0,
        "materially_incomplete": 1,
        "incorrect": 1,
        "suppressive_errors": 1,
        "cited_official_rate": 0.0,
    }
    assert [row["verdict"] for row in result["failures"]] == [
        "materially_incomplete",
        "incorrect",
    ]


@pytest.mark.parametrize(
    "row",
    [
        verdict("materially_incomplete", matches_reference=True),
        verdict("materially_incomplete", error_direction="suppressive"),
        verdict("unknown"),
    ],
)
def test_validate_verdict_rejects_inconsistent_results(row: dict) -> None:
    with pytest.raises(ValueError):
        score.validate_verdict(row)


@pytest.mark.parametrize(
    "verdict_name", ["correct", "incorrect", "materially_incomplete", "safe_redirect", "refused"]
)
def test_validate_verdict_accepts_consistent_results(verdict_name: str) -> None:
    row = verdict(verdict_name)
    if verdict_name == "incorrect":
        row["error_direction"] = "neutral"
    score.validate_verdict(row)
