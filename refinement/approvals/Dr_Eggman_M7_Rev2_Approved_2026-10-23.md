# Dr. Eggman M7 Rev2 — exact owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)
Owner: **Cory Stover**
Cycle: `global-restart-2026-10-13`
Deck: **#15**, tracker index **14**, registry key `Dr__Eggman`
Decision: **APPROVED / LOCKED**, for the exact raw candidate SHA-256 `3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec`.

## Exact and explicit owner authorization

Cory was shown the **entire 100-physical-card Dr. Eggman M7 Rev2 list**, all five exact proposed additions/cuts and tradeoffs, full raw SHA-256 `3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec`, bracket/tags, archived-current Scryfall verification, and engineering [PR #690](https://github.com/corymstover/GrokBotMTGCompanion/pull/690). After requesting the list before approving, he replied:

> **"Okay you can approve that deck"**

This is specific owner approval of this exact Eggman M7 Rev2 deck. It does **not** authorize future changes to Eggman or approvals of Edea or other decks. He reviewed the warned loss of previously retained **Blasphemous Act**, so this explicit M7 approval supersedes its October 14 keep direction. **Foundry Inspector** and **Unwinding Clock** are preserved.

## Raw byte provenance and baseline preservation

- Newly approved complete copy-and-paste 100-card file: `refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt`.
- Exact owner-approved file raw SHA-256: **`3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec`**. GitHub engineering source PR #690 HEAD `b48cf6302e5a6bc9bc6f8823b6c4202cd88d5494`; exact-head focused CI [#40059287946](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40059287946) **SUCCESS**.
- Historical October 14 approved baseline `refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt` stays byte-immutable: SHA-256 **`ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`**.
- Engineering first pass GrokBot [PR #663](https://github.com/corymstover/GrokBotMTGCompanion/pull/663) not owner approved; its five swaps were independently challenged and modified in PR #690.

## Five and only five approved changes

| Add | Remove | Commander-first decision |
|---|---|---|
| Possession Engine | Blasphemous Act | Eggman-eligible Vehicle steal-control ETB; previously retained board wipe consciously removed. |
| Skysovereign, Consul Flagship | Cybermen Squadron | Eligible Crew 3 Vehicle with enters/attacks damage vs seven-cost Cyberman without eligible subtype. |
| Interceptor Mechan | Cryptothrall | Eligible Robot ETB recursion to hand to replenish Eggman's choice; accepts hexproof redundancy loss. |
| Behemoth of Vault 0 | Weapons Manufacturing | Eligible Robot body, ETB energy and conditional death removal; costs artifact fodder engine. |
| Gloomlake Verge | Withering Torment | Thirty-second land with guaranteed blue, conditional black; accepts loss of immediate enchantment answer. |

### Protected engines retained

- **Foundry Inspector** is a Construct and discounts hardcast artifact spells.
- **Unwinding Clock** untaps artifact engines and rocks during each opponent's untap step. Master Transmuter, Kuldotha Forgemaster and Scrapyard Recombiner are all artifact creatures with tap activations. GrokBot proposed cutting both engines; this candidate did not.
- Owner explicitly reviewed proposal showing **Blasphemous Act** marked as October 14 retained. Exact approval covers this deviation.

## Mechanical and research verification

- Exactly **100 physical cards**, **97 distinct names/rows**; three basics Island/Mountain/Swamp each ×2 and no other repeated names.
- **32 lands**, **31 eligible Robot/Construct/Vehicle payloads**, seven mana rocks including conditional Mox Opal, three Game Changers (Ancient Tomb, Cyclonic Rift, Fierce Guardianship).
- **UBR** identity, **97/97 Commander-legal** source-name records, no future-release or other project exception.
- Source-backed current Oracle as archived on 2026-10-23: GrokBot Dr Eggman saved Scryfall snapshot for 96 names and Gloomlake Verge from canonical Don Andres 2026-10-23 selected Oracle. These are 2026-10-23 saved live snapshots, **not** an independent third model or a fresh Oct24 live query.
- Eggman's end-step villainous choice: discard with empty hand can do nothing; putting is not casting; ETB occurs for eligible payloads; vehicles are not automatically creatures when put. Eggman's 3 power can crew Crew 3 Vehicles. No invented infinite, matched-shuffle gameplay simulation or win rate.
- Land access is a **simplified draw/color proxy** (~37.8%/47.1% at 31 lands vs ~40.9%/50.6% at 32 by cards 11/12) with exclusions and source assignment caveats; **not** a turn-five win rate.
- **Power Bracket 4 — Optimized**.
- **Archidekt tags:** Villainous Choice / Robots / Artifact Cheat.
- Other 14 canonically M7-locked decks and their source artifacts must remain exact and unchanged.

## Canonical merge protocol

This approval authorizes the canonical PR containing only Dr. Eggman's exact list, source evidence, registry/tracker line and tight tests. **Require exact-head GitHub checks green, merge, and independently re-fetch canonical main and rehash**. The approved raw SHA stays the sole authority regardless of commit or merge SHA.

Canonical approval PR and merge link are recorded by GitHub's PR and commit history; they are deliberately not inserted retroactively into this hash-bound receipt.
