# Task Queue

Cette file contient les tâches orchestrées et leur état persistant.

## Statuts

- `PENDING` — créée mais non planifiable
- `READY` — toutes les dépendances sont satisfaites
- `IN_PROGRESS` — en cours
- `REVIEW` — en attente de review/validation
- `BLOCKED` — dépendance ou décision manquante
- `FAILED` — échec nécessitant traitement
- `COMPLETED` — critères validés
- `CANCELLED` — annulée

## Active

### TASK-0001 — Finaliser l'infrastructure AI collaboration
- **Status:** READY
- **Priority:** HIGH
- **Role:** ARCHITECT / DOCUMENTATION
- **Dependencies:** None
- **Objective:** Valider et compléter le protocole `/ai/` avant le bootstrap Unreal.
- **Acceptance:** protocole, état, tâches, handoffs, permissions et décisions documentés.

## Queue policy

Les tâches sont ajoutées par l'orchestrateur ou par le Game Director. Les agents ne doivent pas supprimer l'historique des tâches terminées.

Une tâche qui dépend d'une tâche non terminée reste `PENDING`.
