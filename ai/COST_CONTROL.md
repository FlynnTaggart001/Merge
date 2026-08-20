# Merge — AI Cost & Token Control

**Statut : APPROUVÉ — garde-fous pré-API**  
**Date : 2026-08-20**

## Objectif

Empêcher qu'une erreur d'orchestration, une boucle d'agents ou une requête excessive entraîne une consommation incontrôlée.

## Limites par défaut

| Limite | Valeur initiale |
|---|---:|
| Requêtes/minute | 30 |
| Requêtes/heure | 500 |
| Requêtes concurrentes | 4 |
| Timeout | 60 s |
| Retries | 2 |
| Input max/requête | 12 000 tokens |
| Output max/requête | 4 000 tokens |
| Tokens max/tâche | 20 000 |
| Tokens max/session | 100 000 |
| Budget max/tâche | 1 USD |
| Budget max/session | 10 USD |
| Budget max/jour | 25 USD |

Ces valeurs sont des **garde-fous initiaux**, pas une estimation du prix réel des fournisseurs.

## Hiérarchie des limites

Une requête doit respecter simultanément :

1. limite fournisseur ;
2. limite globale ;
3. limite de tâche ;
4. limite de session ;
5. limite journalière ;
6. permission du rôle.

La limite la plus restrictive gagne.

## Budget estimé

Avant un appel, le système doit pouvoir estimer :

`coût estimé = coût input + coût output estimé`

Si l'estimation dépasse le budget restant, l'appel est refusé ou soumis à validation humaine selon la politique de l'orchestrateur.

## Comptabilité

Les compteurs doivent être séparés par :

- fournisseur ;
- modèle ;
- rôle ;
- agent ;
- task ID ;
- session ;
- jour.

## Boucles

Un agent ne peut pas déclencher une chaîne infinie. Chaque tâche possède un nombre maximal d'itérations/reviews. Une boucle dépassant ce plafond devient `BLOCKED` ou `FAILED` et remonte à l'orchestrateur.

## Après intégration des API

Les prix réels devront être configurés par fournisseur et modèle à partir de leurs tarifs officiels. Aucun prix codé en dur ne doit être présenté comme définitif avant cette configuration.
