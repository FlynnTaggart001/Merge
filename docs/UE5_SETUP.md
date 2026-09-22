# Merge — UE5 Local Setup (Phase 1)

## Engine version

**Unreal Engine 5.8.1** (required project version).

If you use another 5.x, update `Merge.uproject` → `EngineAssociation` and the `IncludeOrderVersion` in the Target files.

## Prerequisites

- Unreal Engine 5.8.1 installed via Epic Games Launcher
- Visual Studio 2022 (Windows) with “Game development with C++” workload  
  or Xcode (Mac) / appropriate Linux toolchain
- Git

## First open

1. Clone / open the repository.
2. Right-click `Merge.uproject` → **Generate Visual Studio project files** (or open with UE; it will offer to rebuild).
3. Open `Merge.uproject` with UE 5.8.1.
4. Let it compile the `Merge` module.
5. In Content Browser, create the assets listed in `Content/README.md`.
6. Set GameMode override / defaults if needed (already pointed in `DefaultEngine.ini`).
7. Open / create `L_TestArena`, place Player Start, play.

## Architecture (C++)

The directories described by the technical architecture are the **target architecture**. Only the modules explicitly delivered in the Phase 1 scaffold are currently present; the remaining modules are future implementation targets.

```
Source/Merge/
  Core/          GameInstance, GameMode, PlayerController
  Character/     MergeCharacter (movement + camera foundation)
  Combat/        (empty — future)
  Interaction/   (empty — future)
  Inventory/     (empty — future)
  Quest/         (empty — future)
  AI/            (empty — future)
  Save/          (empty — future)
  World/         (empty — future)
  UI/            (empty — future)
  Data/          Shared structs (attributes block starter)
  Systems/       (empty — future)
```

**Rule:** C++ owns rules and systems. Blueprint configures assets and exposes designer knobs.

## Enhanced Input

Use Enhanced Input (already in `Merge.Build.cs` and `DefaultInput.ini`).

## Validation checklist (local)

- [ ] Project opens in UE 5.8.1
- [ ] C++ compiles without errors
- [ ] BP_MergeCharacter inherits AMergeCharacter
- [ ] Move / Look / Jump work in L_TestArena
- [ ] No secrets in repo
