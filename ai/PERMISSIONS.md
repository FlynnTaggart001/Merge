# AI Permissions

## Levels

| Level | Permission | Default automation |
|---|---|---|
| L0 | Read/analyse | Allowed |
| L1 | Documentation | Allowed |
| L2 | Code/tests | Allowed for scoped tasks |
| L3 | Commit | Allowed only when validation passes |
| L4 | Merge/release | Supervised by default |
| L5 | Critical architecture / scope | Human approval required |

## Mandatory escalation

Escalate to the Game Director for:

- engine changes;
- major architecture changes;
- major scope changes;
- deletion of major systems/content;
- irreversible destructive operations;
- unresolved agent disagreement;
- repeated validation failure beyond retry limits.

## Security

Never store API keys, OAuth tokens, passwords or private credentials in the repository.
