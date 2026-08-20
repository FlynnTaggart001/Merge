# Changelog - CHANGELOG.md

Tous les changements notables du projet sont documentés dans ce fichier.

Le format est basé sur Keep a Changelog et le projet suit Semantic Versioning.

---

## [Unreleased]

### Décisions techniques
- ✅ **Moteur de jeu choisi : Unreal Engine 5**
- ✅ **Langage principal : C++**
- ✅ **Langage complémentaire : Blueprint (prototypage & UI)**
- ✅ **Architecture technique UE5 approuvée** (`specs/TECHNICAL_ARCHITECTURE.md`)

### Infrastructure IA — hardening runtime
- ✅ Politique de sécurité et gestion des secrets (`ai/SECURITY.md`)
- ✅ Contrôle des tokens et coûts (`ai/COST_CONTROL.md`)
- ✅ Budget guard fail-closed (`ai/runtime/budget_guard.py`)
- ✅ Suivi d'usage/coûts (`ai/runtime/cost_tracker.py`)
- ✅ Rate limiter multi-fenêtres (`ai/runtime/rate_limiter.py`)
- ✅ Circuit breaker fournisseur (`ai/runtime/circuit_breaker.py`)
- ✅ **Hard token limits** input/output/total (`ai/runtime/token_budget.py`)
- ✅ **Orchestrateur runtime** avec dépendances, routage par rôle et garde-fous (`ai/runtime/orchestrator.py`)
- ✅ **Timeout réseau + retry borné + exponential backoff** (`ai/runtime/retry.py`, `ai/runtime/providers_api.py`)
- ✅ Tests déterministes des garde-fous (`ai/tests/test_runtime_guards.py`)
- ✅ **CI GitHub Actions** pour compilation, tests et détection basique de credentials (`.github/workflows/ai-runtime.yml`)

### Agents
- ✅ **Claude Code désigné comme agent d'implémentation principal** pour le rôle `PROGRAMMER` (`ai/AGENT_REGISTRY.md`)
- ✅ Périmètre Claude Code défini : Unreal Engine 5, C++, gameplay systems, outils, debugging, refactoring, intégration et tests
- ✅ Autorité Claude Code limitée à l'implémentation ; aucune autorité sur la vision, le Game Design ou les décisions critiques d'architecture
- ✅ Chaîne recommandée : Game Director → spécification approuvée → Claude Code → Review → Claude Code (corrections) → QA

### Validation
- ✅ Suite locale de validation des garde-fous exécutée sur une reconstruction isolée des modules concernés : **4 tests / 4 passés**.
- ⚠️ L'environnement d'exécution n'a pas permis de cloner le dépôt GitHub directement ; la validation locale ne constitue donc pas encore une exécution du checkout GitHub complet.
- 🟡 La CI GitHub est la source de vérité pour la validation du dépôt réel.

### API
- 🔒 **Aucune clé API réelle n'est nécessaire ou incluse.**
- 🔒 Le runtime reste utilisable en mode dry-run sans fournisseur externe.

### À venir
- Finaliser la validation CI du branch hardening.
- Après validation, fusionner l'infrastructure de hardening vers `main`.
- Puis seulement connecter les fournisseurs IA réels et leurs clés.
- Prototype technique Unreal Engine 5.

---

## [0.0.5] - 2026-08-20

### Security
- 🔐 Implémentation d'un rate limiter indépendant des fournisseurs.
- 🔐 Implémentation d'un circuit breaker fail-safe.
- 🔐 Conservation d'un budget guard fail-closed et d'un suivi d'usage/coûts dans le runtime IA.

### Tests
- 🧪 Ajout de tests déterministes pour les limites de requêtes.
- 🧪 Ajout de tests de bascule et récupération du circuit breaker.

### Architecture
- 📝 La Phase 0.5 distingue les garde-fous déjà implémentés de leur intégration finale dans l'orchestrateur.
- 📝 Les clés API restent volontairement absentes.

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
- 📊 `ai/PROJECT_STATE.md`
- ⚙️ `.env.example`

---

## [0.0.3] - 2026-08-20

### Changed
- 🎮 **Choix définitif du moteur : Unreal Engine 5**
- 📝 Phase 1 « Choix du moteur » considérée comme complétée.
- 📝 Alignement avec `specs/TECHNICAL_ARCHITECTURE.md`.

---

## [0.0.2] - 2026-08-19

### Added
- ✅ AI_RULES.md
- ✅ ROADMAP.md
- ✅ CHANGELOG.md
- ✅ Structure complète du dépôt documentée
- ✅ Principes de collaboration multi-IA établis
- ✅ Jalons critiques définis

---

## [0.0.1] - 2026-08-18

### Added
- ✅ Structure initiale du dépôt GitHub
- ✅ README.md
- ✅ GAME_BIBLE.md
- ✅ Direction artistique PS1
- ✅ Systèmes principaux documentés
- ✅ Ambiance gothique et rétro établie

---

**Dernière mise à jour** : 2026-08-20
**Statut** : Hardening runtime IA en validation CI
**Moteur** : Unreal Engine 5 — APPROUVÉ
**Langage principal** : C++ — APPROUVÉ
