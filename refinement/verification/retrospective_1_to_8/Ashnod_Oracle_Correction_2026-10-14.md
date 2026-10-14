# Ashnod the Uncaring — fresh Oracle correction

**Date:** 2026-10-14  
**Cycle:** global-restart-2026-10-13  
**Approved deck status:** remains APPROVED / LOCKED; no card-list change is made by this correction.

## Current canonical Oracle record

The fresh current-cycle Scryfall cache generated at `2026-10-14T05:25:45.050588+00:00` resolves Ashnod the Uncaring to:

> Deathtouch  
> Whenever you activate an ability of an artifact or creature that isn't a mana ability, if one or more permanents were sacrificed to activate it, you may copy that ability. You may choose new targets for the copy. (Sacrificing an artifact for mana to activate an ability doesn't count.)

Scryfall ID: `8f3d67c1-3142-44b4-8f83-0ca6177cf9ac`  
Oracle ID: `dcd5ab1b-adc5-486e-a1e0-636af6ee9470`

## Historical documentation error corrected

Earlier approval-era notes incorrectly described Ashnod's ability as triggering only once each turn and, in places, as requiring a nontoken permanent to be sacrificed. **Neither restriction appears in the current Oracle text.** Those statements are superseded for current rules analysis; the old files remain preserved as historical records.

Correct implications for the approved list:

- Every qualifying nonmana activated ability of an artifact or creature may be copied when one or more permanents are sacrificed as an activation cost. There is no once-per-turn ceiling in Ashnod's current Oracle text.
- The sacrificed permanent need not be nontoken.
- `Oni-Cult Anvil`, `Arcbound Ravager`, the sacrifice modes of `Trading Post`, `Repurposing Bay`, `Time Sieve`, and other qualifying nonmana activated abilities work with Ashnod when their activation costs sacrifice one or more permanents.
- `Ashnod's Altar` and `Krark-Clan Ironworks` are mana abilities; Ashnod expressly does not copy mana abilities.
- Sacrifices that occur only while an ability resolves, rather than as part of activating it, do not satisfy Ashnod's trigger condition. This preserves the earlier conclusion that `Goblin Welder` is not an Ashnod trigger merely because its exchange can cause an artifact to be sacrificed on resolution.
- Copying an activated ability does not repay its activation costs. One qualifying activation produces the original ability plus Ashnod's copy.

## Effect on approved deck

This correction **does not reveal a legality problem, broken combo, or required deck change**. It strengthens the approved sacrifice-activation engine relative to the stale interpretation. The exact approved 100-card list remains frozen.

Source records:
- `refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl`
- `refinement/verification/retrospective_1_to_8/Card_Verification_Ashnod_the_Uncaring_2026-10-14.csv`
- Current Comprehensive Rules entry point: https://magic.wizards.com/en/rules
- Latest current rules update bulletin checked: https://magic.wizards.com/en/news/announcements/reality-fracture-update-bulletin

**Correction result: PASS — stale rules wording repaired; approved list unchanged.**
