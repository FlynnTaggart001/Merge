# Merge — Gestion des terres et domaine noble

**Statut** : Conception validée  
**Lié à** : Q-005 — Devenir noble

## Vue d’ensemble

Lorsqu’un joueur obtient un titre de noblesse (via Q-005 ou autre moyen), il acquiert un **domaine**.  
Ce système permet de gérer les terres, les revenus, la population et les conséquences politiques liées au roi.

Le système doit rester léger (pas de micro-gestion lourde) tout en produisant des conséquences persistantes dans le monde non régénératif de Merge.

---

## Accès

- Disponible uniquement si le joueur possède un titre de noblesse.
- Le domaine est lié au titre obtenu (terres, villages, fermes, etc. du noble éliminé ou accordé).

---

## Fonctions de base

- Visualiser l’état du domaine (population, ressources, bâtiments, moral).
- Collecter les impôts / revenus du domaine.
- Décider d’investissements (agriculture, défense, infrastructures, bâtiments utiles).
- Gérer une milice / hommes d’armes locaux (nombre limité).
- Observer la satisfaction générale de la population (**Bonheur**).

---

## Système de Bonheur de la population

Le **Bonheur général** du peuple du domaine est une valeur entre 0 et 100 %.

### Règle critique liée au roi

- **Si le Bonheur reste sous 60 %** : situation stable vis-à-vis du roi.
- **Si le Bonheur atteint ou dépasse 60 %** : le roi considère le joueur comme un **opposant potentiel** (trop populaire / trop bon pour son peuple).

### Conséquences si Bonheur ≥ 60 %

- L’humeur du roi à l’égard du joueur devient **mauvaise**.
- Les négociations et conversations avec le roi (et sa cour proche) deviennent nettement plus difficiles.
- Des **assassins du roi** viennent rendre visite au joueur de temps en temps (menaces, tentatives d’élimination).
- Le roi peut chercher à reprendre le titre ou à nuire au domaine.

### Conception

Le joueur est donc encouragé à maintenir un équilibre :  
trop bien traiter son peuple = danger politique de la part du roi.  
Trop mal le traiter = risque de révolte locale / perte de revenus / réputation négative.

---

## Interactions avec le roi

- Le roi peut exiger des impôts supplémentaires, des troupes, ou des services.
- Un roi mécontent (Bonheur ≥ 60 %) rend les dialogues et négociations plus durs (prix plus élevés, refus plus fréquents, menaces).
- Le système d’assassins royaux est le même que celui déclenché en cas de refus dans Q-005.

---

## Conséquences persistantes

- État du domaine sauvegardé avec le monde.
- Population, bâtiments et moral évoluent selon les décisions du joueur et les événements mondiaux.
- La mort du joueur ou la perte du titre peut entraîner la redistribution du domaine (selon les règles du royaume).

---

## Notes d’implémentation

- Le système doit s’intégrer au WorldState et aux factions.
- Pas de micro-gestion excessive : les décisions sont stratégiques et ont des effets visibles à moyen/long terme.
- Le seuil de 60 % de Bonheur est une valeur de conception actuelle (ajustable plus tard).
