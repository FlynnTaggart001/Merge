# Merge — AI Toolchain (canonical)

**Decision approved by the Game Director — 2026-10-13**

The only AI tools selected for Merge development are:

1. **ChatGPT Plus** — project discussion, design decisions, system audits, planning, contradiction checks, and review. GitHub remains the source of truth: approved decisions must be recorded in the relevant canonical document.
2. **Claude Code** — repository-aware coding, implementation, refactoring, tests, and GitHub changes. It must read the relevant project rules before editing and report exactly what it changed and tested.
3. **Wingman Premium** — work inside Unreal Engine, especially editor-side/Blueprint assistance and local iteration. Wingman is not assumed to have GitHub access; any resulting change must be handed back through the documented GitHub workflow.

No Gemini, Grok, GitHub Copilot, or other AI product is part of the selected Merge toolchain. Historical references or dormant adapter code do not mean that a tool is currently approved or configured.

## Responsibilities and boundaries

| Tool | Primary responsibility | Boundary |
|---|---|---|
| ChatGPT Plus | Think, design, audit, explain, plan, review | A Plus subscription is not an OpenAI API key or API credit balance. Do not route runtime API calls through it or claim that it is programmatically connected. |
| Claude Code | Read/edit the repository, implement tasks, refactor, run available tests, prepare changes | Must respect AI_RULES.md, canonical gameplay docs, permission boundaries, and human approval gates. Do not claim Unreal compilation/PIE succeeded unless actually run on a machine with UE installed. |
| Wingman Premium | Assist inside Unreal Editor and support local Blueprint/editor work | Treat GitHub handoff as manual unless a real integration is explicitly verified. Do not let editor-side suggestions silently override canonical GitHub rules. |

## Standard workflow

1. The Game Director states the objective.
2. ChatGPT Plus helps clarify the design, risks, dependencies, and acceptance criteria.
3. Approved design decisions are written to the existing canonical GitHub documents; do not create competing specifications.
4. Claude Code reads AI_RULES.md, ai/TOOLCHAIN.md, the current project state, and relevant specs, then implements repository tasks in a reviewable change.
5. Claude Code reports changed files, tests actually run, outcomes, blockers, and any decisions requiring approval.
6. Wingman is used for Unreal Editor work that needs local interaction. The user or Claude Code records the outcome, changed assets/settings, and validation results back in GitHub.
7. Review the diff and test results before accepting changes. Unreal compile and Play-In-Editor (PIE) checks must be reported separately from Python/CI checks.
8. Update CHANGELOG.md, ai/PROJECT_STATE.md, and ROADMAP.md only when the actual project state warrants it.

## Runtime/orchestrator limitation

The repository's guarded orchestration runtime does not automatically gain access to ChatGPT Plus or Wingman merely because the user has those subscriptions. ChatGPT Plus is used interactively; Wingman is used in Unreal; Claude Code is the repository-facing coding tool. Do not mark any tool as runtime-connected until a real, tested adapter exists. Existing API adapters for other providers are not part of the selected workflow and must not be routed by default.

## Security and cost

- Never commit credentials, session tokens, or personal configuration.
- Do not add API keys for ChatGPT Plus; the subscription and OpenAI API billing are separate.
- Do not infer subscription usage or costs from the orchestrator's token/API budget guards.
- Prefer local tests and fixed, deterministic validation where possible.
- The Game Director retains final authority. Suggestions are not approvals.
