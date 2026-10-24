# Doctor Doom, King of Latveria M7 Rev2 — exact owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Owner: **Cory Stover**  
Cycle: `global-restart-2026-10-13`  
Decision: **APPROVED / LOCKED**, Deck #13/tracker index 12, raw SHA-256 `7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20`.

## Exact user authorization and scope

After receiving the full Doctor Doom, King of Latveria M7 Rev2 100-card list, all nine precise add/cuts, its exact raw SHA-256, and engineering PR #688 verified SUCCESS at head `0a20ca02ecb680f9230fc5fcae7eda1f8ae5195d`, Cory expressly replied:

> Approved

This approves **only the exact 100-card raw UTF-8 list**, `7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20`. It authorizes the Doctor Doom canonical approval PR, merge and hash-locked update, **not** any change to Deck #14 Don Andres, other locked decks, source-baseline exports or project governance.

Approved file: `refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt`. SHA-256 7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20; 100 physical cards and 100 names, one commander, 99 unique library cards, final LF.
Historical Oct14 owner-approved file: `refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt`, raw SHA-256 `c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58`; preserved byte-for-byte with its approval context.

## Nine exact approved substitutions

| Added | Removed | Commander-first benefit and tradeoff |
|---|---|---|
| Lightning Axe | Big Score | Cheap red instant land-discard casting cost and removal; loses four-mana card draw/Treasures. |
| Glint-Horn Buccaneer | Green Goblin, Revenant | Hasty per-card discard damage; retains Change of Fortune's refill rather than Grok's original cut. |
| Red Ghost, Intangible Genius | Loki, the Deceiver | Doom's second combat draw repeatedly creates hasty Ape Villains for multiple on-theme ETB effects; loses attacking-copy upside. |
| Coastal Peak | Shipwreck Marsh | Mountain/Island land cycling is an independent discard; enters tapped and replaces conditional-untapped UB. |
| Swiftfoot Boots | Unexpected Windfall | Protects Doom with own-target-safe hexproof; loses one instant burst draw/Treasure. |
| Mox Diamond | Fellwar Stone | Zero-mana all-color rock preserving seven-rock count, can discard land after Doom arrives; costs a land card and triggers no earlier Doom. |
| Withering Torment | Feed the Swarm | Keeps enchantment answer and upgrades to instant speed/flat two life; costs three mana. |
| Molten Vortex | Kang, Temporal Tyrant | One-red reusable separate land-discard damage engine; trades a four-mana Villain second-draw payoff. |
| Tolaria West | Geier Reach Sanitarium | Activated sorcery-speed land discard tutoring any MV-0 land/Mox; loses repeatable colorless group loot but taps for U. |

## Independent gate results

- **Exactly 100** physical cards, 100 distinct named entries; commander first and annotated, no excess companions, only singleton 1x.
- **38 lands, seven mana rocks** (Sol Ring, Arcane Signet, Mox Diamond, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence, The Soul Stone).
- **100/100 Scryfall Oracle IDs, names and text; 100/100 Commander legal; 100/100 color identities within U/B/R.** 98 identities from Oct23 PR #661 231-card direct API archive, two named-card direct API queries for Molten Vortex and Tolaria West Oct23.
- **Seven Game Changers:** Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Mox Diamond, Vampiric Tutor. **Power Bracket 4 — Optimized**.
- Archidekt tags: **Land Discard / Villains / Connive**. **No project exceptions**.
- `Doctor Doom, King of Latveria` drains two life to **each** opponent per **event** discarding one or more land cards, not per land in a single wheel; Glint-Horn separately deals one per **card** discarded.
- Molten Vortex costs R for each individual land discard, and its damage needs a legal target. Mox Diamond only triggers Doom if he was already present for its replacement discard. Tolaria West is activated only as sorcery for {1}{U}{U} and can find MV-0 lands or Mox.
- Swiftfoot Boots hexproof allows own Doom combat targeting; Lightning Greaves shroud does not. Restricted mana from Villainous Hideout cannot pay non-Villain Molten Vortex/Seismic Assault activation.
- Dakmor Salvage / Tectonic Reformation / Surly Badgersaur repeatable cycle/dredge line is **finite/library-bounded**, not a deterministic infinite loop; relevant graveyard hate/counterplay remain.
- Eight full 100-card counterfactual configurations archived and candidate-specific mechanical tests passed. There were no measured matched-opening multiplayer games or win-rate claims; the archived owner-equivalent non-independent M6 Pass C was **not** re-sealed.

## Exact-head evidence and canonical execution

- Engineering [PR #688](https://github.com/corymstover/GrokBotMTGCompanion/pull/688), head `0a20ca02ecb680f9230fc5fcae7eda1f8ae5195d`, [CI #40057650413](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40057650413) **SUCCESS**; candidate byte-exact re-fetched independently and SHA-256 matched `7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20`.
- Preserve all 12 earlier M7 owner-approved locks and historic Oct14 Doctor Doom file; registry/test/tracker changes only to Doctor Doom.
- Canonical PR exact-head CI and main post-merge fetch/rehash are mandatory; this document records authorization **and verification intent**, not an unearned post-merge success until independently checked.

