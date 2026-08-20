# Changelog - CHANGELOG.md

Tous les changements notables du projet sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
le projet suit [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Décisions techniques
- ✅ **Moteur de jeu choisi : Unreal Engine 5**
- ✅ **Langage principal : C++**
- ✅ **Langage complémentaire : Blueprint (prototypage & UI)**
- ✅ **Architecture technique UE5 approuvée** (`specs/TECHNICAL_ARCHITECTURE.md`)

### Infrastructure IA
- ✅ Politique de sécurité et gestion des secrets (`ai/SECURITY.md`)
- ✅ Contrôle des tokens et coûts (`ai/COST_CONTROL.md`)
- ✅ Protocole d'orchestration (`ai/ORCHESTRATION_PROTOCOL.md`)
- ✅ Gate QA / Definition of Done (`ai/QA_GATE.md`)
- ✅ État partagé du projet (`ai/PROJECT_STATE.md`)
- ✅ `.gitignore` renforcé contre les secrets et fichiers locaux
- ✅ `.env.example` ajouté sans credentials réels
- 🟡 Implémentation runtime des quotas, circuit breaker et compteurs encore à faire

### À Venir
- Implémentation runtime de l'infrastructure IA
- Prototype technique Unreal Engine 5
- Systèmes de gameplay
- Contenu du monde

---

## [0.0.4] - 2026-08-20

### Security
- 🔐 Ajout d'une politique explicite de protection des secrets.
- 🔐 Interdiction de stocker clés API, tokens et credentials dans Git.
- 🔐 Ajout d'un `.gitignore` dédié Unreal Engine et environnement IA.

### Added
- 🤖 `ai/SECURITY.md`
- 💰 `ai/COST_CONTROL.md`
- 🔄 `ai/ORCHESTRATION_PROTOCOL.md`
- 🧪 `ai/QA_GATE.md`
- 📊 Renforcement de `ai/PROJECT_STATE.md`
- ⚙️ `.env.example` avec garde-fous initiaux.

### Changed
- 📝 `AI_RULES.md` renforcé avec règles de sécurité, quotas, coûts, retries, circuit breaker et autonomie contrôlée.
- 📝 `ROADMAP.md` mis à jour pour distinguer les fondations documentaires déjà établies de l'implémentation runtime restante.

### Status
- Phase 0.5 : fondations de l'infrastructure IA établies.
- API keys : non configurées volontairement.
- Aucun fournisseur IA externe requis pour poursuivre le travail de préparation.

---

## [0.0.3] - 2026-08-20

### Changed
- 🎮 **Choix définitif du moteur : Unreal Engine 5**
- 📝 Mise à jour du statut du projet : la Phase 1 « Choix du moteur » est désormais considérée comme complétée.
- 📝 Alignement du changelog avec `specs/TECHNICAL_ARCHITECTURE.md`.

### Status
- Préproduction en cours
- Documentation technique approuvée
- **Engine : Unreal Engine 5**
- Prêt pour la suite du développement technique et le prototype.

---

## [0.0.2] - 2026-08-19

### Added
- ✅ AI_RULES.md : Rôles et responsabilités des IA collaboratrices
- ✅ ROADMAP.md : Plan de développement complet en 10 phases
- ✅ CHANGELOG.md : Ce fichier (historique des changements)
- ✅ Structure complète du dépôt documentée
- ✅ Principes de collaboration multi-IA établis
- ✅ Jalons critiques définis

### Modified
- 📝 GAME_BIBLE.md : Intégration de la structure 30 sections complète
- 📝 README.md : Lien vers tous les documents centraux

### Status
- Préproduction en cours
- Documentation de base complète
- Prêt pour Phase 1 : Choix du moteur
- Système de collaboration multi-IA en place

---

## [0.0.1] - 2026-08-18

### Added
- ✅ Structure initiale du dépôt GitHub
- ✅ README.md : Documentation d'accueil du projet
- ✅ GAME_BIBLE.md : Vision complète du projet action-RPG PS1 style MediEvil
- ✅ Définiton de l'esthétique PS1 intentionnelle
- ✅ Systèmes principaux documentés
- ✅ Ambiance gothique et rétro établie

### Status
- Projet initialisé
- Vision générale définie
- Prêt pour phase de préproduction

---

## Conventions de Ce Changelog

### Types de Changements
- **Added** : Nouvelles fonctionnalités ou sections
- **Changed** : Changements à la fonctionnalité existante
- **Deprecated** : Fonctionnalité à venir mais pas encore active
- **Removed** : Fonctionnalité supprimée
- **Fixed** : Bugs correctifs
- **Security** : Changements de sécurité
- **Modified** : Modifications à la documentation existante

### Statuts de Développement
- 🟢 **EN COURS** : Actuellement en développement
- 🟡 **EN ATTENTE** : Bloqué ou en pause
- 🔴 **À VENIR** : Planifié mais pas commencé
- ✅ **COMPLÉTÉ** : Fini et testé
- 🔄 **EN RÉVISION** : Attente de feedback/validation

### Tickets Associés
Chaque entrée importante inclut une référence aux issues/PRs pertinentes.

---

**Dernière mise à jour** : 2026-08-20
**Responsable** : GitHub Copilot
**Vérifié par** : Game Director
