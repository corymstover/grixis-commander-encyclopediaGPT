# Edea, Possessed Sorceress M7 Rev2 — exact owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)
Owner: **Cory Stover**
Cycle: `global-restart-2026-10-13`
Deck: **#16**, tracker index **15**, registry ID `Edea__Possessed_Sorceress`
Status: **APPROVED / LOCKED** for raw SHA-256 `a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`.

## Explicit authorization and bounded scope

After reading the **entire Edea M7 Rev2 100-card list**, its five substitutions and rationale, exact candidate SHA-256 `a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`, [engineering PR #691](https://github.com/corymstover/GrokBotMTGCompanion/pull/691), focused verification, and Bracket 4/tags, Cory replied **"Approved"** on 2026-10-23. This exact approval supersedes Edea's October 14 current list; it does not authorize reopening any other commander.

## Exact raw evidence and preservation

- Approved new artifact: `refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt`.
- SHA-256 **`a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`**, exact engineering source head `734f2c2b18697e3b420697ac8c3a9bc134b183f1`, focused successful Actions runs [#40062061450](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40062061450) and [#40062034383](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40062034383).
- Historical 2026-10-14 approved file **not overwritten**: `refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt`, raw SHA **`fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`**.
- GrokBot research [PR #664](https://github.com/corymstover/GrokBotMTGCompanion/pull/664) is historical first-pass evidence, not the selected candidate.

## Five approved changes

| Add | Cut | Strategic tradeoff |
|---|---|---|
| Aggravated Assault | Mass Mutiny | Repeatable five-mana additional combats and theft rather than immediate one-shot up-to-three borrowed creatures. |
| Kaya's Ghostform | Zara, Renegade Recruiter | One-mana Ghostform + same-turn sacrifice of an Edea theft, order simultaneous death triggers to retain stolen creature and still draw; gives up five-mana hand-theft body. |
| Hall of Echoes | Shipwreck Marsh | Five-mana land activation to copy Edea until end of turn, legend-rule waiver; pays a real U/B untapped dual-source cost and can be vulnerable while creature. |
| Geyadrone Dihada | Village Rites | More repeatable theft/corruption and ultimate control; loses the efficient one-black-mana sacrifice/draw-two. |
| Combat Celebrant | Seize the Spotlight | Combat exert creates an extra combat and another Edea trigger; loses a one-shot political multi-opponent theft/card/Treasure choice. |

**Owner-kept Evereth and High Market preserved. Ayara likewise preserved. No repeatable sacrifice outlet lost.**

## Mechanical gates and caveats

- Exactly **100 physical cards**, **94 names**, only Island/Mountain/Swamp each ×3; **35 lands**, **six rocks**; **three Game Changers** (Ancient Tomb, Demonic Tutor, Fierce Guardianship).
- Archived **live 2026-10-23** Scryfall source checks 94/94 Oracle names, Commander legality and UBR identities. This is a selected snapshot from GrokBot's verified pool, **not** a new independent October 24 live query. No project exceptions.
- Edea theft each beginning of combat; Assault only sorcery activation; Celebrant must attack/exert and does not untap next ordinary untap; Ghostform death trigger timing plus Edea draw; Hall {5} clone with legend suppression; Dihada's −3 targets creatures or planeswalkers.
- Deterministic 140,000-sample draw/color-access approximation implies about **0.7–0.8 percentage points** reduction in modeled five-mana UBR access after Hall replaces Shipwreck Marsh. Not a gameplay simulation, mulligan policy, exact cast rate or match win rate.
- No independent third-model or comprehensive historical suite-green claim. **Bracket 4 — Optimized**, Archidekt tags **Theft / Extra Combats / Aristocrats**.
- Only Edea's registry entry/tracker row change; previous **15 M7 locks** must stay exact.

## Canonical release protocol

This receipt records owner approval **before** the PR completes. Verify exact-head canonical CI, merge PR without replacing historical approved source, re-fetch canonical main, recompute exact `a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`, and confirm registry and tracker. Commit history is the authoritative merge reference; do not invent a PR or merge SHA in this pre-merge file.
