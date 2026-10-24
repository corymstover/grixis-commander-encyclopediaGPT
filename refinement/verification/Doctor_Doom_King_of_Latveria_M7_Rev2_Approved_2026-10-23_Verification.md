# Doctor Doom M7 Rev2 canonical verification — owner-approved exact 100

**Result intended:** exact owner-approved candidate, pending canonical PR exact-head CI and main post-merge rehash.  
**Owner reply:** `Approved` to complete nine-swap Doctor Doom M7 Rev2 list and raw SHA on 2026-10-23 America/Chicago.  
**Exact raw SHA-256:** `7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20`.  
**Canonical artifact:** `refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt`.  
**Historical Oct14 source:** `refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt` → `c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58`; preserve unchanged.

## Source-bound full-list verification

| Check | Result |
|---|---|
| Cards | 100 physical; commander first, 99 unique library cards; singleton PASS |
| Names | 100 distinct; one each of Island, Mountain and Swamp; no repeats |
| Lands and cheap ramp | 38 lands, seven mana rocks |
| Scryfall Oracle | 100 current source records, IDs and complete text, 98 archived Oct23 live Scryfall PR #661 and two direct Scryfall named/API Molten Vortex/Tolaria West Oct23 |
| Commander legality | All 100 legal officially as of checked records; color identities ⊆ U/B/R; no exceptions |
| Game Changers | Seven: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Mox Diamond, Vampiric Tutor |
| Power and tags | Bracket 4 — Optimized; Land Discard / Villains / Connive |
| Delta | Exactly nine new cards and nine cuts against byte-exact Oct14 baseline |
| Engine interaction | Separate land discard events, connive timing, Mox replacement, Tolaria transmute, Swiftfoot hexproof, Coastal cycling verified |
| Finite loop | Dakmor / Tectonic / Surly is library-limited. No unbounded/infinite claim |
| External research | PR #688 nine swaps and eight 100-card variants; EDHREC/Scryfall used as inputs, not proof by popularity |
| Gaming simulations | No measured matched-openings/multiplayer win-rates; no invented claims |

## Key edge-case proof

- Doctor Doom's one-or-more-land ability occurs once for each land-discard event; three individually paid Molten Vortex activations create three Doom life-loss triggers while a wheel discarding three land cards simultaneously yields only one. Glint-Horn Buccaneer has its own per-card trigger.
- Mox Diamond's discard is an as-it-enters replacement; ramping with Mox before Doom is online doesn't retroactively drain. It requires a land card in hand.
- Tolaria West itself is a land so transmuting it counts as discard while Doom is present; cost {1}{U}{U}, activated as a sorcery, tutors mana-value-zero lands and Mox Diamond. The tutor does not access MV3 Seismic Assault.
- Change of Fortune counts every card previously discarded during the same turn plus its own discarded hand. Losing Big Score and Unexpected Windfall reduces four-mana instant burst resources but keeps Change/Wheel/Windfall/cheap outlets and seven rocks.
- Low-source red hands and graveyard hate remain meaningful counterplay. Villainous Hideout mana cannot pay Molten or non-Villain costs. No claim that finite Dakmor ends a multiplayer game through guaranteed deterministic infinite.

## Checkpoints for actual canonical lock

1. Fetch exactly PR #688 head `0a20ca02ecb680f9230fc5fcae7eda1f8ae5195d`, confirm workflow #40057650413 SUCCESS and bytes/hash.
2. Confirm unchanged canonical Oct14 approved baseline exact hash, existing 12 new-cycle lock entries and 62 tracker rows.
3. Commit candidate, selected 100-card Oracle, approval record, this verification, **Doctor Doom-only** registry/tracker, and isolated approval tests to canonical branch PR.
4. Run exact-head PR CI and regression tests for all 12 prior M7 locks; do not claim historical full pytest suite PASS.
5. Merge only after exact-head CI PASS; independently fetch new canonical `main` approved file and confirm raw SHA and only intended registry/tracker entry.

