# Dr. Eggman M7 Rev2 — canonical candidate verification

**Owner decision:** `"Okay you can approve that deck"` after full 100-card list / five substitutions / exact SHA.
**Raw candidate:** `3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec`
**Raw historical Oct14 baseline:** `ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`
**Status:** Approved and authorized for canonical locking; exact-head canonical PR checks and post-merge main rehash required (not presumed here).
**Engineering primary:** [PR #690](https://github.com/corymstover/GrokBotMTGCompanion/pull/690), head `b48cf6302e5a6bc9bc6f8823b6c4202cd88d5494`, focused CI SUCCESS run `40059287946`.
**First-pass research:** GrokBot [PR #663](https://github.com/corymstover/GrokBotMTGCompanion/pull/663); its candidate is unapproved and not the final list.

## Count / singleton / color / legality
- Physical 100, distinct 97, first line `1x Dr. Eggman [Commander]`, 96 other distinct card names; Island ×2, Mountain ×2, Swamp ×2, all else singleton.
- Land count **32**. Eligible Construct/Robot/Vehicle cards **31** (excluding commander); conditional Mox Opal included in **seven** mana rocks.
- Three Game Changers: Ancient Tomb / Cyclonic Rift / Fierce Guardianship. Power Bracket 4 — Optimized.
- Archived live 2026-10-23 Scryfall: all 97 named cards legal in Commander; all color identities subset of UBR. No project exceptions. Gloomlake Verge from approved Don Andres exact source, with always-{U} and conditional-{B} only while controlling an Island or Swamp.

## Explicit change and owner's Oct14 keep policy
1. Blasphemous Act → Possession Engine: losing owner-kept Act knowingly accepted upon explicit approval.
2. Cybermen Squadron → Skysovereign, Consul Flagship.
3. Cryptothrall → Interceptor Mechan: loss of artifact-creature hexproof redundancy disclosed.
4. Weapons Manufacturing → Behemoth of Vault 0: loss of Munitions-sacrifice fodder engine disclosed.
5. Withering Torment → Gloomlake Verge: 31→32 land access; loss of direct enchantment removal disclosed.

**Retained:** Foundry Inspector and Unwinding Clock. Clock's repeatable artifact untaps of Master Transmuter, Kuldotha Forgemaster and Scrapyard Recombiner were an independent reason to reject GrokBot's proposed eight-mana Su-Chi Cave Guard replacement. No minimum-five cap or padded sixth swap.

## Actual mechanics and limitations
- Eggman's Oracle: at beginning of *our* end step, draw a card, then each opponent chooses discard or an eligible put from our hand. Opponent with an empty hand may choose discard for no effect. The Valeyard adds choices, not forced productive discards.
- **Put ≠ cast**; enters triggers for Interceptor, Possession and Behemoth work; a cast-only trigger like Cityscape Leveler's does not fire if put.
- Vehicles put through Eggman are not crewed; Dr Eggman's 3 power alone meets Crew 3 of both added Vehicles.
- Behemoth four energy counters on ETB and optional pay mana value of target nonland permanent when it dies; not blanket unconditional kill.
- Possession Engine grants control for as long as Vehicle remains controlled, stolen creature cannot attack or block; loses control once Vehicle is lost.
- Land access proxy 160k bounded sampled hands without play sequencing/mulligans/rational opponents, no claim of match outcomes. Archived DP's union-color approximation is not exact payable-color proof.
- **No independent third-model Pass C review, no comprehensive suite-green claim, no gameplay win rate.**

## Preservation and promotion checks
- Canonical historical file SHA remains `ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`, not overwritten.
- Current registry only `Dr__Eggman` changes; tracker only index14 row changes; all other 61 state records untouched, previous 14 locked M7 file hashes independently regression-checked.
- Exact-head CI must run canonical targeted test and previous fourteen M7 tests; comprehensive baseline suite can have known pre-existing failures and should not be mislabeled all-green.
- After merge, fetch **canonical main** approved file and independently compute SHA-256 equal to `3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec`; confirm registry/tracker and untouched source.
