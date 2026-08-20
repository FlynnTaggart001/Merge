# Merge AI Orchestrator Runtime

This directory contains the provider-agnostic executable orchestration layer.

## Design

```text
CLI
 ↓
Orchestrator
 ├── RepositoryState
 ├── TaskPlanner
 ├── AgentRouter
 ├── ValidationRunner
 └── Persistence
       ↓
    AgentProvider
       ├── OpenAI/Codex
       ├── Claude
       ├── Gemini
       ├── GitHub/Copilot
       └── Future providers
```

The runtime must never contain provider secrets. Credentials are supplied through environment variables or the host's secret manager.

## Current status

Scaffold only. Provider calls are intentionally not implemented until the corresponding integrations are configured.

The first executable milestone is a dry-run that reads the repository and produces a task plan without changing game code.
