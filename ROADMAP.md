# Development Roadmap - ROADMAP.md

## Vue d'Ensemble

Ce document définit les grandes phases de développement du projet Merge, du concept initial jusqu'à la release finale.

Chaque phase a des objectifs clairs, des dépendances, et des critères de succès.

---

## PHASE 0 : Préproduction

**Durée estimée** : À DÉCIDER
**Statut** : 🟢 EN COURS

### Objectif
Préparer le terrain pour le développement.

### Tâches
- [x] Créer la structure du dépôt
- [x] Définir la vision du jeu (GAME_BIBLE.md)
- [x] Établir les règles de collaboration (AI_RULES.md)
- [ ] Créer un document de design détaillé
- [ ] Valider les systèmes clés avec le Game Director
- [ ] Planifier les phases suivantes

### Dépendances
Aucune

### Critères de Succès
- Documentation complète et accessible
- Tous les systèmes principaux définis
- Accord sur la vision générale
- Prêt à passer à la Phase 1

---

## PHASE 1 : Choix du Moteur

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 EN ATTENTE DE DÉCISION

### Objectif
Sélectionner et mettre en place l'infrastructure technique.

### Tâches
- [ ] Évaluer les options (Unity, Godot, Unreal, Bevy, custom, etc.)
- [ ] Prendre une décision officielle
- [ ] Mettre en place le projet de base
- [ ] Configurer le pipeline de build
- [ ] Tester l'esthétique PS1 avec le moteur choisi
- [ ] Mettre en place Git et versioning

### Dépendances
- Phase 0 complétée

### Critères de Succès
- Moteur choisi et justifié
- Projet de base fonctionnel
- Esthétique PS1 testée et validée
- Pipeline de dev fonctionnel

### Points de Décision Clés
- **À DÉCIDER** : Quel moteur de jeu ?
- **À DÉCIDER** : Quel langage de programmation ?
- **À DÉCIDER** : Plateforme cible (PC, console, etc.) ?

---

## PHASE 2 : Prototype Technique

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Démontrer les capacités techniques de base.

### Tâches
- [ ] Implémentation du joueur et déplacement
- [ ] Caméra troisième personne
- [ ] Système d'esthétique PS1
- [ ] Chargement du monde basique
- [ ] UI basique (menu, HUD)
- [ ] Gestion de la sauvegarde
- [ ] Tests de performance

### Dépendances
- Phase 1 complétée
- Moteur choisi et configuré

### Critères de Succès
- Personnage jouable et déplaçable
- Caméra fonctionnelle
- Esthétique PS1 appliquée
- Pas de crashes

---

## PHASE 3 : Prototype Gameplay

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Tester les mécaniques essentielles du RPG.

### Tâches
- [ ] Combat de base (attaque légère/lourde)
- [ ] Magie simple (2-3 sorts)
- [ ] Inventaire basique
- [ ] Équipement fonctionnel
- [ ] PNJ avec dialogue simple
- [ ] Quête simple
- [ ] Système de progression

### Dépendances
- Phase 2 complétée

### Critères de Succès
- Combat temps réel fonctionnel
- Une quête complète du début à la fin
- Progression visible
- Pas de bugs critiques

---

## PHASE 4 : Vertical Slice

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Créer une démo verticale complète et jouable.

### Le Vertical Slice Doit Démontrer
- [x] Déplacement du personnage
- [ ] Caméra dynamique fonctionnelle
- [ ] Combat (attaque, esquive, parade)
- [ ] Ennemi avec IA basique
- [ ] Armes et équipement fonctionnels
- [ ] Magie (au moins 2-3 sorts)
- [ ] Inventaire complet
- [ ] Compétences et progression
- [ ] PNJ avec routine
- [ ] Dialogues arborescents
- [ ] Une quête simple du début à la fin
- [ ] Une petite zone explorée (village + forêt)
- [ ] Esthétique PS1 validée
- [ ] Cycle jour/nuit

### Dépendances
- Phase 3 complétée
- Tous les systèmes de base en place

### Critères de Succès
- Démo jouable de 30-60 minutes
- Tous les systèmes clés fonctionnels
- Esthétique PS1 cohérente
- Aucun crash bloquant
- Gameplay fluide

### Durée Estimée
À DÉCIDER

---

## PHASE 5 : Première Région Complète

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Développer une région entière jouable.

### Tâches
- [ ] Définir la première région (géographie, lieux)
- [ ] Implémenter tous les lieux principaux
- [ ] Créer des quêtes pour la région
- [ ] Mettre en place les factions de la région
- [ ] Balancer le contenu
- [ ] Remplir de PNJ et dialogues
- [ ] Ajouter lore et détails

### Dépendances
- Phase 4 complétée

### Critères de Succès
- Région entière jouable
- Contenu varié et engageant
- 10+ heures de gameplay
- Équilibrage acceptable

---

## PHASE 6 : Expansion du Monde

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Ajouter des régions supplémentaires.

### Tâches
- [ ] Développer 2-3 régions additionnelles
- [ ] Connecter les régions de manière logique
- [ ] Implémenter le système de voyage
- [ ] Ajouter du contenu pour chaque région
- [ ] Créer des ponts narratifs

### Dépendances
- Phase 5 complétée

### Critères de Succès
- Monde interconnecté fonctionnel
- 30+ heures de gameplay
- Aucune région isolée

---

## PHASE 7 : Contenu

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Remplir le monde de quêtes, lore et détails.

### Tâches
- [ ] Quêtes principales (main storyline)
- [ ] Quêtes secondaires
- [ ] Livres et journaux
- [ ] Légendes et lore
- [ ] Événements dynamiques
- [ ] Contenu caché

### Dépendances
- Phase 6 complétée

### Critères de Succès
- Monde riche en contenu
- 50+ heures de gameplay
- Histoire cohérente

---

## PHASE 8 : Polish

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Raffiner l'expérience globale.

### Tâches
- [ ] Améliorer l'esthétique visuelle
- [ ] Animations supplémentaires
- [ ] Effets sonores et musique
- [ ] Raffinement des dialogues
- [ ] Correction des bugs visuels
- [ ] Équilibrage final
- [ ] UX improvements

### Dépendances
- Phase 7 complétée

### Critères de Succès
- Jeu visuellement cohérent
- Aucun glitch visuel visible
- Audio immersif

---

## PHASE 9 : Optimisation

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Assurer performance et stabilité.

### Tâches
- [ ] Optimisation des performances
- [ ] Réduction de la taille du jeu
- [ ] Tests de compatibilité
- [ ] Profiling et debugging
- [ ] Optimisation mémoire
- [ ] Tests sur configurations variées

### Dépendances
- Phase 8 complétée

### Critères de Succès
- FPS stable sur cible
- Taille acceptable
- Aucune fuite mémoire

---

## PHASE 10 : Release

**Durée estimée** : À DÉCIDER
**Statut** : 🔴 À VENIR

### Objectif
Préparer le lancement.

### Tâches
- [ ] Tests finaux complets
- [ ] Build de release
- [ ] Documentation utilisateur
- [ ] Configuration des plateformes
- [ ] Préparation du marketing
- [ ] Lancement officiel

### Dépendances
- Phase 9 complétée

### Critères de Succès
- Jeu stable et jouable
- Documentation complète
- Lancement réussi

---

## Jalons Critiques

| Jalon | Phase | Impact |
|-------|-------|--------|
| **Moteur choisi** | 1 | Détermine toute l'architecture technique |
| **Vertical Slice complété** | 4 | Valide que le projet est réalisable |
| **Première région complète** | 5 | Démontre la capacité à créer du contenu |
| **Monde entier** | 6 | Fixe l'ampleur finale |
| **Release** | 10 | Lancement officiel |

---

## Dépendances Entre Phases

```
Phase 0 (Préproduction)
    ↓
Phase 1 (Choix du moteur)
    ↓
Phase 2 (Prototype technique)
    ↓
Phase 3 (Prototype gameplay)
    ↓
Phase 4 (Vertical Slice)
    ↓
Phase 5 (Première région)
    ↓
Phase 6 (Expansion du monde)
    ↓
Phase 7 (Contenu)
    ↓
Phase 8 (Polish)
    ↓
Phase 9 (Optimisation)
    ↓
Phase 10 (Release)
```

---

## Notes Importantes

- Les phases peuvent se chevaucher partiellement
- Les estimations de durée dépendent des ressources
- Chaque phase demande validation du Game Director avant de procéder
- Les phases peuvent être ajustées selon les découvertes techniques
- Les retours peuvent nécessiter du travail de phase précédente

---

**Dernière mise à jour** : 2026-08-19
**Statut** : Actif
**Prochaine décision** : Choix du moteur de jeu
