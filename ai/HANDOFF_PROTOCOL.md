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


## Handoff spécifique Wingman → GitHub

Quand Wingman Premium est utilisé dans Unreal Editor, ajouter ces informations au handoff (les champs généraux ci-dessus restent obligatoires) :

```text
TOOL_USED: Wingman Premium
UNREAL_ENGINE_VERSION: 5.8.1
PROJECT_OR_MAP:
BLUEPRINTS_ASSETS_SETTINGS_CHANGED:
EDITOR_STEPS_PERFORMED:
LOCAL_VALIDATION: NOT_RUN | PASS | FAIL
PIE_VALIDATION: NOT_RUN | PASS | FAIL
SCREENSHOTS_OR_EVIDENCE:
GITHUB_SYNC_STATUS: NOT_SYNCED | COMMITTED | PR_OPENED
GITHUB_COMMIT_OR_PR:
FOLLOW_UP_REQUIRED:
```

- Ne jamais déclarer un Blueprint, asset ou réglage synchronisé avec GitHub sans vérifier son état réel dans le dépôt.
- Si Wingman ne peut pas écrire dans GitHub, le Game Director ou Claude Code doit reporter le changement dans le dépôt et vérifier le diff.
- Les résultats d'éditeur locaux doivent être distingués des tests CI ; ne pas inventer de capture, commit ou résultat de PIE.
