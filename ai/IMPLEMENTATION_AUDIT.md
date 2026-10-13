# Merge — AI Collaboration Implementation Audit

**Date:** 2026-08-24
**Scope:** AI collaboration, orchestration, recommendations, reviews, human gates and resumability.

| Rule / capability | Runtime status | Implementation |
|---|---|---|
| Hard token ceilings | IMPLEMENTED | `orchestrator.py`, `token_limits.py` |
| Budget Guard | IMPLEMENTED | `budget_guard.py` |
| Rate limiting | IMPLEMENTED | `rate_limiter.py` |
| Circuit breaker | IMPLEMENTED | `circuit_breaker.py` |
| Timeout/retry/backoff | IMPLEMENTED | `retry.py` + provider execution |
| Cost tracking | IMPLEMENTED | `cost_tracker.py` |
| Fail-closed pipeline | IMPLEMENTED | `orchestrator.py` |
| Offline provider tests | IMPLEMENTED | existing mock/scripted tests |
| Role registry | IMPLEMENTED | `AGENT_REGISTRY.md`, `agent_router.py` |
| Provider registry | IMPLEMENTED | `providers.py` |
| Automatic role fallback | IMPLEMENTED | `role_assignment.py` |
| AI task decomposition | IMPLEMENTED | `ai_task_planner.py` |
| Task contract validation | IMPLEMENTED | `task_planner.py` |
| Persistent task queue | IMPLEMENTED | `task_store.py`, `team_workflow.py` |
| Dependency resolution | IMPLEMENTED | `DependencyGraph` |
| Cycle detection | IMPLEMENTED | `DependencyGraph.detect_cycles()` |
| Least privilege | IMPLEMENTED | `permissions.py` |
| Devil's Advocate | IMPLEMENTED | `recommendation_engine.py` |
| Independent review | IMPLEMENTED | `team_workflow.py` |
| QA stage | IMPLEMENTED | `team_workflow.py` |
| Confidence escalation | IMPLEMENTED | `RecommendationEngine` |
| Human decision ledger | IMPLEMENTED | `decision_manager.py`, `DECISIONS.md` |
| Explicit critical execution gate | IMPLEMENTED | `execution_gate.py` |
| Recommendation persistence | IMPLEMENTED | `RecommendationStore` |
| Disagreement persistence | IMPLEMENTED | `Disagreement` ledger |
| Structured handoffs | IMPLEMENTED | `handoff.py` |
| Resumable project state | IMPLEMENTED | `project_state.py` |
| Proactive state recommendations | IMPLEMENTED | `proactive_recommendations.py` |
| Follow-up task generation | IMPLEMENTED | `TeamWorkflow.followup_planner` + `TaskStore` |
| Role-specific provider execution | IMPLEMENTED | `team_factory.py` |
| CI coverage for new runtime contracts | IMPLEMENTED | `.github/workflows/ai-runtime.yml` |
| Automatic Git commit/merge authority | HUMAN CONTROLLED | no runtime auto-approval |
| Unreal compile / PIE validation | EXTERNAL ENVIRONMENT | requires local UE5 machine |
| Real API credentials | EXTERNAL ENVIRONMENT | intentionally not stored in Git |

## Important interpretation

"Implemented" means the repository now contains the runtime contract and enforcement path. It does not mean external providers, Unreal Engine, Git credentials or a human decision have been fabricated.

The runtime remains truthful about unavailable external execution.


## Addendum — selected toolchain (2026-10-13)

The Game Director selected **ChatGPT Plus, Claude Code, and Wingman Premium** as the only AI tools for Merge. See TOOLCHAIN.md.

This decision does not change the meaning of the historical audit rows above: runtime guardrails and orchestration contracts can be implemented while real external tool integrations remain unverified.

- ChatGPT Plus is interactive; it must not be treated as an OpenAI API provider or as including API credits.
- Claude Code is the repository-facing coding tool, but its local adapter still requires a verified end-to-end connection to the runtime provider interface before automatic orchestration can be claimed.
- Wingman Premium is used inside Unreal Editor. GitHub handoff remains manual unless a real integration is tested.
- Gemini, Grok, and other providers are not selected for active use. Legacy adapter code, if retained, is inactive and must not be routed by default.
- Unreal compilation and PIE remain local validations and must not be inferred from CI success.
