# Changelog

Tous les changements notables du projet sont documentés dans ce fichier. Le format suit [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) et le projet s'inspire de [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Documentation — roadmap and combat audit (2026-10-15)
- Removed the superseded probabilistic combat-resolution model from `docs/gameplay/COMBAT_RESOLUTION.md`, replacing it with a redirect to the canonical real-time combat and weapon specifications.
- Corrected `specs/COMBAT_AND_EFFECTS.md` so data-driven attack definitions do not permit un-parryable attacks by default.
- Updated `ROADMAP.md` to separate specified combat rules from pending design decisions and Unreal validation.
- Clarified the base cost of 10 endurance per blocked impact; heavy-armor stamina surcharge is approved in principle, with exact coefficients still pending.
- Reaffirmed `specs/COMBAT_SYSTEM_SPEC.md` as the single canonical combat specification; the old `docs/gameplay/COMBAT_RESOLUTION.md` content is removed and the file now redirects to canonical rules.
- Updated weapon base damage by family (unarmed remains open) and synchronized `GAME_BIBLE.md`, `ROADMAP.md`, `docs/CONSISTENCY_AUDIT.md`, `specs/GAMEPLAY_SYSTEMS_MASTER_SPEC.md`, and `specs/COMBAT_AND_EFFECTS.md`; removed the superseded combat model.

### Changed — AI toolchain selected (2026-10-13)
- Official Merge AI tools are now **ChatGPT Plus, Claude Code, and Wingman Premium** only.
- Added ai/TOOLCHAIN.md as the canonical responsibility, cost, and handoff guide.
- Clarified that ChatGPT Plus does not include OpenAI API credits and that Wingman is not assumed to have GitHub access.
- Removed unused provider API-key placeholders from the example environment files and removed unselected providers from default runtime routing.
- Automatic Claude Code runtime wiring and Wingman-to-GitHub handoff remain validation tasks; they are not claimed as complete.

### Changed — Character creation update (2026-10-07)
- Character creation now offers a **Homme / Femme** sex choice.
- The creation pool is reduced from **26 to 20 characteristic points**.
- All 6 characteristics still start at **6/20** and remain capped at **14/20** during creation.
- The initial characteristic pool is now **56 points** (6 × 6 + 20).
- Initial skills remain automatically derived from the final characteristic profile.
 - CHANGELOG.md

Tous les changements notables du projet sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
le projet suit [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Fixed — Canonical design synchronization (2026-09-22)
- Synchronized `GAME_BIBLE.md`, `ROADMAP.md`, progression specifications and gameplay master documentation with the current **attribute-first character creation** model.
- Character creation is now consistently documented as **6/20 base in each of 6 characteristics + 26 points to distribute, maximum 14/20**.
- Removed the obsolete creation model based on **45 skills at 5 + 30 specialization points** from current specifications.
- Initial skill values are now consistently derived from the final characteristic profile using the canonical characteristic → skill conversion.
- Synchronized the Kima Vé government name to **Kiyeka**; the previous Kiyoka correction was itself erroneous.
- Synchronized world boundaries to **40 km² / 6.32 × 6.32 km** and the **eastern ocean** boundary.
- Removed obsolete `Domptage` / `Réflexe` progression architecture from current design documentation; Endurance remains a gameplay resource.
- Marked `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` as historical/superseded rather than allowing it to override the current canonical rules.


### Fixed — Progression consistency (2026-09-16)
- Synchronisé `ai/PROJECT_STATE.md` avec le baseline de progression du jour.
- Aligné `GAME_BIBLE.md` §07 et les systèmes dépendants sur le système canonique approuvé : **45 compétences + 6 caractéristiques**.
- Supprimé des règles actuelles toute progression indépendante de **Réflexe** ou **Domptage**.
- Clarifié que **Endurance** reste une ressource de gameplay et n'est pas une caractéristique canonique.
- Clarifié que les caractéristiques progressent automatiquement à partir de la progression validée des compétences.
- Clarifié que les classes/voies sont déterminées par le **profil de caractéristiques**, avec notification et révélation du nom lorsqu'une voie devient accessible.
- Retiré de la documentation actuelle la condition non validée précédemment attribuée à **Déité** ; ses conditions restent à définir dans la future spécification des classes.
- Corrigé le multiplicateur d'Intelligence dans `specs/PROGRESSION_DESIGN_BASELINE_2026-09-16.md` pour l'échelle 0–20 (`0.75 + 0.025 × I`).

### Added — AI Team Orchestration
- End-to-end supervised workflow: objective → state → planning → dependencies → role → permissions → proposal → Devil's Advocate → review → QA → human gate → execution → handoff → state → follow-up tasks.
- AI-assisted task decomposition with strict JSON contract and safe fallback.
- Dependency graph validation and cycle detection.
- Deterministic role assignment and expanded provider routing.
- Least-privilege role permissions.
- Recommendation engine with `NO_CONCERN`, `SUGGESTION`, `REVIEW`, `PENDING_HUMAN`, `BLOCKED`.
- Confidence-based escalation and explicit human-decision escalation.
- Persistent recommendations, disagreements and structured handoffs.
- Human decision manager and explicit approval gate for critical/destructive/merge-level actions.
- Resumable machine-readable project state.
- Proactive project-health recommendations.
- CI coverage for recommendation and team-workflow contracts.

### Added — Gameplay & World Design
- Spécification `specs/GAMEPLAY_AND_PERSISTENT_WORLD.md` couvrant mouvement, accroupissement, roulade, furtivité, détection progressive et Backstab.
- Spécification d'un bestiaire à populations dynamiques avec reproduction, mortalité, prédation, ressources, migration et extinction locale.
- Règle fondamentale de monde non régénératif : les morts, destructions et suppressions définitives persistent.
- Architecture conceptuelle de persistance par monde et de plusieurs mondes indépendants.
- **Saut arrière**, **pas de côté**, franchissement contextuel, escalade contextuelle et réception contrôlée.
- Coûts d'**Endurance** data-driven pour les principaux efforts physiques : course/sprint, saut, roulade, bond arrière, pas de côté, franchissement et escalade.
- **Agilité** reliée aux actions de mobilité uniquement via les compétences canoniques concernées et leur progression validée.
- **Parade active** : timing précis, `CombatResolver`, attaques parables/non parables et fenêtre de riposte.
- Système de ciblage intelligent : priorité aux cibles proches, parcours des cibles valides et lock-on compatible mêlée/magie.
- Système de **groupe de PNJ** et de **magie collective** avec positionnement, synchronisation, mana, compatibilité et interruption.
- Système de **montures** avec acquisition auprès d'éleveurs ou acquisition naturelle selon les règles propres à l'espèce.
- Système de confiance/lien avec la monture et persistance de son état.
- Système aquatique : eau peu profonde, flottaison, nage, plongée, respiration et noyade.
- Flottabilité influencée par l'équipement : une armure lourde peut faire couler le personnage ou rendre la remontée difficile.
- Dégâts environnementaux : brûlure, chute, noyade, chaleur et dangers futurs.
- Système de faim, hydratation et **sommeil/fatigue** avec altérations physiologiques progressives.
- Nouvelle compétence **Médecine** pour diagnostic et soins non magiques.
- Système de **maladies régionales** dépendant du climat, de l'eau, de la faune, de l'hygiène et des événements du monde.
- Diagnostic diégétique : aucune maladie n'est révélée automatiquement par un texte ; diagnostic via médecin PNJ ou autodiagnostic selon la compétence Médecine.
- Maladies, besoins et récupération intégrés à la simulation probabiliste hors zone.
- **Système de saisons** : printemps, été, automne, hiver, transitions persistantes et profils saisonniers régionaux.
- Effets saisonniers sur climat, météo, écologie, reproduction, migrations, ressources, maladies et risques naturels.
- Excursions saisonnières des prédateurs influencées par disponibilité des proies, météo et pression écologique.
- Catastrophes naturelles : séismes, tornades, feux de forêt, foudre, pluies torrentielles, inondations, glissements de terrain, activité volcanique et coulées de lave.
- Interaction séisme → réveil volcanique probabiliste.
- Coulées de lave capables de suivre le relief, remplir certaines dépressions/ravins, créer des zones de danger et déclencher des incendies.
- Direction de world design à trois grandes régions : **Dark Fantasy**, **Light Fantasy** avec grande colline et lac d'altitude, et **Fantasy classique**.
- Hydrologie régionale : le lac d'altitude peut générer des ruissellements, torrents, débordements et inondations en aval.
- **Déplacements territoriaux des prédateurs** : territoire principal privilégié, excursions occasionnelles vers des zones voisines, retour probabiliste et distinction claire entre excursion et migration permanente.
- `specs/PERFORMANCE_AND_SIMULATION_SPEC.md` imposant la simulation probabiliste hors zone et la simulation détaillée locale.
- `specs/SYSTEM_INTEGRATION_MATRIX.md` pour contrôler les dépendances et éviter les contradictions entre systèmes.
- `specs/WORLD_REGIONS_HYDROLOGY_AND_THREATS_SPEC.md` pour la direction de la carte et les risques régionaux.
- `specs/SEASONALITY_AND_CYCLE_SPEC.md` pour le système de saisons et ses interactions avec le monde.

### Updated
- `docs/gameplay.md` consolidé avec mouvement, combat, ciblage, groupes, magie collective, progression, survie, Médecine, maladies, montures, aquatique, catastrophes et structure du monde.
- `docs/architecture.md` aligné sur les nouveaux systèmes, les saisons et leur ordre d'implémentation.
- `docs/world.md` maintient la règle de monde persistant/non régénératif, les territoires de prédateurs, les excursions et la simulation régionale hors zone.
- `specs/REGIONAL_PROBABILISTIC_SIMULATION_SPEC.md` définit les territoires principaux des prédateurs, leurs excursions occasionnelles, leur influence saisonnière et leur matérialisation locale cohérente.
- Les spécifications spécialisées restent data-driven et n'enferment pas encore les domaines magiques, espèces de montures, chiffres d'équilibrage ou contenu définitif.
- Les nouveaux systèmes sont spécifiés mais ne sont pas déclarés comme implémentés.
- Engine version standardized to **Unreal Engine 5.8.1** across project configuration and documentation.
- AI collaboration rules are now backed by runtime enforcement rather than documentation alone.

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

### [0.0.4] - 2026-08-20

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

**Dernière mise à jour** : 2026-10-15
