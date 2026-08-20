# Merge Content

This folder holds Unreal assets (maps, blueprints, meshes, data assets).

## Expected foundation assets (create in Editor)

### Maps
- `Maps/L_TestArena` — minimal test level (floor + light + player start)

### Blueprints (inherit from C++)
- `Blueprints/Core/BP_MergeGameMode` → `AMergeGameMode`
- `Blueprints/Core/BP_MergePlayerController` → `AMergePlayerController`
- `Blueprints/Core/BP_MergeGameInstance` → `UMergeGameInstance` (optional)
- `Blueprints/Character/BP_MergeCharacter` → `AMergeCharacter`

### Input (Enhanced Input)
- `Input/IA_Move` (Axis2D)
- `Input/IA_Look` (Axis2D)
- `Input/IA_Jump` (Digital)
- `Input/IA_Interact` (Digital)
- `Input/IMC_Default` (mapping context)

Assign IA_* on `BP_MergeCharacter` and IMC_Default on `BP_MergePlayerController`.

Binary `.uasset` files are created by the Unreal Editor, not by hand.
