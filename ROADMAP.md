# Development Roadmap - ROADMAP.md

## Vue d'ensemble

Cette roadmap définit les grandes phases de développement de **Merge**.

---

## PHASE 0 : Préproduction

**Statut : 🟢 TERMINÉE**

- [x] Structure dépôt, GAME_BIBLE, AI_RULES, architecture, UE5 + C++
- [x] Principes fondamentaux de gameplay et du monde persistant spécifiés
- [x] Furtivité, Backstab, roulade et accroupissement cadrés architecturalement
- [x] Écosystème prédateur/proie et populations dynamiques spécifiés
- [x] Monde non régénératif et multi-mondes spécifiés

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
- [x] `Merge.uproject` (UE 5.8.1)
- [x] Module C++ `Merge` (Core + Character)
- [x] Config DefaultEngine / Input / GameplayTags
- [x] Guide `docs/UE5_SETUP.md`
- [x] Spécification gameplay/world ajoutée sans implémentation prématurée

### À valider en local
- [ ] Générer project files + compiler
- [ ] Créer BP_* + L_TestArena
- [ ] PIE : move / look / jump
- [ ] Valider la base caméra troisième personne

---

## PHASE 2 : Prototype Gameplay

**Statut : ⚪ À VENIR**

### Mouvement
- [ ] Accroupissement
- [ ] Roulade / esquive
- [ ] États de mouvement et transitions

### Furtivité / Combat
- [ ] Système de bruit et visibilité
- [ ] Détection progressive des ennemis
- [ ] États Calme / Soupçon / Recherche / Alerte / Combat
- [ ] Backstab conditionnel

### Monde vivant
- [ ] Définitions d'espèces
- [ ] Populations abstraites
- [ ] Reproduction
- [ ] Mortalité
- [ ] Prédateur / proie
- [ ] Ressources et capacité écologique
- [ ] Migration
- [ ] Extinction locale

### Persistance
- [ ] État persistant du monde
- [ ] Destruction persistante
- [ ] État écologique persistant
- [ ] Sauvegardes indépendantes par monde
- [ ] Création d'un nouveau monde sans supprimer les anciens

---

## PHASE 3+ : Vertical Slice et contenu

Prototype technique → vertical slice → contenu → expansion du monde → polish → optimisation → release.

Les systèmes de Phase 2 devront être validés avant de construire du contenu dépendant de leurs règles définitives.

---

**Dernière mise à jour** : 2026-08-21  
**Moteur** : Unreal Engine 5.8.1  
**Langage principal** : C++
