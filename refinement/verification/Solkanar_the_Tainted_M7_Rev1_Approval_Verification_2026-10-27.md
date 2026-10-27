# Deck #53 — Sol'Kanar the Tainted M7 Rev1 — exact approved-list verification

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

## Byte-bound source and selected inventory

- Canonical new list: `refinement/decklists/Solkanar_the_Tainted_M7_Rev1_Approved_2026-10-27.txt`, raw UTF-8 SHA-256 **`c244b7c3e31b108a0730db37790de14dd167c9ee274259b3f18bbb5971a1ef20`**.
- Before: `refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt`, raw SHA-256 `72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58` (preserved, not overwritten).
- **100 physical / 93 distinct** including single commander. Island x3, Mountain x3, Swamp x4 are only repeats. No MDFC, companion or project legality exception. **35 lands** and all nine ramp artifacts unchanged. Grixis color identity **U/B/R**.
- Six one-for-one replacements: Suit→Kitten, Chimera→Familiar, Reins→Brand, Visions→Alexios, Heist→Sleeper Agent, Propaganda→Wishclaw. No other card difference.

## Legality, interaction and decision evidence

- [Engineering PR #734](https://github.com/corymstover/GrokBotMTGCompanion/pull/734) exact tested head `a0ad5e80a8e8f11ac7418d5a4d306d7a661ec1f9`, merged `61f32f0a127ddb0965853e3e946c44c8b4dc6db8`. All 99 old noncommander physical slots judged, six selected cuts and 15 named alternatives evaluated, eight-swap whole-100 variant rejected after emergency-role tradeoff.
- [Focused Actions #40566082752](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40566082752) **SUCCESS**, including full live current Scryfall 93-name Oracle ID / legality / identity audit and 17 bounded finite rules fixtures.
- [M7 structural contract Actions #40566082743](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40566082743) **SUCCESS** on the same exact head, including physical alternatives and open-ended no-five-anchoring gate.
- Commander four modes are chosen as part of placing the controller's own end-step trigger on the stack; a new object resets mode history, and control change alone doesn't. Thassa, Closet, Kitten and Planar Incision are distinct timing/target restrictions; Brand returns ALL owned permanents and can reclaim lethal gifts; Nightscape applies **one** generic-cost reduction to Sol; Alexios cannot attack owner; Wishclaw changes controller only on tutor activation resolution.
- Direct Pact gift after modes, Coil grave-exile recipient death, Audience recipient modes, owned creature retrieval and relevant opponent responses checked in scoped finite fixtures, not a complete game-engine simulation. Mana curve, UBR pips, 35 lands and remaining 24 other blue nonland Force of Will pitches reviewed.
- Natural power ceiling **Bracket 4 — Optimized**, tags **Donate / Blink / Giftable Curses**.

## Authority and scope

Cory replied **"Approve"** to the exact six-swap Deck #53 M7 Rev1 100-card list and SHA. No second confirmation needed. Historical Oct15 approved file and all other 61 commander locks stay untouched. The older M6 J input receipt is not a sealed executed M6.10 completion; this deck-specific closeout does not imply aggregate M6.10, M7 or M8 milestone acceptance.

## Required postmerge readback

Re-fetch the new deck bytes and `state/current_deck_overrides.json#decks.Sol_kanar_the_Tainted` from canonical `main`, confirm exact SHA and APPROVED/LOCKED. Check tracker row #53 and preserved Oct15 predecessor separately.
