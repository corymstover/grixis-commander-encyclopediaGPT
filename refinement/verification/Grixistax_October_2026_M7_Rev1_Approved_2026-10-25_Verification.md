# Deck #27 — Grixistax M7 Rev1 source, rules, and canonical preservation verification

**Owner-approved SHA-256:** `70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e` (raw UTF-8, one terminal LF). Original October 14 lock: `f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c`.

## Exact physical audit

- Two Partner commanders: `Kraum, Ludevic's Opus` and `Tevesh Szat, Doom of Fools`. Two `[Commander]` rows, 98 library cards, 100 physical cards, 100 distinct names, 26 lands, no companion.
- Exactly five additions and five removals: +Arcane Signet / −Mox Amber; +Bitterblossom / −Magus of the Moon; +Opposition / −Ashiok, Dream Render; +Phyrexian Altar / −Damping Sphere; +Ophiomancer / −Sheoldred, the Apocalypse.
- Preserves Kraum's second-spell trigger, Tevesh's Thrull and draw abilities, Contamination/Skullclamp/Tangle Wire/Overburden/Karn/Orb prison, Helm + exile and Breach/LED/Brain Freeze packages, both wheels and Narset/Notion Thief.
- Official Commander legality source record count 100, Grixis color identity, 22 Game Changers, no exceptions. The selected index has 98 names from live Scryfall's 2026-10-23 archived 214-name set and two new name/page checks on 2026-10-25 (Ophiomancer and Phyrexian Altar). The two page-only entries intentionally lack an Oracle ID and are not characterized as fresh API collection records.

## Changed-case transfer, not automatic reuse

The original Grixistax Grok I/J candidate from [PR #675](https://github.com/corymstover/GrokBotMTGCompanion/pull/675) was a **different two-swap research 100**, not proof of Rev1. Instead, the independent exact approved-100 test suite `tests/test_m6_grixistax_rev1_case_transfer.py` executed **15** blueprint required cases: P0 `C1 C2 K1 K2 K3 F1` and P1 `K4 K5 E1 E2 W1 W2 W3 F2 F3`. It also checked the 100 current/archived Scryfall identity/legality rows. Engineering [PR #705](https://github.com/corymstover/GrokBotMTGCompanion/pull/705) exact head `dca07c0f58e751398ecc2d29753da4a65542bb14`, focused [CI #40175693250](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40175693250) SUCCESS. Overall [M7 CI #40175693200](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40175693200) SUCCESS.

Affected source cases are **re-adjudicated**: Kraum's second-spell trigger now through retained Trinisphere without removed Damping Sphere; mana-lock E2 replaces Magus/Damping parity with Opposition, Bitterblossom and Phyrexian Altar; Breach K5/F3 considers Trinisphere and Chalice; W3 no longer claims Sheoldred damage or life gain. This explicit changed-source mapping is in `refinement/verification/m7_certification_transfer/Grixistax___October_2026_70b48148409e849e.json`.

### Important rules costs and negatives

- Bitterblossom and Contamination: order simultaneous upkeep triggers so the Faerie resolves before the sacrifice trigger. Ophiomancer requires *no Snake* when its upkeep trigger would fire.
- Opposition is an enchantment's activated ability, so Cursed Totem does not stop it; tapping our Orb **before** our untap permits parity, but casting Opposition under Contamination needs real off-land blue pips.
- Phyrexian Altar sacrifices one actual creature for one chosen mana, unaffected by Cursed Totem. The same Thrull cannot simultaneously pay Contamination, Skullclamp, Tower and Altar.
- Helm with Leyline or Dauthi exiles the target library; the opponent generally loses on the subsequent attempted draw, **not merely because Helm resolved**.
- Own Trinisphere and Chalice still obstruct free artifact casts and Breach loops. A zero-mana-value LED keeps MV 0 even if Trinisphere makes its cast cost three.
- The tests are finite authored mechanical assertions, **not** full multiplayer simulations or tournament win-rate estimates.

## Canonical merge requirements

1. Exact new artifact, raw hash and five-for-five structural difference must agree with the owner receipt.
2. The historical `f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c` file must stay immutable.
3. The approval-state/ordered tracker must name the same new SHA and approval date.
4. The immutable 62-deck historical snapshot and required M6 manifest must stay unchanged; current registry must preserve the other 61 deck hashes.
5. The fail-closed `verify_m7_certification_transfer.py --check` and its regression suite, plus deck-scoped exact-owner-lock CI, must pass at the precise PR head before merge and post-merge state must be re-read.

**Bracket:** 5 — fringe/rogue cEDH. **Tags:** Grixis Stax / Thrull Sacrifice / Helm–Breach Combo. **Project exceptions:** none. No M8 or aggregate milestone claim.
