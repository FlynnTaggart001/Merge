# Système de compétences — Merge

## 1. Objectif

Les compétences représentent les savoir-faire spécifiques du personnage. Elles sont distinctes des caractéristiques : une caractéristique représente une capacité générale, tandis qu'une compétence représente un domaine de pratique précis.

Le système suit le principe fondamental de **Merge** : progression par utilisation (*learning by doing*).

Une action peut développer une compétence ainsi qu'une ou plusieurs caractéristiques lorsque l'activité le justifie réellement.

## 2. Principes généraux

- Les compétences sont spécialisées et indépendantes les unes des autres.
- Les compétences utilisent une échelle de **0 à 100**.
- Le personnage progresse en pratiquant réellement la compétence concernée.
- **Seules les réussites accordent une progression de compétence.** Une tentative échouée accorde 0 progression.
- Il n'existe **aucune pénalité artificielle anti-répétition** : si le joueur réussit réellement plusieurs actions difficiles, chacune peut faire progresser la compétence.
- La difficulté et la complexité de l'action influencent la progression.
- La difficulté d'une action est **prédéfinie pour cette action ou cet objet**. Elle n'est pas automatiquement augmentée ou diminuée selon le niveau du personnage.
- Une action devenue trop facile par rapport au niveau actuel peut donner **0 progression**.
- La progression devient progressivement plus lente lorsque le niveau de compétence augmente.
- L'Intelligence accélère l'apprentissage, mais ne donne pas de progression sans pratique et ne garantit pas la réussite.
- Les compétences sont **permanentes** : elles ne diminuent pas simplement parce qu'elles ne sont pas utilisées.
- La valeur réelle d'une compétence est conservée avec des **décimales** en interne. L'interface peut afficher une valeur arrondie.
- Les compétences ne sont pas limitées par la classe actuelle du personnage.
- Les classes représentent une orientation et non une restriction définitive des savoir-faire.
- Les caractéristiques peuvent soutenir une compétence, mais ne la remplacent pas.

## 3. Nouvelle règle — déblocages de maîtrise

Contrairement aux **caractéristiques de base**, les **compétences** débloquent de nouvelles possibilités de gameplay à chaque dizaine de niveaux.

Les déblocages sont placés aux niveaux **10, 20, 30, 40, 50, 60, 70, 80, 90 et 100**.

Chaque compétence possède donc **10 déblocages de maîtrise**.

Ces déblocages représentent des techniques, actions, possibilités ou niveaux de maîtrise réellement nouveaux. Ils ne sont pas de simples bonus numériques du type « +5 % de dégâts ».

Principes :

- Une caractéristique comme Force 50 ne débloque pas automatiquement une capacité à 50.
- Une compétence comme Épée 50 peut en revanche débloquer une nouvelle technique d'épée.
- Les déblocages doivent rester cohérents avec la nature de la compétence.
- Un déblocage peut nécessiter les caractéristiques associées ou d'autres conditions particulières lorsqu'il est exceptionnel.
- Le niveau 100 représente la maîtrise maximale de la compétence, pas nécessairement une puissance magique ou surnaturelle.
- Les effets progressifs de la compétence continuent d'exister entre les paliers.

## 4. Échelle de difficulté

Chaque action pouvant faire progresser une compétence reçoit une difficulté prédéfinie sur une échelle de 0 à 100 :

| Niveau de difficulté | Valeur de référence |
|---|---:|
| Très facile | 10 |
| Facile | 25 |
| Moyenne | 50 |
| Difficile | 70 |
| Très difficile | 85 |
| Exceptionnelle | 100 |

Des valeurs intermédiaires peuvent être utilisées. Une difficulté supérieure à 100 peut être utilisée pour des situations exceptionnelles, mais la compétence reste plafonnée à 100.

## 5. Formule universelle de progression

La même formule est utilisée pour toutes les compétences.

On définit :

- `S` = niveau actuel de la compétence, de 0 à 100 ;
- `D` = difficulté prédéfinie de l'action ;
- `I` = Intelligence du personnage, de 0 à 100 ;
- `P` = progression accordée par une réussite.

Pour une action réussie :

```text
P = 0.9 × max(0, (D − S + 15) / 50) × 1 / (1 + 0.012 × S) × (0.75 + 0.005 × I)
```

```text
S_nouveau = min(100, S + P)
```

Une tentative échouée applique directement `P = 0`.

La progression devient plus lente avec le niveau, tandis que l'Intelligence accélère modérément l'apprentissage.

La compétence est stockée avec ses décimales en interne. L'interface peut afficher une valeur arrondie.

### Exemple — Crochetage

Un personnage possède Crochetage 80 : une serrure difficulté 25, 50 ou 70 ne lui apporte plus de progression ; une serrure difficulté 85 ou 100 peut encore lui en apporter.

## 6. Compétences et déblocages

### 6.1 Combat

#### Épée — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Enchaînement de deux attaques rapides |
| 20 | Frappe directionnelle après déplacement |
| 30 | Contre-attaque après une parade réussie |
| 40 | Enchaînement de trois attaques avec changement de direction |
| 50 | Frappe circulaire permettant de toucher plusieurs adversaires proches |
| 60 | Contre-attaque avancée immédiatement après une esquive parfaite |
| 70 | Enchaînement aérien avec reprise d'appui rapide |
| 80 | Désarmement technique sur une ouverture précise |
| 90 | Enchaînement expert combinant parade, déplacement et contre-attaque |
| 100 | Maîtrise ultime de l'épée : chaîne de techniques avancées sans rupture de rythme |

#### Hache — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Frappe lourde chargée |
| 20 | Frappe latérale après déplacement |
| 30 | Crochet de hache pour déséquilibrer un adversaire |
| 40 | Enchaînement lourd de deux frappes |
| 50 | Brise-garde contre une défense affaiblie |
| 60 | Frappe de rotation à forte amplitude |
| 70 | Contre lourd après esquive réussie |
| 80 | Désarmement par accrochage de l'arme adverse |
| 90 | Enchaînement expert de frappes lourdes et changements d'angle |
| 100 | Maîtrise ultime : utilisation complète de l'inertie de la hache pour des attaques dévastatrices |

#### Masse — Force

| Niveau | Déblocage |
|---:|---|
| 10 | Frappe lourde chargée |
| 20 | Frappe permettant de repousser un adversaire léger |
| 30 | Coup écrasant contre une garde affaiblie |
| 40 | Frappe au sol à courte portée |
| 50 | Capacité à étourdir sur une ouverture précise |
| 60 | Frappe capable de faire perdre l'équilibre à un adversaire lourd |
| 70 | Coup de rotation à grande puissance |
| 80 | Brise-garde avancé |
| 90 | Enchaînement de frappes lourdes sans perte majeure de contrôle |
| 100 | Maîtrise ultime : exploitation maximale de la puissance et du poids de l'arme |

#### Lance — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Estoc précis |
| 20 | Estoc après recul contrôlé |
| 30 | Balayage circulaire |
| 40 | Enchaînement estoc + balayage |
| 50 | Maintien d'une distance de combat efficace contre plusieurs adversaires |
| 60 | Contre-estoc après esquive |
| 70 | Rotation défensive autour du personnage |
| 80 | Désarmement par contrôle de la hampe |
| 90 | Enchaînement expert à longue portée |
| 100 | Maîtrise ultime : contrôle exceptionnel de la distance et des angles |

#### Dague — Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Attaque rapide depuis une garde basse |
| 20 | Double frappe rapprochée |
| 30 | Contre après esquive courte |
| 40 | Enchaînement rapide de plusieurs coups |
| 50 | Désengagement instantané après attaque |
| 60 | Frappe ciblée sur une ouverture précise |
| 70 | Transition fluide entre attaque et déplacement |
| 80 | Désarmement rapide sur une ouverture |
| 90 | Enchaînement expert à très courte distance |
| 100 | Maîtrise ultime : mobilité et précision maximales avec la dague |

#### Arme à deux mains — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Première technique de frappe chargée |
| 20 | Enchaînement de deux attaques lourdes |
| 30 | Frappe circulaire de grande amplitude |
| 40 | Changement d'orientation pendant une attaque |
| 50 | Brise-garde puissant |
| 60 | Contre-attaque après esquive avec arme lourde |
| 70 | Enchaînement avancé avec reprise d'appui rapide |
| 80 | Désarmement ou renversement par exploitation de l'arme |
| 90 | Enchaînement expert à très forte amplitude |
| 100 | Maîtrise ultime : contrôle exceptionnel d'une arme à deux mains malgré son inertie |

#### Arc — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Tir précis depuis une position stable |
| 20 | Tir rapide après déplacement |
| 30 | Tir sans arrêt complet du mouvement |
| 40 | Tir sur cible en déplacement avec anticipation |
| 50 | Tir rapide sur plusieurs cibles |
| 60 | Tir précis depuis une position inconfortable |
| 70 | Tir réflexe à courte distance |
| 80 | Tir précis pendant un déplacement complexe |
| 90 | Enchaînement expert de tirs rapides et précis |
| 100 | Maîtrise ultime : précision exceptionnelle dans des situations de mouvement et de pression extrêmes |

#### Arbalète — Perception + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Tir précis sur cible immobile |
| 20 | Rechargement plus fluide après déplacement |
| 30 | Tir sur cible en mouvement |
| 40 | Tir depuis une couverture sans exposition inutile |
| 50 | Rechargement et tir dans une séquence maîtrisée |
| 60 | Tir réflexe à courte portée |
| 70 | Tir précis depuis une position instable |
| 80 | Enchaînement de tirs et déplacements défensifs |
| 90 | Exploitation experte des ouvertures de tir |
| 100 | Maîtrise ultime : précision et gestion du rythme de tir exceptionnelles |

#### Combat à mains nues — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Enchaînement de coups simples |
| 20 | Coup de projection simple |
| 30 | Esquive suivie d'une contre-attaque à mains nues |
| 40 | Prise et déséquilibre d'un adversaire |
| 50 | Enchaînement de frappes et projections |
| 60 | Immobilisation courte après une prise réussie |
| 70 | Contre avancé contre une attaque rapprochée |
| 80 | Désarmement à mains nues |
| 90 | Enchaînement expert de prises, projections et frappes |
| 100 | Maîtrise ultime : contrôle exceptionnel du combat rapproché |

#### Parade — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Parade des attaques simples |
| 20 | Parade d'attaques rapides |
| 30 | Déviation suivie d'une riposte |
| 40 | Parade contre des attaques lourdes avec timing précis |
| 50 | Parade successive de plusieurs attaques |
| 60 | Déviation vers une direction choisie |
| 70 | Contre-parade contre un adversaire expérimenté |
| 80 | Parade réflexe sur une attaque difficile à anticiper |
| 90 | Chaîne de parades et ripostes avancées |
| 100 | Maîtrise ultime : lecture et déviation exceptionnelle des attaques adverses |

### 6.2 Défense / mouvement

#### Esquive — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Pas d'esquive court |
| 20 | Esquive latérale rapide |
| 30 | Roulade contrôlée |
| 40 | Esquive suivie d'une reprise immédiate de position |
| 50 | Esquive de plusieurs attaques successives |
| 60 | Esquive réflexe sur attaque rapide |
| 70 | Enchaînement d'esquives dans plusieurs directions |
| 80 | Esquive acrobatique sur attaque complexe |
| 90 | Lecture avancée des trajectoires ennemies |
| 100 | Maîtrise ultime : déplacements défensifs extrêmement précis et rapides |

#### Parade — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Déviation simple d'une attaque |
| 20 | Déviation d'attaques rapides |
| 30 | Déviation suivie d'un repositionnement |
| 40 | Parade d'attaques lourdes |
| 50 | Parade successive |
| 60 | Déviation vers une direction choisie |
| 70 | Parade réflexe avancée |
| 80 | Déviation d'attaques complexes |
| 90 | Chaîne de parades précises |
| 100 | Maîtrise ultime du timing défensif |

#### Blocage — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Blocage d'attaques simples |
| 20 | Blocage d'attaques rapides |
| 30 | Blocage d'une attaque lourde sans perdre immédiatement l'équilibre |
| 40 | Blocage suivi d'un déplacement contrôlé |
| 50 | Maintien de garde contre plusieurs attaques |
| 60 | Absorption d'une attaque très puissante |
| 70 | Repositionnement pendant le blocage |
| 80 | Blocage et contre immédiat |
| 90 | Gestion experte de séries d'attaques |
| 100 | Maîtrise ultime : efficacité défensive maximale dans les situations de pression extrême |

#### Acrobatie — Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Saut contrôlé et réception stable |
| 20 | Roulade de réception |
| 30 | Saut avec changement de direction |
| 40 | Franchissement acrobatique d'obstacles |
| 50 | Enchaînement de mouvements acrobatiques |
| 60 | Réception après chute importante |
| 70 | Déplacement acrobatique rapide en combat |
| 80 | Utilisation d'éléments du décor pour changer de trajectoire |
| 90 | Enchaînement acrobatique complexe sans rupture |
| 100 | Maîtrise ultime du mouvement acrobatique |

#### Escalade — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Escalade de surfaces faciles |
| 20 | Franchissement de petits murs |
| 30 | Escalade de surfaces irrégulières |
| 40 | Changement de direction sur une paroi |
| 50 | Escalade rapide de structures verticales |
| 60 | Progression sur prises difficiles |
| 70 | Escalade de parois très complexes |
| 80 | Traversée latérale de surfaces difficiles |
| 90 | Escalade experte de structures presque impraticables |
| 100 | Maîtrise ultime : exploitation exceptionnelle des prises et de l'élan |

#### Athlétisme — Force + Agilité

| Niveau | Déblocage |
|---:|---|
| 10 | Course et saut correctement maîtrisés |
| 20 | Sprint court efficace |
| 30 | Franchissement rapide d'obstacles |
| 40 | Saut avec prise d'élan optimisée |
| 50 | Enchaînement course-saut-escalade |
| 60 | Course prolongée à haute intensité |
| 70 | Franchissement de parcours complexes à grande vitesse |
| 80 | Exploitation avancée de l'élan et du terrain |
| 90 | Parcours athlétique extrêmement exigeant |
| 100 | Maîtrise ultime des mouvements athlétiques |

### 6.3 Furtivité

#### Discrétion — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Déplacement discret de base |
| 20 | Déplacement silencieux sur terrain simple |
| 30 | Passage discret derrière une personne inattentive |
| 40 | Déplacement discret pendant une activité bruyante |
| 50 | Filature d'une personne sans attirer l'attention |
| 60 | Passage discret dans un environnement surveillé |
| 70 | Filature prolongée d'une personne attentive |
| 80 | Déplacement discret sur terrain défavorable |
| 90 | Infiltration experte dans un environnement fortement surveillé |
| 100 | Maîtrise ultime de la discrétion et de la filature |

#### Élimination furtive — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Attaque furtive sur cible totalement distraite |
| 20 | Élimination depuis l'arrière |
| 30 | Élimination après approche silencieuse |
| 40 | Élimination depuis une couverture |
| 50 | Élimination rapide sans attirer immédiatement les témoins proches |
| 60 | Élimination sur cible en déplacement |
| 70 | Enchaînement furtif sur plusieurs cibles séparées |
| 80 | Exploitation avancée du décor pour masquer l'action |
| 90 | Élimination furtive dans une situation fortement surveillée |
| 100 | Maîtrise ultime de l'approche et de l'élimination furtive |

#### Pickpocket — Agilité + Perception

| Niveau | Déblocage |
|---:|---|
| 10 | Vol d'un objet facilement accessible sur une personne distraite |
| 20 | Vol dans une poche extérieure sans être repéré |
| 30 | Vol d'un objet dans un vêtement moins accessible |
| 40 | Vol sur une personne en mouvement |
| 50 | Vol d'un objet mieux dissimulé |
| 60 | Vol sur une personne attentive avec une bonne maîtrise du timing |
| 70 | Vol discret dans une foule dense |
| 80 | Vol de plusieurs objets lors d'une même opportunité |
| 90 | Vol d'objets très bien dissimulés sur des personnes extrêmement vigilantes |
| 100 | Maîtrise ultime du pickpocket : vols extrêmement complexes réalisables avec une discrétion exceptionnelle |

#### Crochetage — Agilité + Intelligence

| Niveau | Déblocage |
|---:|---|
| 10 | Serrures très simples |
| 20 | Serrures mécaniques simples |
| 30 | Serrures à plusieurs difficultés |
| 40 | Serrures renforcées |
| 50 | Serrures complexes |
| 60 | Serrures protégées avec mécanismes secondaires |
| 70 | Serrures très complexes |
| 80 | Serrures expertes avec plusieurs mécanismes |
| 90 | Serrures exceptionnelles et très difficiles à analyser |
| 100 | Maîtrise ultime du crochetage mécanique |

#### Camouflage — Perception + Intelligence

| Niveau | Déblocage |
|---:|---|
| 10 | Se dissimuler dans un environnement favorable |
| 20 | Utiliser correctement les ombres et couvertures |
| 30 | Adapter sa position à l'environnement |
| 40 | Camouflage dans un environnement peu favorable |
| 50 | Se fondre dans un décor complexe |
| 60 | Modifier rapidement sa position pour rester caché |
| 70 | Camouflage avancé sur terrain difficile |
| 80 | Exploitation experte de la lumière, du décor et des couleurs |
| 90 | Dissimulation dans des environnements fortement défavorables |
| 100 | Maîtrise ultime du camouflage environnemental |

### 6.4 Magie

#### Invocation — Intelligence + Volonté

| Niveau | Déblocage |
|---:|---|
| 10 | Invoquer une petite créature simple |
| 20 | Maintenir une créature plus longtemps |
| 30 | Invoquer une créature de combat fiable |
| 40 | Contrôler plusieurs aspects d'une invocation |
| 50 | Invoquer une créature puissante |
| 60 | Maintenir une invocation complexe sous pression |
| 70 | Invoquer plusieurs créatures avec contrôle avancé |
| 80 | Invoquer une créature majeure exceptionnelle |
| 90 | Invocation de créatures extrêmement puissantes |
| 100 | Maîtrise ultime de l'invocation, permettant les manifestations les plus extraordinaires du domaine |

#### Nécromancie — Intelligence + Volonté

| Niveau | Déblocage |
|---:|---|
| 10 | Réanimer un cadavre récent de manière rudimentaire |
| 20 | Contrôler un mort-vivant simple |
| 30 | Maintenir plusieurs morts-vivants faibles |
| 40 | Réanimer un cadavre plus complexe |
| 50 | Créer un mort-vivant de combat puissant |
| 60 | Maintenir une petite troupe de morts-vivants |
| 70 | Manipuler des cadavres dans une zone étendue |
| 80 | Créer des morts-vivants majeurs |
| 90 | Produire un phénomène nécromantique exceptionnel |
| 100 | Maîtrise ultime de la nécromancie et de ses phénomènes à grande échelle |

#### Contrôle mental — Intelligence + Volonté

| Niveau | Déblocage |
|---:|---|
| 10 | Influencer brièvement une cible faible |
| 20 | Influencer une décision simple |
| 30 | Imposer une action courte à une cible vulnérable |
| 40 | Maintenir une influence plus complexe |
| 50 | Contrôler temporairement une cible résistante |
| 60 | Maintenir plusieurs influences simples |
| 70 | Contrôler plusieurs cibles avec une coordination avancée |
| 80 | Influencer une foule importante dans certaines conditions |
| 90 | Exercer un contrôle mental à très grande échelle |
| 100 | Maîtrise ultime : influence exceptionnelle sur un très grand nombre d'individus, selon les conditions du sort |

#### Magie élémentaire — Intelligence + Volonté

| Niveau | Déblocage |
---:|---|
| 10 | Manipulation élémentaire simple |
| 20 | Projectile élémentaire maîtrisé |
| 30 | Zone élémentaire de petite taille |
| 40 | Combinaison de formes élémentaires |
| 50 | Sort élémentaire puissant |
| 60 | Modification avancée de l'environnement proche |
| 70 | Manifestation élémentaire majeure |
| 80 | Phénomène élémentaire à grande échelle |
| 90 | Phénomène naturel majeur |
| 100 | Maîtrise ultime : manifestation élémentaire pouvant atteindre une ampleur catastrophique selon le contexte |

#### Magie physique — Intelligence + Volonté

| Niveau | Déblocage |
---:|---|
| 10 | Renforcement physique simple |
| 20 | Renforcement ciblé d'une capacité |
| 30 | Soin léger |
| 40 | Renforcement prolongé |
| 50 | Soin important |
| 60 | Modification avancée d'une capacité physique |
| 70 | Renforcement simultané de plusieurs capacités |
| 80 | Soin ou modification majeure |
| 90 | Transformation physique magique exceptionnelle |
| 100 | Maîtrise ultime du renforcement, des soins et de la modification physique |

#### Magie de groupe — Intelligence + Volonté

| Niveau | Déblocage |
---:|---|
| 10 | Compréhension et préparation d'un rituel collectif simple |
| 20 | Petit effet magique affectant plusieurs personnes ou une zone |
| 30 | Rituel capable de maintenir un effet de groupe |
| 40 | Effet de groupe de portée importante |
| 50 | Rituel puissant affectant une grande zone |
| 60 | Coordination de plusieurs composantes magiques |
| 70 | Manifestation magique majeure à grande échelle |
| 80 | Phénomène magique exceptionnel pouvant modifier durablement une zone |
| 90 | Manifestation de puissance à très grande échelle, avec conséquences majeures sur le monde |
| 100 | Maîtrise ultime de la magie de groupe : réalisation des phénomènes magiques les plus extraordinaires du système |

#### Magie de pacte — Intelligence + Volonté

| Niveau | Déblocage |
---:|---|
| 10 | Établir un pacte simple avec une entité compatible |
| 20 | Maintenir un lien magique durable |
| 30 | Obtenir un pouvoir limité en échange d'une condition |
| 40 | Négocier des conditions plus complexes |
| 50 | Établir un pacte puissant avec une entité majeure |
| 60 | Maintenir plusieurs clauses ou contreparties |
| 70 | Établir un pacte à conséquences importantes |
| 80 | Contracter avec une entité exceptionnellement puissante |
| 90 | Créer un pacte complexe capable de transformer durablement les possibilités du personnage |
| 100 | Maîtrise ultime des pactes, de leurs conditions et de leurs contreparties |

### 6.5 Connaissances

#### Alchimie — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Préparer des mélanges simples |
| 20 | Identifier les propriétés de composants courants |
| 30 | Préparer des potions fonctionnelles |
| 40 | Combiner plusieurs effets simples |
| 50 | Créer des potions complexes |
| 60 | Stabiliser des mélanges difficiles |
| 70 | Produire des préparations puissantes |
| 80 | Reproduire des recettes rares |
| 90 | Concevoir des préparations exceptionnelles |
| 100 | Maîtrise ultime de l'alchimie et création de préparations extraordinaires |

#### Botanique — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Identifier les plantes communes |
| 20 | Identifier leurs usages principaux |
| 30 | Reconnaître des espèces moins communes |
| 40 | Identifier des plantes dans des conditions difficiles |
| 50 | Identifier des plantes rares |
| 60 | Comprendre leurs interactions complexes |
| 70 | Identifier des espèces très rares |
| 80 | Reconnaître des plantes magiques complexes |
| 90 | Identifier presque toute flore exceptionnelle connue |
| 100 | Maîtrise ultime de la flore et de ses propriétés |

#### Médecine — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Traiter une blessure légère |
| 20 | Diagnostiquer les blessures courantes |
| 30 | Traiter des blessures plus sérieuses |
| 40 | Diagnostiquer des problèmes complexes |
| 50 | Réaliser des soins avancés |
| 60 | Traiter des traumatismes graves |
| 70 | Diagnostiquer des maladies ou blessures difficiles |
| 80 | Réaliser des interventions médicales complexes |
| 90 | Traiter des cas exceptionnellement difficiles |
| 100 | Maîtrise ultime de la médecine connue du monde |

#### Histoire — Intelligence

| Niveau | Déblocage |
---:|---|
| 10 | Connaître les événements historiques courants |
| 20 | Comprendre les grandes périodes historiques |
| 30 | Identifier les événements régionaux importants |
| 40 | Relier plusieurs événements historiques |
| 50 | Reconstruire une situation historique complexe |
| 60 | Identifier les contradictions dans les sources |
| 70 | Déduire des informations historiques inconnues |
| 80 | Interpréter des sources anciennes rares |
| 90 | Reconstituer des événements presque oubliés |
| 100 | Maîtrise exceptionnelle de l'histoire et de ses sources |

#### Géographie — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Lire une carte simple |
| 20 | S'orienter sur un territoire connu |
| 30 | Lire des cartes complexes |
| 40 | S'orienter dans une région inconnue |
| 50 | Estimer distances et reliefs efficacement |
| 60 | Cartographier correctement une zone explorée |
| 70 | S'orienter avec très peu de repères |
| 80 | Cartographier des régions complexes |
| 90 | Reconstruire une géographie à partir d'indices limités |
| 100 | Maîtrise ultime de l'orientation et de la cartographie |

#### Créatures — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Identifier les créatures communes |
| 20 | Reconnaître leurs comportements de base |
| 30 | Identifier leurs faiblesses évidentes |
| 40 | Reconnaître les comportements inhabituels |
| 50 | Identifier les créatures rares |
| 60 | Comprendre leurs cycles et comportements complexes |
| 70 | Déduire les faiblesses de créatures inconnues |
| 80 | Identifier des créatures très rares ou anciennes |
| 90 | Comprendre des créatures exceptionnellement mystérieuses |
| 100 | Maîtrise exceptionnelle de la connaissance des créatures |

#### Linguistique — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Comprendre quelques mots d'une langue inconnue |
| 20 | Comprendre des phrases simples |
| 30 | Tenir un échange rudimentaire |
| 40 | Comprendre des conversations courantes |
| 50 | Parler correctement une langue apprise |
| 60 | Comprendre des dialectes et variantes |
| 70 | Interpréter des expressions culturelles complexes |
| 80 | Comprendre une langue très rare ou ancienne |
| 90 | Décoder des formes linguistiques presque inconnues |
| 100 | Maîtrise exceptionnelle des langues et de leur structure |

### 6.6 Artisanat

#### Forge — Force + Intelligence

| Niveau | Déblocage |
---:|---|
| 10 | Réaliser des travaux de forge simples |
| 20 | Fabriquer des pièces métalliques fiables |
| 30 | Fabriquer des objets métalliques fonctionnels |
| 40 | Travailler des matériaux plus difficiles |
| 50 | Produire des pièces de haute qualité |
| 60 | Travailler des alliages complexes |
| 70 | Produire des ouvrages de forge avancés |
| 80 | Travailler des matériaux rares |
| 90 | Produire des ouvrages exceptionnels |
| 100 | Maîtrise ultime de la forge |

#### Travail de la matière — Intelligence + Agilité

| Niveau | Déblocage |
---:|---|
| 10 | Travailler correctement le bois, cuir et matériaux simples |
| 20 | Fabriquer des objets simples |
| 30 | Réaliser des assemblages précis |
| 40 | Travailler des formes complexes |
| 50 | Produire des objets de haute qualité |
| 60 | Combiner plusieurs matériaux efficacement |
| 70 | Travailler des matériaux difficiles |
| 80 | Réaliser des objets complexes et rares |
| 90 | Produire des ouvrages exceptionnels |
| 100 | Maîtrise ultime du travail des matériaux |

#### Couture — Agilité + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Réaliser des coutures simples |
| 20 | Réparer correctement un vêtement |
| 30 | Fabriquer un vêtement simple |
| 40 | Réaliser des coutures complexes |
| 50 | Fabriquer des vêtements ajustés |
| 60 | Travailler des matériaux délicats |
| 70 | Fabriquer des pièces complexes |
| 80 | Réaliser des ouvrages très détaillés |
| 90 | Créer des pièces exceptionnellement complexes |
| 100 | Maîtrise ultime de la couture et du travail textile |

#### Fabrication d'armes — Intelligence + Force

| Niveau | Déblocage |
---:|---|
| 10 | Fabriquer une arme simple |
| 20 | Fabriquer une arme fiable |
| 30 | Améliorer correctement une arme |
| 40 | Fabriquer des armes complexes |
| 50 | Produire des armes de haute qualité |
| 60 | Fabriquer des armes adaptées à des usages spécifiques |
| 70 | Produire des armes avancées |
| 80 | Travailler des matériaux rares pour l'armement |
| 90 | Concevoir des armes exceptionnelles |
| 100 | Maîtrise ultime de la fabrication d'armes |

#### Fabrication d'armures — Intelligence + Force

| Niveau | Déblocage |
---:|---|
| 10 | Fabriquer une protection simple |
| 20 | Réaliser une armure fonctionnelle |
| 30 | Ajuster une armure à son porteur |
| 40 | Fabriquer des protections complexes |
| 50 | Produire des armures de haute qualité |
| 60 | Optimiser protection et mobilité |
| 70 | Fabriquer des armures avancées |
| 80 | Travailler des matériaux rares |
| 90 | Concevoir des armures exceptionnelles |
| 100 | Maîtrise ultime de la fabrication d'armures |

#### Réparation — Intelligence + Perception

| Niveau | Déblocage |
---:|---|
| 10 | Réparer des dégâts simples |
| 20 | Réparer des équipements courants |
| 30 | Identifier rapidement une panne ou un défaut |
| 40 | Réparer des mécanismes complexes |
| 50 | Restaurer efficacement un équipement fortement endommagé |
| 60 | Réparer sans détériorer les composants sensibles |
| 70 | Restaurer des équipements complexes |
| 80 | Réparer des objets rares ou anciens |
| 90 | Restaurer des objets dans un état exceptionnellement dégradé |
| 100 | Maîtrise ultime du diagnostic et de la réparation |

### 6.7 Social / communication

#### Persuasion — Charisme + Intelligence

| Niveau | Déblocage |
---:|---|
| 10 | Convaincre sur une demande simple |
| 20 | Obtenir un petit changement de décision |
| 30 | Convaincre une personne hésitante |
| 40 | Argumenter efficacement dans une situation tendue |
| 50 | Convaincre sur une demande importante |
| 60 | Adapter rapidement son argumentaire à l'interlocuteur |
| 70 | Convaincre une personne fortement opposée |
| 80 | Obtenir un accord difficile sans pression directe |
| 90 | Convaincre dans des situations extrêmement défavorables |
| 100 | Maîtrise ultime de la persuasion, dans les limites de la personnalité et des convictions de l'interlocuteur |

#### Intimidation — Charisme + Force

| Niveau | Déblocage |
---:|---|
| 10 | Impressionner une personne vulnérable |
| 20 | Faire hésiter un interlocuteur peu déterminé |
| 30 | Obtenir une concession simple |
| 40 | Faire reculer un adversaire socialement ou physiquement impressionné |
| 50 | Imposer une demande importante à une personne hésitante |
| 60 | Maintenir la pression face à une opposition forte |
| 70 | Intimider un adversaire expérimenté |
| 80 | Faire céder un groupe dans certaines circonstances |
| 90 | Intimider des individus exceptionnellement déterminés |
| 100 | Maîtrise ultime de l'intimidation, sans garantir la soumission d'une personne totalement incorruptible ou fanatique |

#### Éloquence — Charisme + Intelligence

| Niveau | Déblocage |
---:|---|
| 10 | Discours clair et compréhensible |
| 20 | Maintenir l'attention d'un petit groupe |
| 30 | Construire un argument convaincant |
| 40 | Adapter son discours à différents interlocuteurs |
| 50 | Captiver un groupe important |
| 60 | Improviser un discours complexe |
| 70 | Mobiliser un groupe autour d'une idée |
| 80 | Tenir un discours majeur devant une foule |
| 90 | Influencer fortement une assemblée hostile |
| 100 | Maîtrise ultime de l'éloquence et de la prise de parole publique |

#### Marchandage — Charisme + Intelligence

| Niveau | Déblocage |
---:|---|
| 10 | Négocier un prix simple |
| 20 | Obtenir une petite réduction |
| 30 | Identifier une marge de négociation |
| 40 | Négocier plusieurs éléments d'un échange |
| 50 | Obtenir un accord commercial avantageux |
| 60 | Exploiter correctement les besoins de l'interlocuteur |
| 70 | Négocier des contrats complexes |
| 80 | Conclure des échanges très difficiles |
| 90 | Négocier dans des situations économiques exceptionnellement défavorables |
| 100 | Maîtrise ultime du marchandage et des négociations commerciales |

## 7. Caractéristiques et compétences

Les caractéristiques associées indiquent les capacités générales principalement sollicitées. Elles ne remplacent pas la compétence.

Une même action peut développer plusieurs éléments du système lorsqu'elle exerce réellement plusieurs capacités.

Exemples :

- utiliser une épée développe **Épée** et peut solliciter Force et Agilité ;
- apprendre une langue développe **Linguistique** et sollicite notamment Intelligence ;
- négocier dans une langue étrangère peut solliciter **Linguistique**, **Marchandage** et Charisme ;
- réussir une parade développe **Parade** et sollicite Agilité et Perception.

## 8. Structure actuelle

Le système conserve les **45 entrées de compétences actuellement définies**, réparties en 7 domaines :

| Domaine | Nombre |
|---|---:|
| Combat | 10 |
| Défense / mouvement | 6 |
| Furtivité | 5 |
| Magie | 7 |
| Connaissances | 7 |
| Artisanat | 6 |
| Social / communication | 4 |
| **Total** | **45** |

Chaque entrée dispose maintenant de **10 paliers de maîtrise**, soit **450 déblocages définis**.

## 9. Éléments restant à définir

- valeur initiale des compétences ;
- influence numérique exacte des caractéristiques sur chaque compétence ;
- éventuels prérequis supplémentaires pour certains déblocages ;
- interactions détaillées avec les races ;
- interactions détaillées avec les classes ;
- règles détaillées de chaque compétence magique ;
- équilibrage des déblocages lors des tests en jeu ;
- effets exacts des techniques dans Unreal Engine.
