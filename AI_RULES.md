# AI Collaboration Rules — Merge

## 1. Purpose

`AI_RULES.md` définit le protocole de collaboration entre les agents IA travaillant sur Merge.

L'objectif est de permettre à plusieurs agents de travailler comme **une seule équipe**, avec le dépôt GitHub comme source de vérité partagée.

Le Game Director (utilisateur) donne les objectifs de haut niveau. Les agents et l'orchestrateur déterminent ensuite les tâches nécessaires, leurs dépendances et les validations requises.

---

## 2. Autorité et source de vérité

Ordre d'autorité en cas de contradiction :

1. Décision explicite du Game Director
2. `GAME_BIBLE.md`
3. `specs/`
4. `docs/`
5. `/ai/DECISIONS.md`
6. Propositions et analyses individuelles des agents

Une proposition ne devient pas une décision simplement parce qu'elle a été écrite par une IA.

Les décisions critiques doivent être explicitement marquées `APPROVED` ou `PENDING_HUMAN`.

---

## 3. Rôles, pas modèles

Les responsabilités sont définies par **rôle et capacité**, et non par un modèle IA permanent.

Un même agent peut remplir plusieurs rôles et un rôle peut être assuré par plusieurs agents.

Rôles principaux :

- `ARCHITECT` — architecture technique, dépendances, intégration
- `PROGRAMMER` — implémentation C++ / Unreal Engine
- `GAMEPLAY_DESIGNER` — systèmes RPG, combat, magie, progression
- `WORLD_DESIGNER` — monde, régions, PNJ, lore, contenu
- `RESEARCHER` — recherche et comparaison de solutions
- `REVIEWER` — revue critique, architecture et code review
- `QA` — tests, régressions, bugs et validation
- `DOCUMENTATION` — documentation et cohérence du dépôt
- `RELEASE` — builds, packaging et préparation de release

Les agents réellement disponibles et leurs capacités sont enregistrés dans `/ai/AGENT_REGISTRY.md`.

---

## 4. Principe d'orchestration

Un utilisateur peut donner un objectif unique, par exemple :

> Développe le système de combat de Merge.

L'orchestrateur doit alors :

1. lire l'état du projet ;
2. lire les spécifications pertinentes ;
3. identifier les dépendances ;
4. décomposer l'objectif en tâches ;
5. sélectionner les rôles/agents adaptés ;
6. exécuter les tâches dans l'ordre approprié ;
7. valider les résultats ;
8. créer automatiquement les tâches suivantes ;
9. arrêter et escalader uniquement lorsqu'une décision humaine est nécessaire ou qu'un blocage ne peut pas être résolu automatiquement.

Aucun agent ne doit attendre inutilement que le Game Director lui indique manuellement la tâche suivante lorsqu'elle peut être déduite de l'état du projet.

---

## 5. Avant toute tâche

Chaque agent doit :

1. lire `AI_RULES.md` ;
2. lire les documents sources nécessaires ;
3. consulter `/ai/PROJECT_STATE.md` ;
4. consulter la tâche courante ;
5. vérifier les dépendances ;
6. inspecter l'état Git et les fichiers concernés ;
7. éviter de recréer ce qui existe déjà.

Une tâche ne doit pas être commencée si une dépendance critique est `BLOCKED`.

---

## 6. Contrat de tâche

Toute tâche orchestrée doit disposer au minimum de :

- `ID`
- `OBJECTIVE`
- `STATUS`
- `PRIORITY`
- `ROLE`
- `ASSIGNED_AGENT`
- `DEPENDENCIES`
- `CONTEXT`
- `INPUTS`
- `EXPECTED_OUTPUT`
- `ACCEPTANCE_CRITERIA`
- `VALIDATION`
- `CREATED_BY`
- `CREATED_AT`
- `UPDATED_AT`

Statuts autorisés :

`PENDING`, `READY`, `IN_PROGRESS`, `REVIEW`, `BLOCKED`, `FAILED`, `COMPLETED`, `CANCELLED`.

---

## 7. Handoff obligatoire

À la fin d'une tâche, l'agent doit fournir :

```text
TASK_ID
STATUS
SUMMARY
FILES_CHANGED
TESTS_RUN
TEST_RESULTS
DECISIONS
PROBLEMS_FOUND
WARNINGS
BLOCKERS
RECOMMENDED_NEXT_TASKS
```

Le handoff doit être exploitable par un autre agent sans conversation privée avec l'agent précédent.

---

## 8. Validation

« Terminé » ne signifie pas « l'agent affirme avoir terminé ».

Une tâche doit être validée par les critères appropriés :

- compilation ;
- tests unitaires ;
- tests d'intégration ;
- validation Unreal ;
- analyse statique ;
- inspection Git diff ;
- revue architecture ;
- validation documentaire ;
- tests de régression.

Une tâche qui échoue doit générer une correction ou être marquée `BLOCKED`.

---

## 9. Reviews croisées

Les changements importants doivent être revus par un agent différent de celui qui les a produits lorsque cela est possible.

Exemple :

```text
ARCHITECT
    ↓
PROGRAMMER
    ↓
REVIEWER
    ↓
PROGRAMMER (correction si nécessaire)
    ↓
QA
```

Limiter les boucles automatiques par un nombre maximal de tentatives défini par l'orchestrateur.

---

## 10. Décisions humaines

Une IA ne doit jamais inventer une décision qui relève du Game Director.

Si une information critique est inconnue, créer une décision :

`PENDING_HUMAN`

avec :

- le problème ;
- le contexte ;
- les options ;
- les avantages/inconvénients ;
- la recommandation de l'agent ;
- les tâches bloquées par cette décision.

Exemples : vision du jeu, changement majeur d'architecture, changement de moteur, suppression d'un système majeur, modification substantielle du scope.

---

## 11. Permissions

Les agents doivent appliquer le principe du moindre privilège.

Niveaux conceptuels :

- `L0_READ` — lecture/analyse
- `L1_DOCS` — documentation
- `L2_CODE` — code et tests
- `L3_COMMIT` — commits atomiques
- `L4_MERGE` — fusion de changements validés
- `L5_CRITICAL` — décisions/changements d'architecture critique, toujours humains par défaut

L'absence de permission ne doit jamais être contournée.

---

## 12. Git

Règles :

- petits commits atomiques ;
- messages descriptifs ;
- jamais écraser silencieusement le travail d'un autre agent ;
- inspecter les changements avant commit ;
- éviter les modifications non liées à la tâche ;
- documenter les changements importants ;
- utiliser branches/PR lorsque le niveau de risque le justifie.

---

## 13. Gestion des conflits

En cas de :

- conflit Git ;
- décisions contradictoires ;
- modifications concurrentes ;
- dépendance cassée ;
- architecture incompatible ;

l'agent doit arrêter la partie concernée, documenter le problème et demander une résolution via l'orchestrateur ou le Game Director selon la gravité.

Aucune correction silencieuse ne doit masquer un conflit critique.

---

## 14. Dépendances connues

Ces dépendances sont indicatives et doivent être vérifiées contre les spécifications actuelles avant exécution :

- Combat → Attributs, Compétences, Équipement, IA ennemis
- Magie → Attributs, Compétences, Ressource magique
- Quêtes → PNJ, Dialogues, Factions, Réputation
- Factions → Lore, Réputation, PNJ, Monde
- Inventaire → Équipement, Poids, Prix

L'orchestrateur doit pouvoir découvrir et compléter les dépendances plutôt que de considérer cette liste comme exhaustive.

---

## 15. Mise à jour de l'état

Après chaque tâche significative, l'état pertinent doit être mis à jour dans `/ai/PROJECT_STATE.md` et/ou les fichiers de tâches concernés.

L'état doit permettre à un nouvel agent de reprendre le travail après une interruption sans dépendre du contexte conversationnel précédent.

---

## 16. Règle de non-hallucination

Un agent ne doit jamais prétendre avoir :

- exécuté une commande qu'il n'a pas exécutée ;
- compilé un projet qu'il n'a pas compilé ;
- testé une fonctionnalité qu'il n'a pas testée ;
- modifié un fichier qu'il n'a pas modifié ;
- utilisé une API ou un autre agent auquel il n'a pas réellement accès.

Toute limitation d'environnement doit être explicitement signalée.

---

## 17. Compatibilité Merge

Les décisions actuellement approuvées comprennent :

- **Engine : Unreal Engine 5**
- **Langage principal : C++**
- **Blueprint : complémentaire**
- Direction artistique : PS1 low-poly 1996–1999
- Action-RPG troisième personne

Toute modification de ces choix nécessite une décision explicite du Game Director.

---

## 18. Sécurité, coûts et autonomie contrôlée

Les règles détaillées sont définies dans :

- `/ai/SECURITY.md`
- `/ai/COST_CONTROL.md`
- `/ai/ORCHESTRATION_PROTOCOL.md`
- `/ai/QA_GATE.md`

Règles obligatoires :

1. Aucun secret dans Git.
2. Les limites de tokens, coût, durée, concurrence et retries sont des plafonds durs.
3. L'agent ne peut jamais augmenter automatiquement une limite.
4. Une limite atteinte doit arrêter proprement la tâche ou déclencher l'escalade prévue.
5. Toute boucle d'agents/reviews possède un nombre maximal d'itérations.
6. Toute sortie IA externe est considérée comme une entrée non fiable et doit être validée avant exécution.
7. Les logs ne doivent jamais contenir de clés ou credentials.
8. Le système doit rester fonctionnel sans API afin de permettre les tests locaux des garde-fous.

---

## 19. Intégration des fournisseurs IA

Les fournisseurs réels sont configurés uniquement par l'environnement d'exécution. Les clés ne sont jamais enregistrées dans les fichiers du dépôt.

Avant chaque appel externe, l'orchestrateur doit vérifier :

- permission du rôle ;
- budget restant ;
- quota restant ;
- nombre de requêtes concurrentes ;
- timeout ;
- taille maximale du contexte ;
- état du circuit breaker.

Après l'appel, il doit enregistrer les métriques non sensibles nécessaires à l'audit : fournisseur, modèle, tâche, durée, tokens et statut lorsque disponibles.

---

## 20. Mise à jour

Ce document évolue avec le système d'orchestration. Toute règle ajoutée doit préserver la traçabilité, la sécurité, la cohérence du projet et l'autorité finale du Game Director.

**Dernière mise à jour : 2026-08-20**  
**Statut : EN VIGUEUR**
