# Davros, Dalek Creator — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Cybermat. Cut: Counterspell.
- Final list: 100 copies, 95 distinct names, 34 land copies; repeated basic lands preserved. Commander first.
- Revised TXT SHA-256: `744ef073e8780162c8c1ccabf6f559ff076eeaa0402603bb6ac7441c74f390e5`.
- Baseline raw CSV SHA-256: `786fd20674049875df5c3eea0b00d78938fc27234f3ab56eaf1caa3ae708f447`.
- Baseline raw TXT SHA-256: `d97f76f87f56ebc7c7c54ee85167b2af55603d53bbf19bcc331885141ed08556`.
- Normalized baseline hash: `7afbb08cb95bd6ea5030134a9c9009036aee757098e30ff1a7b548d86243e85b`.

## Commander-first plan and change rationale

Davros creates a 3/3 black Dalek artifact creature with menace at end step if an opponent lost at least 3 life that turn, then gives opponents who crossed that threshold a villainous choice between you drawing a card and them discarding. The list remains a Dalek/artifact token strategy with life-loss enablers and discard payoffs. Cybermat is a two-mana artifact Robot with skulk; when it attacks unblocked it gets +X/+0 where X is the number of attacking artifact creatures. This supports reaching the 3-life threshold. Cyberman Patrol remains and grants afflict 3 to artifact creatures.

Counterspell is cut as a deliberate interaction-versus-synergy trade. Mana Drain, Swan Song, Fierce Guardianship, Deflecting Swat, and extensive removal remain. If the intended table is especially combo-heavy, retaining Counterspell may be preferable; this is not a universal upgrade claim.

Direct current Oracle and legality references: [Cybermat](https://mtg.wtf/card/who/175/Cybermat), [Counterspell](https://mtg.wtf/card/mh3/88/Counterspell), [Davros](https://mtg.wtf/card/who/192/Davros-Dalek-Creator). These cards are Commander-legal; color identity fits UBR. Official Commander banned list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 95 lines with quantities, commander first; total quantity 100.
- CSV: 95 rows, quantity sum 100, unique names 95.
- Current project-wide Scryfall metadata refresh generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; final names reconcile against that refresh. Cybermat, Counterspell and Davros directly checked.
- Candidate triage: 16 candidates; 1 accepted, 4 retained, 11 rejected with reasons.
- Consistency review covers 31 land copies, damage-threshold enablers, discard engines, artifact/Dalek density, interaction and removal. No numerical goldfish or matched-seed multiplayer test; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
