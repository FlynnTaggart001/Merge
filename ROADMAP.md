# Development Roadmap - ROADMAP.md

## Vue d'ensemble

Cette roadmap définit les grandes phases de développement de **Merge**.

---

## PHASE 0 : Préproduction

**Statut : 🟢 TERMINÉE**

- [x] Structure dépôt, GAME_BIBLE, AI_RULES, architecture, UE5 + C++

---

## PHASE 0.5 : Infrastructure de développement IA

**Statut : 🟢 P0 TERMINÉE — orchestrateur + garde-fous runtime opérationnels**

### Fondations établies
- [x] Protocole multi-agents et docs `/ai/`
- [x] BudgetGuard, RateLimiter, CircuitBreaker, CostTracker
- [x] Token limits runtime
- [x] Retry + exponential backoff + jitter
- [x] Orchestrateur central intégré
- [x] Tests d'intégration (12 scénarios)
- [x] CI GitHub Actions

### Restant (post-P0)
- [ ] Planner → exécution réelle de tâches
- [ ] Brancher les providers IA réels derrière l'orchestrateur

---

## PHASE 1 : Bootstrap Unreal Engine 5

**Statut : 🟡 SCAFFOLD LIVRÉ — compilation locale requise**

### Livré sur GitHub
- [x] `Merge.uproject` (UE 5.5)
- [x] Module C++ `Merge` (Core + Character)
- [x] Config DefaultEngine / Input / GameplayTags
- [x] Guide `docs/UE5_SETUP.md`

### À valider en local
- [ ] Générer project files + compiler
- [ ] Créer BP_* + L_TestArena
- [ ] PIE : move / look / jump

---

## PHASE 2+ : (inchangé — à venir)

Prototype technique → gameplay → vertical slice → contenu → release.

---

**Dernière mise à jour** : 2026-08-20  
**Moteur** : Unreal Engine 5.5  
**Langage principal** : C++
