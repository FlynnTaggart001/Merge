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
| QA | tests, régressions, validation | Non |
| DOCUMENTATION | docs, cohérence, changelog | Non |
| RELEASE | build, packaging, release | Non |

## Règles

1. Un rôle décrit une capacité, pas une marque d'IA.
2. Plusieurs agents peuvent fournir le même rôle.
3. Un agent peut fournir plusieurs rôles.
4. L'orchestrateur sélectionne l'agent disponible selon la capacité requise.
5. Les informations de connexion et secrets ne doivent jamais être stockés dans Git.
6. Les agents indisponibles doivent être marqués comme tels plutôt que simulés.

## Agents actuels

À compléter automatiquement lorsque les intégrations réelles sont configurées.
