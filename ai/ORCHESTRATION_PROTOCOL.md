# Merge — AI Orchestration Protocol

**Statut : APPROUVÉ — pré-API**  
**Date : 2026-08-20**

## Pipeline obligatoire

```text
OBJECTIVE
  ↓
READ PROJECT STATE
  ↓
DECOMPOSE TASK
  ↓
CHECK DEPENDENCIES
  ↓
CHECK PERMISSIONS
  ↓
ASSIGN ROLE
  ↓
EXECUTE
  ↓
VALIDATE
  ↓
REVIEW
  ↓
UPDATE PROJECT STATE
  ↓
HANDOFF / NEXT TASK
```

## Contrat de tâche

Chaque tâche doit avoir un identifiant unique, un objectif, un rôle, des dépendances, des critères d'acceptation et une méthode de validation.

## Limites d'orchestration

- Une tâche ne peut pas dépasser son budget de tokens/coût.
- Les retries sont plafonnés.
- Les boucles de review sont plafonnées.
- Une dépendance `BLOCKED` empêche l'exécution des tâches qui en dépendent.
- Une décision `PENDING_HUMAN` ne peut pas être auto-résolue par une IA.

## Handoff

Le résultat doit toujours indiquer :

`TASK_ID`, `STATUS`, `SUMMARY`, `FILES_CHANGED`, `TESTS_RUN`, `TEST_RESULTS`, `DECISIONS`, `PROBLEMS_FOUND`, `WARNINGS`, `BLOCKERS`, `RECOMMENDED_NEXT_TASKS`.

## Séparation des responsabilités

L'agent qui implémente une modification importante ne doit pas être le seul validateur lorsque plusieurs rôles sont disponibles.

## Pré-API

Le protocole est conçu pour fonctionner avec ou sans fournisseur IA connecté. Avant les API, les tâches peuvent être simulées par des fixtures et tests locaux afin de valider les garde-fous, transitions d'état et contrats.
