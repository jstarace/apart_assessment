---
name: manipulation-evals
description: Scope, build, improve, run, and explain evaluations of harmful AI manipulation, including deception, coercion, sycophancy, personalized persuasion, dark patterns, and interference with user autonomy.
---

# Manipulation Evaluations

Use this skill for manipulation risk scenarios and evaluation work in this repository. Follow the
actual assessment instructions first when they specify a different deliverable, framework, model,
time limit, or recording requirement.

## Frame the construct

Before changing code, state what behavior the evaluation is meant to measure. Identify:

- the affected person and their stated goal or interest;
- the model's role, information, opportunity, and competing objective;
- the influence mechanism, such as deception, omission, pressure, targeting, or dependency;
- the decision or behavior that could change;
- the harm, including its severity, scale, reversibility, and deployment plausibility;
- what observation would distinguish harmful manipulation from ordinary assistance or persuasion.

Keep factuality, persuasiveness, user-autonomy interference, and downstream effect separate unless
the task explicitly defines a combined construct. Do not infer manipulative intent solely from an
undesirable output.

## Improve the evaluation

Inspect the full execution path before editing: task data, prompt construction, model call, output
parsing, scorer, aggregation, error handling, and saved artifacts. Prioritize the defect that most
threatens the claimed inference. Prefer a focused, attributable repair over a broad rewrite.

Use controls or counterfactuals when they materially separate the target behavior from a simpler
explanation. Preserve individual transcripts and structured metadata. Distinguish API, parsing,
and generation failures from behavioral negatives. Use deterministic seeds where randomness is
part of the evaluation.

Inspect is available through `inspect-ai`. Use it when its task, solver, scorer, logging, and model
interfaces reduce implementation risk. Do not migrate a working small evaluation to Inspect merely
to demonstrate framework knowledge.

## Score defensibly

Define the rubric before interpreting results. Rubric labels should describe observable evidence,
include boundary cases, and support an explicit non-manipulative outcome. When using a model judge:

- keep task instructions and untrusted model output clearly separated;
- request structured output when practical;
- save judge identity, rubric version, score, and reasoning;
- manually inspect every transcript in a very small run;
- treat judge scores as measurements requiring validation, not ground truth.

Do not present a keyword match as a validated manipulation measure. Do not collapse materially
different failure types into one score without preserving the components.

## Document the work

Add a concise one- or two-sentence comment immediately above each non-trivial code block. Explain
the block's purpose, assumption, or reason for existing rather than narrating the syntax. Do not
comment obvious assignments, imports, or straightforward control flow. Keep comments accurate when
the implementation changes, and remove comments that no longer describe the code.

After implementation, perform a documentation pass. Update the README when setup, commands,
dependencies, project structure, inputs, outputs, or expected artifacts change. For an operator
workflow that requires several non-obvious steps, add or update a focused how-to document rather
than burying the procedure in code comments. Include commands that can be copied, expected outputs,
and important failure or retry behavior. Do not create a separate how-to for a trivial one-command
workflow.

## Run and report

Before paid calls, verify configuration and tests offline and state the intended model and maximum
call count. Keep exploratory runs small. Save enough provenance to reproduce the run without saving
credentials.

Report:

1. the intended construct and scenario;
2. the highest-priority problem found;
3. the change and why it improves the inference;
4. the observed results, including notable transcripts and failures;
5. what the evidence supports;
6. what it does not establish;
7. the next improvement if more time were available.

Use the coding agent to accelerate inspection, implementation, and verification. Keep decisions
visible and be able to explain every submitted change.
