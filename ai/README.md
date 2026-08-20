# Merge AI Development System

Ce dossier contient le protocole partagé utilisé pour coordonner les agents IA de Merge.

## Objectif

Permettre au Game Director de donner un objectif de haut niveau et permettre à l'orchestration de transformer cet objectif en tâches exécutables, validables et traçables.

## Fichiers principaux

- `AI_ORCHESTRATOR.md` — contrat et comportement de l'orchestrateur
- `AGENT_REGISTRY.md` — agents disponibles et capacités
- `PROJECT_STATE.md` — état partagé du projet
- `TASK_QUEUE.md` — file des tâches et dépendances
- `DECISIONS.md` — décisions importantes et décisions en attente
- `HANDOFF_PROTOCOL.md` — format de transmission entre agents
- `PERMISSIONS.md` — niveaux d'autonomie et garde-fous

## Règle essentielle

Le dépôt est la mémoire persistante commune. Aucun agent ne doit supposer qu'un autre agent connaît son contexte conversationnel.

Le Game Director reste l'autorité finale sur les décisions critiques.

**Statut : infrastructure en construction.**
