# Agent Handoff Protocol

Tout agent terminant une tâche doit laisser suffisamment d'informations pour qu'un autre agent puisse reprendre sans conversation précédente.

## Required format

```text
TASK_ID:
STATUS:
SUMMARY:
FILES_CHANGED:
FILES_READ:
TESTS_RUN:
TEST_RESULTS:
DECISIONS:
PROBLEMS_FOUND:
WARNINGS:
BLOCKERS:
RECOMMENDED_NEXT_TASKS:
```

## Rules

- Ne pas omettre un champ important simplement parce qu'il est vide : écrire `None`.
- Ne jamais déclarer un test réussi sans l'avoir réellement exécuté.
- Les recommandations doivent rester distinctes des décisions approuvées.
- Les blockers doivent identifier précisément ce qui empêche la progression.
- Le handoff doit être persistant dans Git ou dans le système de tâches configuré.
