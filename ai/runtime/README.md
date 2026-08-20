# Merge AI Orchestrator Runtime

Executable, provider-agnostic orchestration layer with mandatory safety guards.

## Pipeline (enforced order)

```text
AI Request
  → Validation
  → Token Limits          (TokenGuard)
  → Budget Guard          (BudgetGuard)
  → Rate Limiter          (RateLimiter)
  → Circuit Breaker       (CircuitBreaker)
  → Provider + Retry/Backoff
  → Cost Tracker          (CostTracker)
  → Response
```

No normal code path can bypass the Orchestrator.

## Key modules

| Module | Role |
|--------|------|
| `orchestrator.py` | Central entry-point, wires all guards |
| `token_limits.py` | Hard max input/output/task/session tokens |
| `budget_guard.py` | Cost ceilings (call/task/day/month) |
| `rate_limiter.py` | Sliding-window rate limits |
| `circuit_breaker.py` | Provider failure isolation |
| `retry.py` | Exponential backoff + jitter, non-retryable errors |
| `cost_tracker.py` | Append-only usage log |
| `config.py` | Env-driven configuration |
| `provider_base.py` | Provider protocol + MockProvider |

## Running tests (no API keys required)

```bash
# From repository root
python -m ai.tests.test_orchestrator_pipeline
```

## Configuration

Copy `config.example.env` or root `.env.example` to a local `.env`.
All limits are loaded by `RuntimeConfig.from_env()`.

## Status

Phase 0.5 P0 complete:
- Central orchestrator
- Runtime token limits
- Configurable timeout + real retry + exponential backoff
- Circuit breaker wired into the pipeline
- Integration tests + minimal CI
