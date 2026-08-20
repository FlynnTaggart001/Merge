# Development Roadmap - ROADMAP.md

## Vue d'ensemble

Cette roadmap définit les grandes phases de développement de **Merge**, du projet de préproduction jusqu'à la release.

Le développement est piloté par le Game Director et peut être exécuté par le système multi-agents défini dans `/ai/`.

---

## PHASE 0 : Préproduction

**Statut : 🟢 QUASI TERMINÉE**

### Terminé
- [x] Structure initiale du dépôt
- [x] Vision du jeu (`GAME_BIBLE.md`)
- [x] Règles de collaboration (`AI_RULES.md`)
- [x] Architecture technique initiale (`specs/TECHNICAL_ARCHITECTURE.md`)
- [x] Moteur choisi : Unreal Engine 5
- [x] Langage principal choisi : C++

### Restant
- [ ] Finaliser les systèmes encore marqués « À DÉCIDER »
- [ ] Mettre en place l'infrastructure de développement multi-agents
- [ ] Valider les décisions critiques restantes avec le Game Director

### Critères de sortie
- Vision validée
- Architecture technique approuvée
- Infrastructure IA opérationnelle
- Décisions critiques identifiées et tracées

---

## PHASE 0.5 : Infrastructure de développement IA

**Statut : 🟡 EN COURS**

### Objectif
Créer l'environnement permettant à plusieurs agents IA de collaborer sur Merge à partir d'un objectif unique donné par le Game Director.

### Tâches
- [ ] Créer `/ai/` et son protocole de collaboration
- [ ] Créer le registre des agents et capacités
- [ ] Créer le système de tâches et dépendances
- [ ] Créer le système de handoff
- [ ] Créer l'état partagé du projet
- [ ] Créer le système de reviews et validations
- [ ] Définir les niveaux de permission
- [ ] Définir les conditions d'escalade humaine
- [ ] Documenter le protocole d'orchestration

### Critères de sortie
- Un objectif unique peut être transformé en tâches
- Les tâches sont attribuables par rôle/capacité
- Les agents peuvent transmettre leur contexte au suivant
- Les résultats sont vérifiables
- Les blocages critiques remontent au Game Director

---

## PHASE 1 : Bootstrap Unreal Engine 5

**Statut : 🔴 À VENIR**

### Objectif
Créer le projet Unreal Engine 5 réel et établir le pipeline de développement C++.

### Tâches
- [ ] Créer le projet UE5
- [ ] Configurer le module C++ principal
- [ ] Mettre en place la structure `Source/Merge/`
- [ ] Configurer Git/LFS si nécessaire
- [ ] Configurer le build et les configurations de développement
- [ ] Mettre en place les conventions Unreal définies dans la spécification
- [ ] Créer une scène de test minimale
- [ ] Valider le pipeline de compilation

### Dépendances
- Phase 0
- Phase 0.5

### Critères de sortie
- Projet UE5 compilable
- Projet versionné
- Build reproductible
- Structure C++ conforme à la spécification

---

## PHASE 2 : Prototype Technique

**Statut : 🔴 À VENIR**

### Objectif
Démontrer les capacités techniques fondamentales de Merge.

### Tâches
- [ ] Joueur et déplacement
- [ ] Caméra troisième personne
- [ ] Esthétique PS1
- [ ] Chargement/streaming du monde de test
- [ ] UI basique
- [ ] Sauvegarde minimale
- [ ] Tests de performance

### Dépendances
- Phase 1

### Critères de sortie
- Personnage jouable
- Caméra fonctionnelle
- Direction visuelle PS1 validée
- Sauvegarde fonctionnelle
- Pas de crash critique

---

## PHASE 3 : Prototype Gameplay

**Statut : 🔴 À VENIR**

### Objectif
Valider les mécaniques fondamentales du RPG.

### Tâches
- [ ] Combat de base
- [ ] Magie simple
- [ ] Inventaire
- [ ] Équipement
- [ ] PNJ et dialogue simple
- [ ] Quête simple
- [ ] Progression

### Dépendances
- Phase 2

### Critères de sortie
- Combat temps réel jouable
- Une quête complète
- Progression visible
- Aucun bug critique bloquant

---

## PHASE 4 : Vertical Slice

**Statut : 🔴 À VENIR**

### Objectif
Créer une démonstration verticale complète de 30 à 60 minutes.

### Démonstration minimale
- Déplacement
- Caméra dynamique
- Combat
- Ennemi avec IA
- Armes/équipement
- Magie
- Inventaire
- Progression
- PNJ et routines
- Dialogues arborescents
- Une quête complète
- Village + forêt
- Esthétique PS1 cohérente
- Cycle jour/nuit

### Dépendances
- Phase 3

---

## PHASE 5 : Première Région Complète

**Statut : 🔴 À VENIR**

Développer une région complète avec lieux, PNJ, factions, quêtes, lore et économie.

### Critères de sortie
- Région entièrement jouable
- Contenu cohérent
- Équilibrage acceptable
- Au moins 10 heures de contenu visé

---

## PHASE 6 : Expansion du Monde

**Statut : 🔴 À VENIR**

Ajouter et connecter les régions supplémentaires, les systèmes de voyage et les ponts narratifs.

---

## PHASE 7 : Contenu

**Statut : 🔴 À VENIR**

Développer la campagne principale, les quêtes secondaires, le lore, les événements dynamiques et le contenu caché.

---

## PHASE 8 : Polish

**Statut : 🔴 À VENIR**

Raffiner visuels, animations, audio, UX, dialogues et équilibrage.

---

## PHASE 9 : Optimisation

**Statut : 🔴 À VENIR**

Profiling, performances, mémoire, taille du build et compatibilité avec les plateformes cibles.

---

## PHASE 10 : Release

**Statut : 🔴 À VENIR**

Tests finaux, build release, documentation utilisateur, plateformes et lancement.

---

## Jalons critiques

| Jalon | Phase | Impact |
|---|---:|---|
| Infrastructure IA opérationnelle | 0.5 | Permet le développement multi-agents autonome |
| Projet Unreal compilable | 1 | Valide le pipeline technique |
| Prototype technique | 2 | Valide la faisabilité technique |
| Prototype gameplay | 3 | Valide les mécaniques fondamentales |
| Vertical Slice | 4 | Valide la faisabilité de production |
| Première région | 5 | Valide la production de contenu à grande échelle |
| Monde complet | 6 | Valide l'ampleur du projet |
| Release | 10 | Lancement officiel |

---

## Règle d'avancement autonome

Le système multi-agents peut proposer et exécuter les tâches techniques nécessaires pour atteindre le prochain jalon, sous réserve des permissions définies dans `/ai/AI_ORCHESTRATOR.md`.

Une décision relevant du Game Director ne doit jamais être inventée par un agent. Elle doit être créée comme décision `PENDING_HUMAN` et bloquer uniquement les tâches qui en dépendent.

---

**Dernière mise à jour** : 2026-08-20  
**Statut** : Actif  
**Moteur** : Unreal Engine 5 — APPROUVÉ  
**Langage principal** : C++ — APPROUVÉ
