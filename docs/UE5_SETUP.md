# Merge — UE5 Local Setup (Phase 1)

## Engine version

**Unreal Engine 5.8.4** (required project version).

If you use another 5.x, update `Merge.uproject` → `EngineAssociation` and the `IncludeOrderVersion` in the Target files.

## Prerequisites

- Unreal Engine 5.8.4 installed via Epic Games Launcher
- Visual Studio 2022 (Windows) with “Game development with C++” workload  
  or Xcode (Mac) / appropriate Linux toolchain
- Git

## First open

1. Clone / open the repository.
2. Right-click `Merge.uproject` → **Generate Visual Studio project files** (or open with UE; it will offer to rebuild).
3. Open `Merge.uproject` with UE 5.8.4.
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

`AMergeCharacter` reads its Move, Look, Jump, Interact, and Sprint actions from
the character defaults. Create and assign those `Input Action` assets in
`BP_MergeCharacter` (or a child Blueprint), then map them in the input mapping
context assigned to `AMergePlayerController::DefaultMappingContext`.

For the ground movement prototype, configure Move as a 2D axis action and map
WASD plus the left gamepad stick. Configure Sprint as a digital action and map
Left Shift plus a gamepad face/shoulder button; sprint is active only while
held. Set `Walk Speed`, `Sprint Speed`, and `Movement Rotation Rate` on the
character defaults to tune the feel. The C++ defaults are 300 cm/s, 600 cm/s,
and 500 degrees/s respectively. Movement is camera-yaw-relative and the
character rotates toward its movement direction. No skeletal mesh or animation
blueprint is required for the movement logic itself.

## Character attributes prototype

`AMergeCharacter` includes a `UMergeAttributeComponent` for health and stamina.
The defaults follow `specs/COMBAT_SYSTEM_SPEC.md`: 100 health, 100 stamina,
stamina regeneration at 15 points/second after 0.5 seconds without spending,
and sprint cost at 5 points/second. Sprint stops automatically when stamina is
insufficient. The component exposes health/stamina change events and a defeat
event for Blueprint UI and later combat integration; defeat does not yet add
death, respawn, or world-state behavior.

To smoke-test in Unreal, compile the `MergeEditor` target, create/open a test
map with a Player Start, set `AMergeGameMode` (or a child Blueprint) as the
GameMode, and possess `AMergeCharacter` (or its child Blueprint). Assign the
Move and Sprint actions as described above. In PIE, hold Sprint while moving:
the character should run faster, stamina should fall, then recover after the
configured delay when Sprint is released. With no UI yet, inspect
`AttributeComponent` on the possessed character in the Blueprint debugger or
bind its `OnStaminaChanged` event to a temporary Print String. `ApplyDamage`,
`RestoreHealth`, `TrySpendStamina`, and `RestoreStamina` are callable from C++
and Blueprint for prototype testing.

## Validation checklist (local)

- [ ] Project opens in UE 5.8.4
- [ ] C++ compiles without errors
- [ ] BP_MergeCharacter inherits AMergeCharacter
- [ ] Move / Look / Jump work in L_TestArena
- [ ] No secrets in repo
