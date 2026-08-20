# AI Orchestration Implementation

## Important distinction

The `/ai/` directory defines the persistent protocol and state of the Merge multi-agent system. It does **not** by itself create API access to external AI providers.

The executable orchestration layer must live outside the repository when provider credentials or local execution environments are required, or inside a dedicated tool/runtime once those integrations are actually available.

## Required runtime capabilities

The real orchestrator must be able to:

1. accept one human objective;
2. read the Merge repository;
3. create/update tasks;
4. select an available agent by capability;
5. send the relevant context to that agent;
6. receive its output;
7. persist the handoff;
8. run validation commands where available;
9. create correction tasks after failures;
10. update project state;
11. create commits/branches/PRs according to permissions;
12. stop on `PENDING_HUMAN` decisions.

## Provider abstraction

Implement providers behind a common interface rather than hard-coding a model:

```text
AgentProvider
  - id
  - capabilities
  - availability
  - execute(task, context)
  - health_check()
```

Possible providers include GPT/Codex, Claude, Gemini, GitHub Copilot and future providers, but only providers with a real configured integration may be marked available.

## Recommended first runtime

The first executable version should prioritize reliability over maximum autonomy:

- one orchestrator process;
- GitHub as persistent project state;
- explicit task IDs;
- sequential execution by default;
- optional parallelism only for independent tasks;
- validation after every implementation task;
- human approval for critical architecture and destructive operations.

## No fake autonomy

Do not create scripts that merely print messages pretending to call other AIs. A provider must have a real integration before it can be selected for execution.

## Next implementation milestone

Create the executable runtime only after selecting and configuring the actual provider integrations available to the development environment. Then perform a dry run that creates a task and handoff without modifying game code.
