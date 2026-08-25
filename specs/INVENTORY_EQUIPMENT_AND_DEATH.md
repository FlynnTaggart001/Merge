# Merge — Inventory, Equipment & Death Specification

**Statut** : APPROUVÉ — architecture
**Engine** : Unreal Engine 5.8.1

## Inventaire

L'inventaire est distinct de l'équipement et doit supporter :

- armes ;
- armures ;
- accessoires ;
- consommables ;
- matériaux ;
- objets de quête ;
- objets uniques et empilables.

## Équipement

Les emplacements restent extensibles :

```text
MainHand / OffHand
Head / Chest / Hands / Legs / Feet
Accessories[*]
```

Chaque objet est défini par des données. Poids, statistiques, effets et compatibilités peuvent être utilisés par les systèmes de gameplay.

## Mort du joueur

La mort du joueur ne réinitialise jamais automatiquement l'état du monde.

Les conséquences permanentes du monde restent sauvegardées. Les règles exactes de retour du joueur, perte/récupération d'objets et éventuelles pénalités seront décidées pendant le game design, mais l'architecture doit permettre plusieurs modèles sans restaurer le WorldState.

## Règles

1. Inventaire et équipement sont séparés.
2. Les objets sont data-driven.
3. Le monde persiste indépendamment de la mort du joueur.
4. Les règles de pénalité de mort restent ouvertes pour ne pas bloquer le prototype.
