# Merge

Action-RPG with intentional PS1 aesthetic.  
**Engine:** Unreal Engine 5.5 · **Primary language:** C++ · **Complementary:** Blueprint

## Status

| Phase | Status |
|-------|--------|
| 0 — Vision / Game Bible | Done |
| 0.5 — AI infrastructure / security | Done |
| 1 — UE5 foundation | Scaffold ready — compile & assets local |
| 2+ | Not started |

## Quick links

- [GAME_BIBLE.md](GAME_BIBLE.md) — vision
- [specs/TECHNICAL_ARCHITECTURE.md](specs/TECHNICAL_ARCHITECTURE.md) — technical architecture
- [docs/UE5_SETUP.md](docs/UE5_SETUP.md) — local UE5 setup
- [ROADMAP.md](ROADMAP.md) — phases
- [ai/](ai/) — multi-agent protocol + runtime guards

## Structure

```
Merge.uproject
Source/Merge/     C++ module (Core, Character, …)
Content/          Maps, Blueprints, Input (Editor assets)
Config/           DefaultEngine, Input, GameplayTags
ai/               AI orchestration + security runtime
specs/            Architecture docs
```

## Local first steps (Phase 1)

1. Install **UE 5.5**
2. Generate project files from `Merge.uproject`
3. Compile
4. Create Blueprints + `L_TestArena` as described in `Content/README.md`
5. PIE → verify move / look / jump

See `docs/UE5_SETUP.md` for the full checklist.
