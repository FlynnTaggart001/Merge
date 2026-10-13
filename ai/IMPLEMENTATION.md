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

## Selected toolchain and runtime boundary

The approved development tools are **ChatGPT Plus, Claude Code, and Wingman Premium**, as specified in TOOLCHAIN.md.

These are three different interaction surfaces, not three interchangeable API providers:

- ChatGPT Plus is used interactively for design, planning, audits, and review. A Plus subscription does not grant OpenAI API credentials or API credits.
- Claude Code is the repository-facing coding tool. Its local CLI adapter exists, but the adapter must not be described as fully wired into the team orchestrator until the AgentProvider interface and end-to-end tests prove that.
- Wingman Premium is used inside Unreal Editor. Do not claim programmatic access to Wingman or automatic GitHub synchronization without a verified integration; use the documented handoff.

The existing generic provider registry and legacy HTTP adapters are not proof that the selected tools are connected. Only a real, tested adapter may be marked available. Gemini, Grok, and other products are not part of the active toolchain.

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

The selected tools are already documented in TOOLCHAIN.md. Before claiming automatic orchestration, implement and test a Claude Code adapter that conforms to the runtime AgentProvider interface, register it explicitly, and run a dry-run task through planning, routing, permissions, execution, review, and handoff. Keep ChatGPT Plus interactive and Wingman inside Unreal Editor unless real, tested integrations are added. Do not add unselected providers merely to make the registry appear populated.
