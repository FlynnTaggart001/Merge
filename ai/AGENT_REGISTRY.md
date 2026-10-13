# Agent Registry

Ce fichier décrit les rôles et capacités nécessaires à l'équipe multi-agents. Les modèles réellement connectés sont renseignés par l'environnement d'orchestration.

| Role | Capacités principales | Modèle permanent ? |
|---|---|---|
| ARCHITECT | architecture, dépendances, intégration | Non |
| PROGRAMMER | C++, Unreal Engine, debugging | Non |
| GAMEPLAY_DESIGNER | combat, magie, progression, RPG | Non |
| WORLD_DESIGNER | monde, PNJ, quêtes, lore | Non |
| RESEARCHER | recherche, comparaison, documentation | Non |
| REVIEWER | critique, architecture, code review | Non |
| DEVIL_ADVOCATE | contradiction constructive, edge cases, alternatives, risques systémiques | Non |
| QA | tests, régressions, validation | Non |
| DOCUMENTATION | docs, cohérence, changelog | Non |
| RELEASE | build, packaging, release | Non |

## Règles

1. Un rôle décrit une capacité, pas une marque d'IA.
2. Plusieurs agents peuvent fournir le même rôle.
3. Un agent peut fournir plusieurs rôles.
4. L'orchestrateur sélectionne l'agent disponible selon la capacité requise.
5. `DEVIL_ADVOCATE` est un rôle de revue indépendante et ne possède jamais l'autorité d'approuver une décision critique.
6. Les informations de connexion et secrets ne doivent jamais être stockés dans Git.
7. Les agents indisponibles doivent être marqués comme tels plutôt que simulés.

## Outils retenus

La pile approuvée est définie dans [TOOLCHAIN.md](TOOLCHAIN.md) :

| Outil | Capacités à utiliser | Disponibilité |
|---|---|---|
| ChatGPT Plus | Architecture, conception gameplay/monde, recherche interactive, contradiction constructive, revue et documentation | Utilisation interactive ; aucune connexion API automatique présumée |
| Claude Code | Programmation, édition du dépôt, revue de code, tests disponibles, préparation des changements GitHub | Outil de travail sur le dépôt ; l'exécution réelle dépend de l'installation locale |
| Wingman Premium | Assistance Unreal Editor, Blueprints et itérations locales | Utilisation dans Unreal ; accès GitHub non présumé, handoff requis |

Aucun autre fournisseur IA n'est retenu pour le workflow actif. Les rôles ci-dessus sont des capacités de travail et ne signifient pas qu'un orchestrateur peut invoquer chaque outil automatiquement.

## État des intégrations

- [x] Choix des trois outils documenté.
- [x] Workflow de transfert vers GitHub défini.
- [ ] Connexion automatique de ChatGPT Plus à l'orchestrateur : non disponible ou non démontrée ; ne pas supposer une API.
- [ ] Connexion automatique de Wingman à GitHub ou à l'orchestrateur : non disponible ou non démontrée.
- [ ] Adaptateur Claude Code conforme à l'interface runtime et testé de bout en bout : à vérifier avant de déclarer l'orchestration réelle opérationnelle.
