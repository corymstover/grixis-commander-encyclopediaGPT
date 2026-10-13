# Doctor Doom, King of Latveria — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Glorious Purpose. Cut: The Soul Stone.
- Final list: 100 copies, 100 distinct names, 38 land copies; singleton compliance verified. Commander first.
- Revised TXT SHA-256: `f672df6cbf80b48cd727a5e28dbea4afe13b68b7ba7fed464bacfc83c6c322cc`.
- Baseline raw CSV SHA-256: `99e5c2b5a0451af0deb649efa32bbadfbbe0160eabbbe556b0feb7b0bfa675ef`.
- Baseline raw TXT SHA-256: `952edac4f4a1212e0e75266bd2c16b26b27ac16b3db3ce5a61689a7006bbf72b`.
- Normalized baseline hash: `5593c4d626034f4b46975a9bbd207f5e13e8eb8519b30ea9aefc4ab86c72bf4f`.

## Commander-first plan and change rationale

Doctor Doom, King of Latveria triggers whenever you discard one or more land cards, making each opponent lose 2 life. At the beginning of combat on your turn, a Villain you control gains menace and connives. The deck retains its land-discard package—Seismic Assault, Tectonic Reformation, Trade Routes, Change of Fortune, Dark Deal, Big Score, Unexpected Windfall, Geier Reach Sanitarium, and other discard outlets—alongside Villain connive engines.

Glorious Purpose costs {1}{U}. Whenever a creature you control connives, it gets a +1/+1 counter and Glorious Purpose gets a plan counter. When its sixth plan counter is put on it, sacrifice it, exile the top four cards of your library, cast any number of spells among them without paying their mana costs, and put the rest into your hand. The commander guarantees a connive each combat; Kang, Leader, M.O.D.O.K., Baron Strucker and Lethal Scheme provide additional connive opportunities.

The Soul Stone is cut as a deliberate trade. It costs {1}{B} and taps for black, but its recursion engine requires {6}{B}, tapping it and exiling a creature you control before the upkeep reanimation ability becomes active. The list retains other recursion through Reanimate, Oskar, Moonstone and Crucible of Worlds.

Direct current Oracle / legality references: [Glorious Purpose](https://mtg.wtf/card/msc/31/Glorious-Purpose), [The Soul Stone](https://www.mtg.wtf/card/spm/243/The-Soul-Stone), [Doctor Doom, King of Latveria](https://mtg.wtf/card/msc/6/Doctor-Doom-King-of-Latveria). All are Commander-legal; all final card identities fit UBR. Official Commander banned list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 100 lines with quantities, commander first; quantity total 100.
- CSV: 100 rows, quantity sum 100, unique names 100.
- Current project-wide Scryfall metadata refresh generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; final names reconcile against that refresh. Glorious Purpose, The Soul Stone and commander directly checked.
- Candidate triage: 16 candidates; 1 accepted, 5 retained, 10 rejected with reasons.
- Strategy review covers land-discard outlets, connive frequency, Villain density, ramp, draw, interaction, recursion and land count. No numerical goldfish or matched-seed multiplayer test; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
