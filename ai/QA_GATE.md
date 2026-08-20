# Merge — QA & Validation Gate

**Statut : APPROUVÉ — pré-API**  
**Date : 2026-08-20**

## Definition of Done

Une tâche n'est `COMPLETED` que si les critères applicables sont satisfaits et vérifiables.

### Documentation
- cohérence avec `GAME_BIBLE.md` et `specs/` ;
- aucune décision contradictoire non documentée ;
- changelog mis à jour si nécessaire.

### Code
- compilation réussie lorsque le projet existe ;
- tests pertinents exécutés ;
- aucun secret ou credential dans le diff ;
- pas de modification hors périmètre sans justification.

### IA / orchestration
- quotas respectés ;
- timeout/retry respectés ;
- sortie conforme au contrat ;
- erreurs et blocages correctement remontés ;
- aucune affirmation de test non exécuté.

## Niveaux de validation

1. **Automatique** : format, secrets, limites, schémas, tests.
2. **Agent QA** : comportement et régression.
3. **Review architecture** : changements structurants.
4. **Game Director** : décisions critiques et changements de scope.

## Échec

Un échec ne doit pas être masqué. La tâche devient `FAILED` ou `BLOCKED` avec la cause, les tests concernés et la prochaine action recommandée.

## Pré-API

Les garde-fous de sécurité peuvent être testés sans fournisseur externe en utilisant des valeurs simulées et des scénarios limites : dépassement de tokens, dépassement de budget, timeout, trop de retries, concurrence excessive et circuit breaker.
