# Merge AI Development System

Ce dossier contient le protocole partagé utilisé pour coordonner les agents IA de Merge.

Les garde-fous et les contrats du workflow existent, mais les connexions automatiques aux outils doivent être validées séparément. La pile retenue est ChatGPT Plus, Claude Code et Wingman Premium ; voir TOOLCHAIN.md.

## Fichiers principaux

- `TOOLCHAIN.md` — outils retenus, responsabilités et limites d'intégration
- `AI_ORCHESTRATOR.md` — contrat de l'orchestrateur
- `AGENT_REGISTRY.md` — agents et capacités
- `PROJECT_STATE.md` — état partagé
- `TASK_QUEUE.md` — tâches et dépendances
- `DECISIONS.md` — décisions
- `HANDOFF_PROTOCOL.md` — transmissions
- `PERMISSIONS.md` — autonomie et garde-fous

Le dépôt est la mémoire persistante commune. Le Game Director reste l'autorité finale sur les décisions critiques.

**Statut : règles et garde-fous documentés ; intégration automatique de Claude Code et handoff Wingman → GitHub à valider.**
