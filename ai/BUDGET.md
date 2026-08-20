# Merge AI Budget & Safety Policy

> Default policy. Values are intentionally conservative and can be changed by the Game Director.

## Hard limits

| Limit | Default |
|---|---:|
| Monthly budget | 50 USD |
| Daily budget | 5 USD |
| Maximum cost per task | 2 USD |
| Maximum cost per API call | 0.50 USD |
| Warning threshold | 70% |
| Maximum retries per task | 3 |
| Maximum task iterations | 10 |
| Maximum agent handoffs per task | 20 |

## Default token budgets

| Role | Input tokens | Output tokens |
|---|---:|---:|
| ARCHITECT | 50,000 | 15,000 |
| GAMEPLAY_DESIGNER | 40,000 | 12,000 |
| WORLD_DESIGNER | 40,000 | 12,000 |
| PROGRAMMER | 100,000 | 30,000 |
| REVIEWER | 30,000 | 10,000 |
| QA | 30,000 | 10,000 |
| DOCUMENTATION | 25,000 | 10,000 |

## Safety behavior

1. Every paid call must be estimated before execution.
2. A call is denied if it exceeds the per-call, per-task, daily, or monthly hard limit.
3. At 70% of a budget, the runtime emits a warning.
4. At 100%, the runtime enters `BUDGET_HALT` and refuses new paid calls.
5. Retries count toward all limits.
6. A failed provider call must not silently retry forever.
7. The runtime must not treat provider-reported token usage as trusted billing data when a provider supplies an authoritative usage/cost endpoint; actual provider billing remains the source of truth.
8. If the runtime cannot calculate a safe upper bound for a call, it must deny the call in strict mode.

## Modes

### SIMULATION

No external provider is called and no money is spent. The runtime uses estimates only.

### SUPERVISED

The runtime may call providers inside the configured limits. Calls that require human approval are paused.

### AUTONOMOUS

The runtime can progress automatically inside the hard limits. Human escalation rules remain mandatory.

## Secrets

API keys, OAuth tokens and credentials must never be committed to Git. They must be supplied through environment variables or a secret manager.
