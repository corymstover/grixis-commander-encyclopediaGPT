# Crosis, the Purger — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Blizzard Specter; Recoil. Cut: Specter's Shroud; Chaos Warp.
- Final list: 100 copies, 92 distinct names, 36 land copies; singleton compliance verified. Commander first.
- Revised TXT SHA-256: `449d7c02655713e05cc1051c8461dd36061ae1b85eaa9a8bef6595198b36dfc3`.
- Baseline raw CSV SHA-256: `c5f8c7a28a38941a5f35c95d9c8da9cb3ba08c973d4a7ec8d51220d806d3a677`.
- Baseline raw TXT SHA-256: `bbd4acc84ff0abd5f43045bd28d9cc4a154cbfe2592923967315b9a1497c4435`.
- Normalized baseline hash: `11f7ac19d46c1caae2e598307f78f5f00f2dc8885a57d9d87e19f44c646cb848`.

## Commander-first plan and change rationale

Crosis is a flying commander whose combat damage can be converted into a color-based discard effect for {2}{B}. The deck supports repeated combat connections with evasion, hand disruption, discard payoffs, and control.

Blizzard Specter is a four-mana 2/3 flying Snow Specter. Whenever it deals combat damage to a player, choose whether that player returns a permanent they control to its owner’s hand or discards a card. The bounce mode is tempo, not permanent removal, and the opponent chooses the permanent returned. It replaces Specter’s Shroud, an equipment that adds +1/+0 and one discard trigger but requires paying its equip cost.

Recoil costs {1}{U}{B}, returns any target permanent to its owner’s hand, then makes that player discard a card. It replaces Chaos Warp, which shuffles the target into its owner’s library and may put a random permanent from the top of that library onto the battlefield. Recoil adds discard synergy but is less definitive removal; Cyclonic Rift, Feed the Swarm, Bedevil, Damnation, Toxic Deluge and other interaction remain.

Direct current Oracle / legality references: [Blizzard Specter](https://mtg.wtf/card/ima/194/Blizzard-Specter), [Recoil](https://mtg.wtf/card/dmr/197/Recoil), [Specter's Shroud](https://mtg.wtf/card/dst/142/Specters-Shroud), [Chaos Warp](https://mtg.wtf/card/cmm/243/Chaos-Warp), [Crosis](https://mtg.wtf/card/inv/242/Crosis-the-Purger). All are Commander-legal; final list fits UBR. Official Commander banned list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 92 lines with quantities, commander first; quantity total 100.
- CSV: 92 rows, quantity sum 100, unique names 92.
- Current project-wide Scryfall metadata refresh generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; final names reconcile against that refresh. The two accepted cards and paired cuts directly checked.
- Candidate triage: 16 candidates; 2 accepted, 2 retained, 1 cut, 11 rejected.
- Strategy review covers discard density, combat connection, evasion, removal, ramp, draw and land count. No numerical goldfish or matched-seed multiplayer test; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
