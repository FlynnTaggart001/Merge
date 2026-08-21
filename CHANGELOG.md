# Changelog - CHANGELOG.md

Tous les changements notables du projet sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
le projet suit [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added — Gameplay & World Design
- Spécification `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md` couvrant mouvement, accroupissement, roulade, furtivité, détection progressive et Backstab.
- Spécification d'un bestiaire à populations dynamiques avec reproduction, mortalité, prédation, ressources, migration et extinction locale.
- Règle fondamentale de monde non régénératif : les morts, destructions et suppressions définitives persistent.
- Architecture conceptuelle de persistance par monde et de plusieurs mondes indépendants.
- **Saut arrière** intégré au système commun d'esquive/mobilité.
- **Réflexe de combat** ajouté comme progression distincte de l'Agilité, basée sur l'expérience de combat réelle.
- Le Réflexe peut déclencher une **esquive automatique probabiliste** lorsque les conditions de combat le permettent, sans remplacer l'esquive manuelle.
- **Parade active** ajoutée au système de combat : timing précis, résolution via le CombatResolver et possibilité de créer une fenêtre de riposte.
- Distinction explicite entre blocage, parade et esquive.
- Attaques parables/non parables prévues comme données de combat.
- Documentation `docs/gameplay.md`, `docs/world.md` et spécifications de progression/combat mises à jour.

### Updated
- Roadmap enrichie avec les nouveaux systèmes de gameplay, d'écologie et de persistance.
- Les nouveaux systèmes sont spécifiés mais ne sont pas déclarés comme implémentés.
- Engine version standardized to **Unreal Engine 5.8.1** across project configuration and documentation.

### Phase 1 (in progress on local machines)
- UE5 scaffold created; compile/PIE must be validated with Unreal Editor.

---

## [0.1.0] - 2026-08-20

### Added — UE5 Foundation scaffold
- `Merge.uproject` (EngineAssociation 5.8.1)
- C++ module `Merge` with Core + Character foundation
- Classes: `UMergeGameInstance`, `AMergeGameMode`, `AMergePlayerController`, `AMergeCharacter`
- Config: DefaultEngine, DefaultGame, DefaultInput, DefaultGameplayTags
- Enhanced Input dependency
- Content layout + setup guide (`docs/UE5_SETUP.md`, `Content/README.md`)
- Updated `.gitignore` for UE5

### Status
- Source tree ready.
- **Compilation and PIE not verified in CI environment** (no Unreal installed).
- Local checklist required before claiming Phase 1 complete.

---

## [0.0.6] - 2026-08-20

### Security / Runtime
- Central orchestrator: all calls go through `Orchestrator.execute()`.
- Token limits runtime (`token_limits.py`): max input/output/task/session before provider call.
- Retry + exponential backoff + jitter (`retry.py`).
- Circuit breaker wired into the pipeline.
- Fail-closed on validation, tokens, budget, rate limit and open circuit.

### Tests
- 12 offline integration tests (`ai/tests/test_orchestrator_pipeline.py`).

### CI
- GitHub Actions: `ai-runtime.yml` (unit + integration + secrets hygiene).

### Status
- Phase 0.5 P0: **COMPLETE**.

---

## [0.0.5] - 2026-08-20

### Security
- Rate limiter (`ai/runtime/rate_limiter.py`).
- Circuit breaker (`ai/runtime/circuit_breaker.py`).
- Budget guard + cost tracker.

### Tests
- Deterministic tests for rate limiter and circuit breaker.

---

## [0.0.4] - 2026-08-20

### Security
- Secrets policy, `.gitignore`, `.env.example`.

---

## [0.0.3] - 2026-08-20

### Changed
- Engine: Unreal Engine 5.8.1 approved.

---

## [0.0.2] - 2026-08-19

### Added
- AI_RULES, ROADMAP, CHANGELOG, collaboration structure.

---

## [0.0.1] - 2026-08-18

### Added
- Initial repo, README, GAME_BIBLE.

---

**Dernière mise à jour** : 2026-08-21
