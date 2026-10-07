# Development Roadmap - ROADMAP.md

## Vue d'ensemble

Cette roadmap définit les grandes phases de développement de **Merge**. Une mécanique documentée n'est considérée comme implémentée que lorsque son prototype Unreal fonctionne et passe les tests correspondants.

---

## PHASE 0 : Préproduction

**Statut : 🟢 TERMINÉE**

- [x] Structure dépôt, GAME_BIBLE, AI_RULES, architecture, UE5 + C++
- [x] Principes fondamentaux de gameplay et du monde persistant spécifiés
- [x] Furtivité, Backstab, mouvement et combat cadrés architecturalement
- [x] Écosystème prédateur/proie et populations dynamiques spécifiés
- [x] Monde non régénératif et multi-mondes spécifiés
- [x] Ciblage, groupe et magie collective spécifiés
- [x] Système de montures spécifié (acquisition, confiance, comportement)
- [x] Survie, sommeil, Médecine et maladies régionales spécifiés
- [x] Système aquatique et dégâts environnementaux spécifiés
- [x] Catastrophes naturelles, volcan et hydrologie spécifiés
- [x] Simulation probabiliste hors zone et contraintes de performance spécifiées
- [x] Matrice d'intégration inter-systèmes créée
- [x] Direction de world design en trois grandes régions cadrée
- [x] Taille cible du monde fixée à 40 km² (référence 6,32 × 6,32 km)
- [x] Système canonique de progression : 46 compétences + 6 caractéristiques
- [x] Création : sexe Homme/Femme ; 6 caractéristiques à 6/20, 20 points à distribuer, maximum 14/20 ; compétences initiales dérivées automatiquement
- [x] Learning by Doing et progression automatique des caractéristiques spécifiés
- [x] Classes/voies : qualification par profil de caractéristiques et révélation à l'atteinte des conditions
- [x] Système de réputation spécifié

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
- [x] Spécifications gameplay/world et performance ajoutées sans implémentation prématurée

### À valider en local
- [ ] Générer project files + compiler
- [ ] Créer BP_* + L_TestArena
- [ ] PIE : move / look / jump
- [ ] Valider la base caméra troisième personne
- [ ] Vérifier les budgets CPU/GPU/mémoire du prototype de base

---

## PHASE 2 : Prototype Gameplay Core

**Statut : ⚪ À VENIR**

### Mouvement & progression
- [ ] Marche / course / sprint
- [ ] Saut + coût d'Endurance
- [ ] Accroupissement
- [ ] Roulade + i-frames liées à la fenêtre défensive d'Esquive
- [ ] Bond arrière
- [ ] Pas de côté
- [ ] Franchissement contextuel
- [ ] Escalade contextuelle
- [ ] Réception contrôlée
- [ ] Implémenter le pipeline des **46 compétences**
- [ ] Implémenter la progression **Learning by Doing**
- [ ] Implémenter la progression automatique des **6 caractéristiques**
- [ ] Implémenter les seuils, poids et valeurs data-driven
- [ ] Implémenter la validation anti-farming
- [ ] Implémenter la détection des classes/voies à partir du profil de caractéristiques

### Furtivité & combat
- [ ] Perception / bruit / visibilité
- [ ] Détection progressive
- [ ] Backstab conditionnel
- [ ] CombatResolver / DamageContext
- [ ] Blocage
- [ ] Parade et riposte
- [ ] Esquive manuelle
- [ ] Maîtrises d'armes

### Ciblage & groupe
- [ ] TargetingSystem avec priorité aux cibles proches
- [ ] Cycle de cibles / lock-on
- [ ] PartySystem
- [ ] Formation et commandes de groupe
- [ ] GroupMagicSystem
- [ ] Synchronisation et interruption des rituels

### Survie, santé et maladies
- [ ] Faim / alimentation
- [ ] Hydratation
- [ ] Sommeil / fatigue
- [ ] Altérations physiologiques progressives
- [ ] Médecine non magique
- [ ] Diagnostic joueur / médecin PNJ
- [ ] Maladies régionales et symptômes
- [ ] Incubation / transmission / traitement

### Eau & environnement proche
- [ ] Eau peu profonde
- [ ] Flottaison
- [ ] Nage
- [ ] Plongée / respiration
- [ ] Noyade
- [ ] Dégâts de chute
- [ ] Brûlure / chaleur

### Montures
- [ ] Système de montée / descente
- [ ] Acquisition auprès d'éleveurs
- [ ] Acquisition naturelle selon compatibilité de l'espèce
- [ ] Confiance et comportement
- [ ] Endurance / mouvement de monture
- [ ] Interactions terrain / eau / dangers
- [ ] Combat monté si retenu

---

## PHASE 2B : Monde systémique

**Statut : ⚪ À VENIR**

### Écologie & populations
- [ ] Définitions d'espèces
- [ ] Populations abstraites
- [ ] Reproduction
- [ ] Mortalité
- [ ] Prédateur / proie
- [ ] Ressources et capacité écologique
- [ ] Migration
- [ ] Extinction locale
- [ ] Résolution probabiliste hors zone

### Monde naturel
- [ ] Temps / météo
- [ ] Hydrologie
- [ ] Tremblements de terre
- [ ] Tornades
- [ ] Feux de forêt
- [ ] Foudre / tonnerre
- [ ] Pluies torrentielles
- [ ] Inondations
- [ ] Glissements de terrain
- [ ] Volcan / réveil probabiliste
- [ ] Coulées de lave et zones de danger

### Monde & sociétés
- [ ] Factions et réputation
- [ ] PNJ réactifs
- [ ] Quêtes réactives au WorldState
- [ ] Ressources régionales
- [ ] Conséquences écologiques des catastrophes et actions du joueur

### Persistance
- [ ] État persistant du monde
- [ ] Destruction persistante
- [ ] Terrain modifié persistant
- [ ] État écologique persistant
- [ ] Sauvegardes indépendantes par monde
- [ ] Création d'un nouveau monde sans supprimer les anciens

---

## PHASE 3 : Vertical Slice

**Statut : ⚪ À VENIR**

- [ ] Boucle jouable complète
- [ ] Une zone Dark Fantasy avec volcan
- [ ] Une zone Light Fantasy avec colline et lac d'altitude
- [ ] Une zone Fantasy classique de transition
- [ ] Combat + progression + survie + monde persistant
- [ ] Première magie collective
- [ ] Première famille de montures
- [ ] Première maladie régionale
- [ ] Première catastrophe systémique

---

## PHASE 4 : Monde complet & contenu

**Statut : ⚪ À VENIR**

Prototype technique → contenu → expansion du monde → quêtes/factions → polish → optimisation → release.

---

## PHASE 5 : Performance & Release

**Statut : ⚪ À VENIR**

- [ ] Profiling continu CPU/GPU/mémoire
- [ ] Tests de montée en charge
- [ ] Validation World Partition / streaming
- [ ] Validation simulation probabiliste hors zone
- [ ] Optimisation IA / physique / VFX
- [ ] Tests de sauvegarde sur monde fortement modifié
- [ ] Validation matériel cible
- [ ] QA finale

---

**Dernière mise à jour** : 2026-10-02  
**Moteur** : Unreal Engine 5.8.1  
**Langage principal** : C++