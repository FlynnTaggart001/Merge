# Résolution des actions de combat — Merge

**Statut : REMPLACÉ — 2026-10-15.**

Ce document ne définit plus de règles de combat. Son ancien modèle probabiliste d'opposition attaque/esquive/blocage et ses exemples numériques sont retirés, car ils contredisaient les décisions plus récentes du projet.

La référence canonique unique est **[`specs/COMBAT_SYSTEM_SPEC.md`](../../specs/COMBAT_SYSTEM_SPEC.md)**, complétée par **[`specs/WEAPONS_AND_EQUIPMENT_SPEC.md`](../../specs/WEAPONS_AND_EQUIPMENT_SPEC.md)** pour les dégâts, armes, armures, durabilité et équipement.

Règles actuelles à respecter :
- Combat en temps réel à la troisième personne.
- Parade active fondée sur le timing ; toutes les attaques sont parables par défaut, avec fenêtres plus courtes pour les attaques lourdes/spéciales lorsque spécifié.
- Blocage, parade et esquive sont des mécaniques distinctes.
- Les dégâts physiques suivent la formule canonique et les valeurs de base par famille définies dans la spécification d'équipement.
- Le stagger ne se déclenche que si les dégâts finaux dépassent strictement la résistance calculée de la cible.
- Seuls un coup critique, un stagger réussi ou une attaque chargée à 100 % peuvent interrompre une attaque ou briser une défense ; un bris de défense ne provoque pas automatiquement un stagger.
- Les coûts, fenêtres, formules et exceptions doivent provenir des spécifications canoniques ; aucune ancienne formule de ce fichier ne doit être réutilisée.

Les paramètres encore ouverts et les validations de prototype sont suivis dans [`docs/CONSISTENCY_AUDIT.md`](../CONSISTENCY_AUDIT.md) et [`ROADMAP.md`](../../ROADMAP.md). Ne pas recréer de spécification de combat concurrente.
