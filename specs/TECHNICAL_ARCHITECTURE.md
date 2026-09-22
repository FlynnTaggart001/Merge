# TECHNICAL ARCHITECTURE - Unreal Engine 5
## Merge Project - Technical Specification

**Date** : 2026-08-19
**Statut** : APPROUVÉ
**Engine** : Unreal Engine 5.8.1
**Langage Principal** : C++
**Langage Complémentaire** : Blueprint (prototypage & UI)

---

## 1. Vue d'Ensemble

Ce document définit l'architecture technique du projet Merge sous Unreal Engine 5.

L'architecture est conçue pour :
- Supporter tous les systèmes RPG définis dans GAME_BIBLE.md
- Maintenir l'esthétique PS1 intentionnelle
- Permettre l'itération rapide et le prototypage
- Assurer scalabilité et maintenabilité
- Faciliter la collaboration multi-IA

**Important** : Cette architecture décrit la cible technique. Le scaffold actuel ne contient qu'une partie des modules et assets ; les performances réelles et la scalabilité doivent être validées par tests et profiling durant le développement.

---

## 2. Stack Technologique

### Engine
- **Unreal Engine 5.8.1** (version obligatoire)
- **Plateforme cible** : Windows PC (extensible)
- **Résolution cible** : À DÉCIDER
- **FPS cible** : À DÉCIDER

### Langage de Programmation
- **Langage principal** : C++20
- **Langage complémentaire** : Blueprint (prototypage et UI)
- **Outil de scripting** : À DÉCIDER (Python pour outils éditeur)

### Plugins Essentiels
- **World Partition** (partitionnement et streaming du monde)
- **Mass Framework** (optionnel - à utiliser si justifié par les besoins)
- **Niagara** (effets particulaires)
- **Audio Engine** (UE5 natif)
- **MetaHuman** : Non utilisé (esthétique PS1 incompatible)

### Outils Externes
- **Git** : Versioning du code et assets
- **.gitignore** : Configuration standard UE5
- **Perforce** : Optionnel (À DÉCIDER selon équipe)

---

## 3. Structure des Modules C++

### Organisation Modulaire

```
Source/
├── Merge/
│   ├── Core/                    # Systèmes fondamentaux
│   │   ├── Character/           # Joueur et PNJ base
│   │   ├── Controller/          # Input et logique de contrôle
│   │   ├── GameMode/            # Gestion du jeu
│   │   └── Settings/            # Configuration globale
│   │
│   ├── Gameplay/                # Systèmes RPG (à implémenter)
│   │   ├── Combat/              # Combat, dégâts, armes
│   │   ├── Magic/               # Magie et sorts
│   │   ├── Inventory/           # Inventaire et équipement
│   │   ├── Progression/         # Compétences et attributs
│   │   ├── Alchemy/             # Alchimie et crafting
│   │   └── Quest/               # Système de quêtes
│   │
│   ├── AI/                      # Systèmes d'IA (à implémenter)
│   │   ├── Behavior/            # Comportements et routines
│   │   ├── Navigation/          # Pathfinding et mouvement
│   │   ├── Perception/          # Détection et perception
│   │   └── Mass/                # Mass Framework (optionnel)
│   │
│   ├── World/                   # Systèmes du monde (à implémenter)
│   │   ├── Environment/         # Environnement dynamique
│   │   ├── Time/                # Cycle jour/nuit
│   │   ├── Weather/             # Météo
│   │   ├── Events/              # Événements dynamiques
│   │   └── Factions/            # Factions et réputation
│   │
│   ├── UI/                      # Interface utilisateur (à implémenter)
│   │   ├── HUD/                 # HUD en jeu
│   │   ├── Menu/                # Menus principaux
│   │   ├── Dialogue/            # Système de dialogue
│   │   └── Widgets/             # Widgets réutilisables
│   │
│   ├── Data/                    # Data-Driven
│   │   ├── Items/               # Définitions d'objets
│   │   ├── NPCs/                # Données de PNJ
│   │   ├── Quests/              # Données de quêtes
│   │   ├── Spells/              # Données de sorts
│   │   ├── Factions/            # Données de factions
│   │   └── Loot/                # Tables de loot
│   │
│   ├── Rendering/               # Systèmes de rendu custom
│   │   ├── PostProcess/         # Post-processing PS1
│   │   ├── Materials/           # Matériaux et shaders
│   │   └── Textures/            # Gestion des textures
│   │
│   ├── Audio/                   # Systèmes audio
│   │   ├── Ambient/             # Ambiance sonore
│   │   ├── Music/               # Musiques et thèmes
│   │   └── SFX/                 # Effets sonores
│   │
│   ├── Save/                    # Système de sauvegarde
│   │   ├── Serialization/       # Sérialisation des données
│   │   └── Manager/             # Gestionnaire de sauvegarde
│   │
│   └── Utilities/               # Utilitaires et helpers
│       ├── Logging/             # Système de logs
│       ├── Debug/               # Outils debug
│       └── Helpers/             # Fonctions utilitaires
│
└── Plugins/                     # Plugins custom (optionnel)
    └── MergeCore/               # Plugin de base personnalisé
```

### Modules UE5 Public/Private

Chaque module C++ suit la structure UE5 standard :

```
Source/Merge/ModuleName/
├── Public/
│   └── [Header files .h]
├── Private/
│   └── [Implementation files .cpp]
└── ModuleName.Build.cs
```

---

## 4. Conventions de Code C++

### Nommage des Classes
```cpp
// Joueur et PNJ
ACharacterBase
APlayerCharacter
APlayerController
ANPCCharacter

// Systèmes
UInventoryComponent
UCombatComponent
UMagicComponent
UProgressionComponent

// Data
UItemData
USpellData
UQuestData
UNPCData
UFactionData

// Managers
AGameManager
AWorldManager
ATimeManager
AQuestManager

// Enums
EItemType
ESpellSchool
EFactionReputation
ECombatDamageType

// Structs
FCharacterAttributes
FInventorySlot
FSpellEffect
FQuestProgress
```

### Naming Conventions
- **Classes** : Préfixe `A` (Actor) ou `U` (Object)
- **Interfaces** : Préfixe `I`
- **Enums** : Préfixe `E`
- **Structs** : Préfixe `F`
- **Booléens** : Préfixe `b` (ex: `bIsAlive`, `bCanCast`)
- **Variables membres privées** : Préfixe `_` (ex: `_health`, `_mana`)
- **Fonctions** : CamelCase (ex: `GetCharacterHealth()`, `TakeDamage()`)

### Indentation et Formatage
- Indentation : 4 espaces
- Accolades : Allman style (recommandé UE5)
- Longueur de ligne : 120 caractères max

### Documentation
```cpp
/**
 * Applique les dégâts au personnage
 * 
 * @param DamageAmount Montant des dégâts à appliquer
 * @param DamageType Type de dégâts (tranchant, contondant, etc.)
 * @param InstigatorController Contrôleur qui cause les dégâts
 * @return Montant réel des dégâts appliqués
 */
float TakeDamage(float DamageAmount, EDamageType DamageType, AController* InstigatorController);
```

---

## 5. Architecture des Composants

### Character Component Pattern

Tous les personnages (joueur et PNJ) utilisent un système de composants modulaire :

```cpp
ACharacterBase
├── UCharacterMovementComponent
├── UInventoryComponent        // Gestion inventaire
├── UCombatComponent           // Gestion combat
├── UMagicComponent            // Gestion magie
├── UProgressionComponent      // Gestion progression
├── UAttributesComponent       // Attributs de base
├── UStatusComponent           // États (poison, buff, etc.)
├── UPerceptionComponent       // Pour IA (voir, entendre)
└── UAnimationComponent        // Gestion des animations
```

### Pattern de Communication

Les composants communiquent via :
- **Delegates** pour les événements (santé changée, magie lancée, etc.)
- **Getters/Setters** pour accès aux données
- **Event Driven Architecture** pour découplage

```cpp
// Exemple de delegate
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnHealthChanged, float, NewHealth, float, MaxHealth);

// Dans la classe
UPROPERTY(BlueprintAssignable)
FOnHealthChanged OnHealthChanged;

// Dans le composant
void UAttributesComponent::SetHealth(float NewHealth)
{
    Health = NewHealth;
    OnHealthChanged.Broadcast(Health, MaxHealth);
}
```

---

## 6. Data-Driven Architecture

### Tables de Données Principales

Toutes les données de contenu sont stockées en tables de données (Data Tables), pas en code :

#### Items et Équipement
```
/Game/Data/Items/
├── DT_Weapons.uasset       (Table : Épées, haches, arcs, etc.)
├── DT_Armor.uasset         (Table : Casques, armures, etc.)
├── DT_Accessories.uasset   (Table : Anneaux, amulettes, etc.)
├── DT_Consumables.uasset   (Table : Potions, nourriture, etc.)
└── DT_Materials.uasset     (Table : Matériaux d'alchimie, etc.)
```

#### Gameplay
```
/Game/Data/Gameplay/
├── DT_Spells.uasset        (Table : Définitions de sorts)
├── DT_Skills.uasset        (Table : Compétences)
├── DT_Attributes.uasset    (Table : Formules d'attributs)
├── DT_Recipes.uasset       (Table : Recettes d'alchimie)
└── DT_Status.uasset        (Table : États et effets)
```

#### Monde
```
/Game/Data/World/
├── DT_NPCs.uasset          (Table : Définitions de PNJ)
├── DT_Factions.uasset      (Table : Factions et relations)
├── DT_Quests.uasset        (Table : Quêtes principales)
├── DT_SideQuests.uasset    (Table : Quêtes secondaires)
├── DT_Locations.uasset     (Table : Lieux du monde)
└── DT_Dialogue.uasset      (Table : Dialogues)
```

#### Loot
```
/Game/Data/Loot/
├── DT_LootTables.uasset    (Table : Générateurs de loot)
├── DT_WeaponLoot.uasset    (Table : Loot d'armes)
└── DT_TreasureLoot.uasset  (Table : Loot de trésors)
```

### Structure de Data Table

Exemple : `FWeaponRow`
```cpp
USTRUCT(BlueprintType)
struct FWeaponRow : public FTableRowBase
{
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FName WeaponID;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FString DisplayName;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    float BaseDamage;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    EWeaponType WeaponType;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    float Weight;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    UTexture2D* Icon;
    
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FString Description;
};
```

---

## 7. Système de Sauvegarde

### Architecture de Sauvegarde

```
SaveGame/
├── PlayerData
│   ├── Position
│   ├── Rotation
│   ├── Attributes
│   ├── Inventory
│   ├── CompletedQuests
│   ├── Factions (réputation)
│   └── SkillsLevels
│
├── WorldData
│   ├── TimeCycle (heure actuelle)
│   ├── QuestProgress
│   ├── WorldState (objets activés/désactivés)
│   ├── NPCLocations
│   ├── DefeatedEnemies
│   └── CollectedItems
│
└── GameSettings
    ├── GraphicsSettings
    ├── AudioSettings
    ├── GameplaySettings
    └── ControlsBindings
```

### Classe de Sauvegarde

```cpp
UCLASS()
class MERGE_API UMergeSaveGame : public USaveGame
{
    GENERATED_BODY()

public:
    UPROPERTY()
    FString SaveName;
    
    UPROPERTY()
    FDateTime SaveTime;
    
    UPROPERTY()
    FPlayerSaveData PlayerData;
    
    UPROPERTY()
    FWorldSaveData WorldData;
    
    UPROPERTY()
    FGameSettingsSaveData GameSettings;
};
```

### Manager de Sauvegarde

```cpp
UCLASS()
class MERGE_API ASaveGameManager : public AActor
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "Save")
    void SaveGame(const FString& SaveSlot);
    
    UFUNCTION(BlueprintCallable, Category = "Save")
    void LoadGame(const FString& SaveSlot);
    
    UFUNCTION(BlueprintCallable, Category = "Save")
    void DeleteSave(const FString& SaveSlot);
    
    UFUNCTION(BlueprintCallable, Category = "Save")
    bool SaveExists(const FString& SaveSlot);
};
```

---

## 8. World Partition et Streaming

### Partitionnement du Monde

Le monde ouvert utilise **World Partition** pour :
- Charger/décharger les zones automatiquement
- Gérer la mémoire efficacement
- Supporter un monde large et expansible

### Organisation Spatiale

```
/Game/Maps/
├── MainWorld (World Partition activé)
│   ├── Region_VillageCenter
│   ├── Region_ForestNorth
│   ├── Region_CatacombsUnderground
│   ├── Region_MountainPass
│   ├── Region_AbandonedRuins
│   └── [Autres régions]
│
└── LevelStreaming (fallback)
    ├── L_Village
    ├── L_Forest
    └── [Autres niveaux]
```

### Paramètres de Streaming

Les paramètres suivants devront être déterminés par profiling et tests réels :

```cpp
// World Partition Settings (À calibrer)
UPROPERTY(EditAnywhere, Category = "Streaming")
float StreamingDistance = 0.0f;  // À déterminer par profiling

UPROPERTY(EditAnywhere, Category = "Streaming")
float UnloadingDistance = 0.0f;  // À déterminer par profiling

UPROPERTY(EditAnywhere, Category = "Streaming")
int32 MaxCellsToLoad = 0;  // À déterminer par profiling
```

**Note** : Ces valeurs seront optimisées selon :
- La plateforme cible
- Les ressources disponibles
- Les performances observées
- La complexité du contenu

### Actors de Point d'Intérêt

Les zones importantes utilisent des **Actor Descriptors** pour optimisation :

```cpp
UCLASS()
class MERGE_API AWorldRegion : public AActor
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere)
    FString RegionName;
    
    UPROPERTY(EditAnywhere)
    FBox RegionBounds;
    
    UPROPERTY(EditAnywhere)
    float StreamingPriority = 1.0f;
    
    // Déclenche le chargement de contenu
    virtual void OnRegionLoaded();
    virtual void OnRegionUnloaded();
};
```

---

## 9. IA et Comportements

### Architecture de l'IA

L'IA des PNJ est conçue avec flexibilité :

**Pour les PNJ importants** (héros, boss, personnages clés) :
- Utiliser des **Actors classiques** avec comportement personnalisé
- Contrôle fin possible via C++ et Blueprint
- Moins de surcharge de performance

**Pour les PNJ nombreux** (civils, gardes génériques, etc.) :
- Utiliser **Mass Framework** si justifié par les besoins
- Architecture préparée mais adoption optionnelle
- À valider par tests de performance réels

### Comportement de Base (Actor classique)

```cpp
UCLASS()
class MERGE_API ANPCCharacter : public ACharacterBase
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "AI")
    void ExecuteRoutine(float CurrentTime);
    
    UFUNCTION(BlueprintCallable, Category = "AI")
    void DetectPlayer(APlayerCharacter* Player);
    
    UFUNCTION(BlueprintCallable, Category = "AI")
    void RespondToEvent(FNPCEvent Event);

protected:
    UPROPERTY(EditAnywhere)
    TArray<FNPCRoutineStep> DailyRoutine;
    
    UPROPERTY(EditAnywhere)
    float DetectionRange = 1000.0f;  // À calibrer
};
```

### Mass Framework (Optionnel)

Si l'architecture Mass est nécessaire (validée par tests) :

```cpp
// Structure d'entité Mass pour PNJ génériques
USTRUCT()
struct FNPCMassData : public FMassFragment
{
    UPROPERTY()
    FString NPCID;
    
    UPROPERTY()
    FVector GoalPosition;
    
    UPROPERTY()
    float DetectionRange;
    
    UPROPERTY()
    EAIState CurrentState;
};

// States possibles
UENUM(BlueprintType)
enum class EAIState : uint8
{
    Idle,           // Au repos
    Patrol,         // En patrouille
    Suspicious,     // Vigilant
    Attacking,      // Attaque le joueur
    Fleeing,        // Fuite
    Dead            // Mort
};
```

### Système de Routines

Indépendant de la technologie (Actor ou Mass) :

```
Timeline 24h :
00:00 - 06:00 : Sleep (à domicile)
06:00 - 08:00 : Morning Routine
08:00 - 12:00 : Work/Activity
12:00 - 13:00 : Lunch
13:00 - 18:00 : Work/Activity
18:00 - 20:00 : Evening Routine
20:00 - 21:00 : Dinner
21:00 - 00:00 : Leisure/Sleep
```

---

## 10. Gestion des Assets

### Organisation des Assets

```
Content/
├── Art/
│   ├── Characters/
│   │   ├── Player/
│   │   ├── NPCs/
│   │   └── Enemies/
│   ├── Environments/
│   │   ├── Village/
│   │   ├── Forest/
│   │   ├── Catacombs/
│   │   └── Ruines/
│   ├── Items/
│   │   ├── Weapons/
│   │   ├── Armor/
│   │   └── Accessories/
│   ├── Effects/
│   │   ├── Particles/
│   │   ├── Spells/
│   │   └── Combat/
│   └── UI/
│       ├── Icons/
│       ├── Widgets/
│       └── Fonts/
│
├── Audio/
│   ├── Music/
│   │   ├── Ambient/
│   │   ├── Combat/
│   │   └── Exploration/
│   ├── SFX/
│   │   ├── Combat/
│   │   ├── Magic/
│   │   ├── UI/
│   │   └── Ambient/
│   └── Dialogue/
│
├── Blueprints/
│   ├── Characters/
│   ├── Gameplay/
│   ├── UI/
│   └── Tutorials/
│
└── Maps/
    ├── MainWorld/
    └── Testing/
```

### Convention de Nommage des Assets

```
Mesh:       SM_CharacterName_Body
Skeleton:   SK_CharacterName
Material:   M_CharacterName_Skin
Texture:    T_CharacterName_Diffuse
             T_CharacterName_Normal
             T_CharacterName_Roughness
Sound:      A_ActionName_Type
Animation:  A_CharacterName_Action
Blueprint:  BP_CharacterName
DataTable:  DT_CategoryName
             DT_Weapons
             DT_Spells
```

---

## 11. Esthétique PS1

### Configuration du Rendu

Malgré l'utilisation d'UE5, l'esthétique PS1 est maintenue via :

#### Post-Processing
```cpp
UCLASS()
class MERGE_API APS1PostProcessVolume : public APostProcessVolume
{
    GENERATED_BODY()

public:
    virtual void BeginPlay() override;
    
private:
    void SetupPS1Effects();
    void ConfigureGraininess();
    void ApplyLowPolyStyle();
};
```

#### Matériaux Custom
- Vertex-lit uniquement (pas de PBR complexe)
- Textures basse résolution
- Pas de bump mapping moderne
- Éclairage simple et direct

#### Shaders PS1
```hlsl
// Simple vertex lit shader (PS1 style)
float4 main(VertexInput Input) : SV_TARGET
{
    float3 Normal = normalize(Input.Normal);
    float3 LightDir = normalize(-LightDirection);
    float Diffuse = max(0, dot(Normal, LightDir));
    return float4(BaseColor * (Ambient + Diffuse * LightColor), 1.0);
}
```

#### Limitations Visuelles Intentionnelles
- Résolution de texture basse
- Nombre de polygones limité par zone
- Brouillard de distance marqué
- Pas de ray-tracing ou techniques modernes avancées

---

## 12. Modules Dépendances

### Module Dependencies Graph

```
Core (fondation)
├── Gameplay (dépend de Core)
│   ├── Combat
│   ├── Magic
│   ├── Inventory
│   ├── Progression
│   ├── Alchemy
│   └── Quest
├── AI (dépend de Core)
│   ├── Behavior
│   ├── Navigation
│   └── Perception
├── World (dépend de Core)
│   ├── Environment
│   ├── Time
│   ├── Weather
│   ├── Events
│   └── Factions
├── UI (dépend de Core)
│   ├── HUD
│   ├── Menu
│   ├── Dialogue
│   └── Widgets
├── Audio (dépend de Core)
├── Rendering (dépend de Core)
├── Save (dépend de Core)
└── Utilities (dépend de Core)
```

### Règle de Dépendance

- **Jamais** : Gameplay dépend de UI
- **Oui** : UI dépend de Gameplay (unidirectionnel)
- **Oui** : Tous dépendent de Core
- **Non** : Modules frères ne dépendent pas les uns des autres (via interfaces/delegates)

---

## 13. Système de Logging et Debug

### Logging

```cpp
#define MERGE_LOG(Category, Verbosity, Message) \
    UE_LOG(LogMerge, Verbosity, TEXT(Message))

#define MERGE_WARNING(Message) \
    UE_LOG(LogMerge, Warning, TEXT(Message))

#define MERGE_ERROR(Message) \
    UE_LOG(LogMerge, Error, TEXT(Message))
```

### Console Commands

```cpp
void MergeConsoleCommands::RegisterCommands()
{
    IConsoleManager::Get().RegisterConsoleCommand(
        TEXT("merge.godmode"),
        TEXT("Activate god mode"),
        FConsoleCommandDelegate::CreateStatic(&ActivateGodMode)
    );
    
    IConsoleManager::Get().RegisterConsoleCommand(
        TEXT("merge.spawnenemy"),
        TEXT("Spawn enemy at player location"),
        FConsoleCommandWithArgsDelegate::CreateStatic(&SpawnEnemy)
    );
}
```

---

## 14. Intégration Blueprint

### Utilisation de Blueprint

**Blueprint EST utilisé pour** :
- ✅ Prototypage rapide
- ✅ Assemblage de contenu
- ✅ Tuning et balancing
- ✅ UI et Widgets
- ✅ Événements et Timelines simples
- ✅ Tutorial et exemples

**Blueprint N'EST PAS utilisé pour** :
- ❌ Architecture fondamentale
- ❌ Systèmes critiques (Combat, IA)
- ❌ Gestion d'état complexe
- ❌ Optimisation de performance
- ❌ Logique temps réel critique

### Exemple : Blueprint de Prototypage

```
BP_QuickMagicTest (Blueprint)
  └─ Parent: ACharacterBase (C++)
      ├─ UMagicComponent (C++)
      ├─ UCombatComponent (C++)
      └─ [Tuning et visual setup en Blueprint]
```

---

## 15. Phases d'Implémentation

### Phase 2 : Prototype Technique (Actuelle)

**Objectifs** :
- [x] Décision : Unreal Engine 5 + C++
- [ ] Configuration UE5 complète
- [ ] Structure modulaire C++ en place
- [ ] Conventions de code établies
- [ ] Personnage joueur basique (vide, prêt pour systèmes)
- [ ] Caméra troisième personne basique
- [ ] Monde vide chargeable
- [ ] Esthétique PS1 de base testée
- [ ] Pipeline de build validé

**Livrables** :
- Projet UE5 compilable et fonctionnel
- Structure C++ complète
- Documentation technique (ce fichier)
- Configuration git/versioning
- Pas de gameplay réel

### Phase 3 : Prototype Gameplay

Implémentation progressive des systèmes sur la base établie ici.

---

## 16. Checklist de Conformité Architecturale

**Architecture** :
- ✅ Modulaire et extensible
- ✅ Data-driven
- ✅ C++ fondamental + Blueprint complémentaire
- ✅ Prêt pour tous les systèmes GAME_BIBLE

**Flexibilité** :
- ✅ PNJ Actor classique pour personnages importants
- ✅ Mass Framework optionnel (à valider par tests)
- ✅ Performance à calibrer via profiling
- ✅ Pas de contrainte de scalabilité fixe

**Maintainabilité** :
- ✅ Code documenté
- ✅ Conventions claires
- ✅ Séparation des préoccupations
- ✅ Logging et debug tools

---

## 17. Configuration Git

### .gitignore Standard UE5

```
# UE5 .gitignore
Binaries/
Intermediate/
Saved/
*.sln
*.vcxproj
*.vcxproj.filters
Plugins/*/Binaries/
Plugins/*/Intermediate/
```

### Branches de Développement

```
main (stable)
├── develop (intégration)
│   ├── feature/gameplay-*
│   ├── feature/ai-*
│   ├── feature/ui-*
│   ├── feature/world-*
│   ├── bugfix/*
│   └── optimization/*
```

---

## 18. Prochaines Étapes (Phase 2)

1. **Créer le projet UE5** avec configuration initiale
2. **Setup des modules C++** vides (structure prête)
3. **Configurer World Partition**
4. **Créer le personnage de base** (vide en attente des systèmes)
5. **Implémenter la caméra PS1** basique
6. **Tester l'esthétique PS1** avec assets de base
7. **Valider le pipeline de build**

**Remarque** : Aucun gameplay réel ne sera implémenté durant Phase 2. Le socle technique doit être vide et prêt pour l'ajout futur des systèmes.

---

## 19. Conventions de Commit

Tous les commits doivent suivre cette convention :

```
[MODULE] Short description

Longer description explaining the change if needed.

Type: Feature/Bugfix/Optimization/Documentation
Module: Core/Gameplay/AI/World/UI/Audio/Rendering/Save/Utils
```

Exemple :
```
[Core] Setup character base class

- Create ACharacterBase parent class
- Implement attribute system framework
- Add component pattern for modularity

Type: Feature
Module: Core
```

---

## 20. Validations et Tests Futurs

### À Valider par Profiling
- Distances de streaming optimales
- Nombre maximum de PNJ simultanés
- Impact de la résolution des textures PS1
- Performance du rendu vertex-lit

### À Déterminer par Tests
- Efficacité du système de sauvegarde
- Stabilité du World Partition
- Utilité réelle de Mass Framework
- Optimisation des effets PS1

---

## 21. Ressources et Références

### Documentation Officielle
- [Unreal Engine 5 Documentation](https://docs.unrealengine.com/)
- [C++ API Reference](https://docs.unrealengine.com/5.0/en-US/API/)
- [World Partition Guide](https://docs.unrealengine.com/5.0/en-US/world-partition-in-unreal-engine/)
- [Mass Framework](https://docs.unrealengine.com/5.0/en-US/mass-framework/)

### Best Practices
- Coding Standards : UE5 Coding Standard
- Architecture : Actor/Component pattern
- Performance : Profiling avec UE5 Profiler

---

**Statut** : ✅ APPROUVÉ
**Date de Révision** : À chaque changement d'architecture majeur
**Responsable** : Architecture / Game Director
**Validé par** : Game Director
**Date d'Approbation** : 2026-08-19
