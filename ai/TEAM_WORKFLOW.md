# Merge — Multi-Agent Team Workflow

## Purpose

This document describes the runtime implementation of the collaboration rules in `AI_RULES.md`.

## Operational pipeline

```text
OBJECTIVE
  ↓
PROJECT STATE
  ↓
AI TASK DECOMPOSITION
  ↓
DEPENDENCY VALIDATION / CYCLE CHECK
  ↓
ROLE ASSIGNMENT + PROVIDER ROUTING
  ↓
LEAST-PRIVILEGE PERMISSION CHECK
  ↓
PROPOSAL
  ↓
DEVIL_ADVOCATE
  ↓
INDEPENDENT REVIEW
  ↓
QA
  ↓
RECOMMENDATION / HUMAN DECISION GATE
  ↓
GUARDED EXECUTION
  ↓
STRUCTURED HANDOFF
  ↓
PROJECT STATE UPDATE
  ↓
FOLLOW-UP TASK GENERATION
```

## Decision levels

- `NO_CONCERN`: continue normally.
- `SUGGESTION`: record an improvement; do not execute it as a decision.
- `REVIEW`: require additional review.
- `PENDING_HUMAN`: stop the affected task until the Game Director decides.
- `BLOCKED`: stop until the blocking constraint is resolved.

Critical/irreversible/destructive actions require an explicit `APPROVED` human decision before execution.

## Persistent state

Runtime state is kept outside design documents:

- `ai/runtime/state/project_state.json`
- `ai/runtime/state/decisions.json`
- `ai/runtime/state/recommendations.jsonl`
- `ai/runtime/state/handoffs.jsonl`

These files are generated during local runtime and must not contain secrets.

## Implemented components

- `task_planner.py` — task contracts and dependency graph.
- `ai_task_planner.py` — AI-assisted decomposition with safe fallback.
- `role_assignment.py` — deterministic role fallback.
- `agent_router.py` — role-to-provider preference table.
- `permissions.py` — least-privilege enforcement.
- `recommendation_engine.py` — proposal + Devil's Advocate review.
- `decision_manager.py` — human decisions and disagreement ledger.
- `execution_gate.py` — explicit approval gate for critical actions.
- `handoff.py` — structured cross-agent handoffs.
- `project_state.py` — persistent resumable state.
- `proactive_recommendations.py` — state-based proactive suggestions.
- `team_workflow.py` — end-to-end supervised pipeline.
- `team_factory.py` — provider-registry wiring.

## Selected toolchain handoff

Follow TOOLCHAIN.md as the source of truth for the three approved tools.

- **ChatGPT Plus:** interactive design, planning, audit, and review. Approved decisions must be written to canonical GitHub documents. It is not an OpenAI API key or an automatically callable runtime provider.
- **Claude Code:** repository implementation and available tests. Read the relevant canonical docs before edits and report the exact files changed and tests actually run.
- **Wingman Premium:** Unreal Editor/Blueprint assistance. GitHub access is not assumed; use a structured handoff to record changes and local validation.
- Never mark any of these as automatically connected unless the integration has been exercised successfully end to end.
- Do not route Gemini, Grok, or generic OpenAI API adapters as part of the selected toolchain.

## Selected toolchain handoff

Follow TOOLCHAIN.md as the source of truth for the three approved tools.

- **ChatGPT Plus:** interactive design, planning, audit, and review. Approved decisions must be written to canonical GitHub documents. It is not an OpenAI API key or an automatically callable runtime provider.
- **Claude Code:** repository implementation and available tests. Read the relevant canonical docs before edits and report the exact files changed and tests actually run.
- **Wingman Premium:** Unreal Editor/Blueprint assistance. GitHub access is not assumed; use a structured handoff to record changes and local validation.
- Never mark any of these as automatically connected unless the integration has been exercised successfully end to end.
- Do not route Gemini, Grok, or generic OpenAI API adapters as part of the selected toolchain.

## Limits

The runtime never claims that an external provider, Unreal Editor, compiler, or Git operation ran unless the connected host actually performed it. Provider credentials remain outside the repository.
