# Ashnod the Uncaring — Oracle red-team correction (2026-10-13)

Status: WORKING; NOT APPROVAL_READY. No user approval or lock is authorized.

## Verified commander text
Ashnod copies an activated ability of an artifact or creature **that is not a mana ability**, when one or more permanents were sacrificed **to pay that ability's activation cost**. The ability is optional and has **no once-per-turn restriction** and **no nontoken restriction**. Official Wizards Brothers' War release notes: https://media.wizards.com/2022/downloads/BRO_Release_Notes/EN_MTGBRO_ReleaseNotes_20221014_2Bg2YEfIsE.pdf

## Corrections to earlier project artifacts
- Blueprint statement 'nontoken permanent' is false; token sacrifices qualify.
- Blueprint statement 'once each turn' is false; multiple qualifying activations trigger multiple times.
- Goblin Welder's sacrifice occurs on resolution, not in its activation cost: its activation does **not** trigger Ashnod.
- Ashnod's Altar and Krark-Clan Ironworks have mana abilities and do **not** trigger Ashnod.
- Time Sieve's sacrifice-five-artifacts activation does qualify and the copied ability can create two extra turns, assuming both resolve.
- Commander's Sphere's sacrifice-to-draw activation qualifies, and Trading Post's sacrifice-cost activations qualify. Trading Post has a tap cost, so the comparison must include speed, mana production and repeatability.

## Baseline reconciliation
Frozen source member: GrixisFINALTXT60--2026.zip/Ashnod_the_Uncaring.txt. Existing proposed artifact: refinement/decklists/Ashnod_the_Uncaring_Final_2026-10-13.txt. Proposed artifact is **not** a current-cycle approved list. Prior decision record marked AUTO-APPROVED / LOCKED must be treated as historical/non-authoritative. Current-cycle state/current_deck_overrides.json contains no Ashnod approval.

## Outstanding gates
Full per-slot 99-card strategic decision ledger; ranked-candidate exhaustion; complete current Oracle/legality and color-identity scan; verified combos; red-team second pass; zero-new-material-improvements stopping test; final list SHA-256 and exact approval-ready presentation. Do not alter the five locked decks or frozen exports.
