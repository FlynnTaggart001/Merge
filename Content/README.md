# Merge Content

Ce dossier contient les assets Unreal créés dans l'éditeur.

## Assets de fondation à créer localement

### Maps
- `Maps/L_TestArena` — niveau de test minimal.

### Blueprints
- `Blueprints/Core/BP_MergeGameMode` → `AMergeGameMode`
- `Blueprints/Core/BP_MergePlayerController` → `AMergePlayerController`
- `Blueprints/Core/BP_MergeGameInstance` → `UMergeGameInstance` (optionnel)
- `Blueprints/Characters/BP_MergeCharacter` → `AMergeCharacter`

### Input Enhanced Input
- `Input/IA_Move` (Axis2D)
- `Input/IA_Look` (Axis2D)
- `Input/IA_Jump` (Digital)
- `Input/IA_Interact` (Digital)
- `Input/IMC_Default` (mapping context)

Assigner les `IA_*` à `BP_MergeCharacter` et `IMC_Default` à `BP_MergePlayerController`. Les assets `.uasset` sont créés par l'éditeur Unreal, pas à la main.
