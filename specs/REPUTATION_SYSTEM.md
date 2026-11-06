# Merge — Reputation System Specification

**Status:** SPÉCIFIÉ — système canonique en préproduction
**Engine:** Unreal Engine 5.8.4

---

## 1. Overview

The reputation system tracks the player's standing with factions, organizations, and communities in the world of Merge. Reputation affects how NPCs and factions respond to the player, influencing dialogue, trade opportunities, quests, and consequences in the game world.

## 2. Definition

**Reputation** : A quantified measure of how a faction or organization perceives and responds to the player based on past actions, alignment, and interactions.

Reputation is distinct from individual NPC relationships:
- **Reputation** : faction-level standing (affects multiple NPCs of that faction)
- **Individual relationship** : personal connection with a specific NPC (may differ from faction reputation)

A player may have high reputation with the Skeleton Kingdom but still have conflict with an individual Skeleton NPC.

## 3. Factions and Organizations

Reputation exists with the following factions and organizations:

### Major Factions
- **Humans (Royaume de la Fantaisie)** : the human kingdom, its monarchy, and institutions
- **Skeletons / Nécromentiens (Royaume de la Dark Fantaisie)** : the Skeleton Kingdom and its government
- **Kima Vé (Royaume de la Light Fantaisie)** : the magical beings and the Kiyeka collective government
- **Gork Tribes** : tribal organizations (details pending)

### Minor Factions and Organizations
- **Underground organizations** : criminal networks, resistance groups, hidden societies
- **Religious organizations** : temples, religious orders, priesthoods
- **Guilds and professional associations** : merchant guilds, adventurer organizations, craft guilds
- **Specific communities** : villages, settlements, regional populations

### Faction Details

To be defined during further development:
- Which factions are active in each region
- Which factions overlap or conflict
- Geographic scope of each faction's influence

## 4. Reputation Scale

**Canonical scale (To be defined) :**

The exact numerical representation of reputation is to be determined. Possible approaches:

- **Option A (Pending):** Linear scale (e.g., -100 to +100)
- **Option B (Pending):** Tiered levels (e.g., Hated, Disliked, Neutral, Liked, Honored)
- **Option C (Pending):** Hybrid system combining numerical and narrative tiers

**Current status:** À DÉFINIR

## 5. Progression and Mechanics

### How Reputation Changes

Reputation with a faction changes based on player actions that are perceived to benefit or harm that faction:

- **Actions that increase reputation:** helping faction members, completing faction quests, advancing faction goals, defending faction interests
- **Actions that decrease reputation:** harming faction members, betraying faction trust, aiding enemy factions, opposing faction goals
- **Neutral actions:** do not change reputation

### Validation

Not every action automatically changes reputation. Changes must be validated by:
- Context appropriateness
- Intentionality (farming prevention)
- Impact significance

### Rate of Change

To be determined: how quickly reputation increases or decreases, and whether significant thresholds exist.

## 6. NPC and Faction Reactions

### NPC Behavior

Reputation affects how NPCs respond to the player:

- **Dialogue and interactions:** NPCs may refuse to talk, offer special dialogue, or provide additional information
- **Trade:** merchants may offer better prices, special items, or refuse service
- **Quests:** faction-specific quests become available or unavailable based on reputation thresholds
- **Hostility:** low reputation may cause NPCs to become hostile, refuse aid, or report the player to authorities
- **Special opportunities:** high reputation may unlock secret quests, locations, or items

### Faction-Level Consequences

Factions may react collectively to the player:

- Travel restrictions in faction territory
- Bounties or contracts issued against the player
- Alliance shifts (factions may aid or oppose the player based on reputation with rival factions)
- Access to faction resources, services, or territories
- World events triggered by faction actions

## 7. Relationship Between Reputation and World State

Reputation is part of the persistent world state:

- Reputation changes persist across game sessions
- Faction reactions are reactive to world state (if reputation is high with Humans but low with Skeletons, world events reflect this tension)
- Factions remember player actions and adjust behavior accordingly
- Reputation can be recovered but may take time and effort

## 8. Integration with Other Systems

### Progression System

Reputation is independent of the skill progression system:
- Gaining reputation does not directly grant skill points
- Losing reputation does not reduce skills
- Reputation may influence quest difficulty or rewards, which indirectly affect skill progression

### Combat System

Reputation may affect combat encounters:
- Faction members may assist or oppose the player based on reputation
- Enemies may prioritize or ignore the player based on faction affiliation
- Neutral or friendly faction members may refuse to engage in combat against the player

### Magic and Spells

Some spells or magical effects may be faction-restricted:
- Faction NPCs may teach spells only to allied players
- Using magic in certain ways may damage reputation with specific factions

## 9. Mechanical Details (To Be Defined)

The following specifics remain to be decided:

- **Exact numerical scale** for reputation representation
- **Reputation thresholds** at which NPC behavior changes
- **Rate of reputation gain/loss** per action
- **Maximum and minimum reputation values**
- **Whether reputation can be reset or "forgiven"** over time
- **Specific consequences per faction** (which services are locked, which quests become available)
- **Whether hidden reputation exists** (factions tracking player actions without the player knowing)
- **Cross-faction reputation mechanics** (whether helping one faction damages another automatically, or whether each faction is independent)

## 10. Design Principles

- **Reputation is consequence-based:** player actions have lasting effects on how the world perceives them
- **Reputation is not binary:** a player can have complex relationships with different factions
- **Reputation rewards diverse playstyles:** a player can be honored by one faction while hunted by another
- **Reputation supports roleplaying:** players can pursue specific faction goals or attempt reconciliation
- **Reputation is persistent:** the world remembers what the player does

## 11. Scope Clarification

This specification documents how reputation functions in the game world. It does NOT specify:

- Detailed quest content tied to reputation
- Specific NPC dialogue based on reputation (that belongs in dialogue systems)
- Exact numerical values or thresholds (pending further game design decisions)
- Specific faction stories or lore (that belongs in GAME_BIBLE.md and faction documents)
- Implementation details in Unreal Engine (that belongs in technical architecture)

## 12. Status Summary

- **Mechanics:** SPÉCIFIÉ (system principles and architecture defined)
- **Numerical values:** À DÉFINIR (scale, thresholds, rates pending)
- **Faction-specific consequences:** À DÉFINIR (per-faction details pending)
- **Implementation in Unreal:** À DÉFINIR (Phase 2 and beyond)

---

**Last updated:** 2026-10-02
**Status:** SPÉCIFIÉ — Préproduction Phase 0
**Next step:** Define numerical scale and faction-specific mechanics
