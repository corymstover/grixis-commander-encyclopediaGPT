# Ashnod the Uncaring — approval-gate dossier (2026-10-13)

**Cycle:** global-restart-2026-10-13. **State:** APPROVAL_REQUESTED; NOT APPROVED; NOT LOCKED. The five prior locked decks are untouched.

## Authoritative baseline
Frozen source: GrixisFINALTXT60--2026.zip / Ashnod_the_Uncaring.txt. Baseline raw SHA-256 d1b74569999818542ec3b787499c2a9e3d8a420c617af9b883cc875c324dd684. Baseline: 100 cards, 95 distinct names, 33 lands. The current proposal is staged separately at refinement/decklists/Ashnod_the_Uncaring_Approval_Proposal_2026-10-13.txt.

## Recommended changes
1. CUT Audacious Reshapers / ADD Oni-Cult Anvil: copied repeatable sacrifice-artifact drain, Construct fodder, lower curve; relinquishes higher-variance artifact cheat effect.
2. CUT Commander's Sphere / ADD Trading Post: copied draw and artifact recursion across turns; sacrifices three-mana acceleration for four-mana tapped engine. Sphere's own sacrifice-to-draw does qualify for Ashnod and is a real opportunity cost.
3. CUT Corridor Monitor / ADD Moonsilver Key: copied sacrifice-cost tutor for two mana-ability artifacts/basic lands, including combo/ramp pieces; relinquishes cheap ETB untap and potential recursion lines.

## Critical retention and red-team
- Repurposing Bay: Ashnod copies search on sacrifice-as-activation-cost; two artifacts each with MV exactly one greater than sacrificed artifact, subject to library availability.
- Bolas's Citadel: copy sacrifice-ten-nonland activated ability, two 10-life-loss events, and topdeck access. Keep.
- Time Sieve: copy activated extra-turn ability after sacrificing five artifacts as cost; two extra turns if both resolve.
- Clan Crafter: grants commander a copyable sacrifice-cost activated ability; keep.
- Dross Skullbomb and Esoteric Duplicator: absent from stale inherited Ashnod audit but independently checked against card-text/legality references.
- Goblin Welder: sacrifice occurs on resolution, not cost; does not trigger Ashnod. Goblin Engineer and Scrap Welder do.
- Ashnod's Altar and Krark-Clan Ironworks: mana abilities are not copied.
- Oni-Cult Anvil token trigger is once per turn; Ashnod's copying ability is not.

## Rules and legality methodology
Inherited v8.1.4 audit has exact name and Commander legal/color-identity pass for 90 of 95 final unique cards (the other five comprise two inherited cards absent from the stale audit and three additions); the two missing inherited names (Dross Skullbomb, Esoteric Duplicator) were separately checked on current card reference pages. All three additions (Oni-Cult Anvil, Trading Post, Moonsilver Key) were separately checked against current Oracle-style text, color identity, and Commander legality. Ashnod commander was checked separately. Official Commander banned list and October 12, 2026 WotC banned/restricted announcement consulted; no newly identified Commander prohibition. This is combined archived per-card evidence and current targeted verification, **not** a claim that every card received an individual live Scryfall API request. Source data had two stale name mismatches (Aether Spellbomb and Urza's Bauble in old audit only) and neither was silently substituted.

Sources:
- https://mtg.wtf/card/brc/4/Ashnod-the-Uncaring
- https://mtg.wtf/card/one/225/Dross-Skullbomb
- https://mtg.wtf/card/big/70/Esoteric-Duplicator
- https://mtg.wtf/card/neo/230/Oni-Cult-Anvil
- https://mtg.wtf/card/c14/279/Trading-Post
- https://mtg.wtf/card/mid/255/Moonsilver-Key
- https://mtg.wtf/card/dft/56/Repurposing-Bay
- https://mtgcommander.net/index.php/banned-list/
- https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026

## Whole-deck analysis
All 99 physical noncommander slots reviewed; all 100 ranked candidates screened. Three swaps selected. Baseline 33 lands unchanged, fast artifact acceleration retained; 5-mana commander makes opening-hand resource discipline important. Exact hypergeometric land-only consistency for 99 noncommander cards / 33 lands: 7-card hand P(0 lands) 5.23%, P(0 or 1 lands) 25.37%; 10 cards seen P(0 lands) 1.35%, P(0 or 1 lands) 9.19%. These are not win-rate or goldfish estimates and ignore ramp, mulligans and colored sources. Compared to baseline, removing Commander's Sphere lowers 3-mana rock density by one, while Moonsilver Key tutors ramp and Anvil lowers curve. No qualified multiplayer simulator or matched-seed win-rate experiment was conducted. Do not invent performance improvements.

## Strategic assessment
Identity: repeatable activation-cost artifact/creature sacrifice, ability-copying, recursion, copied tutor and finishers. Proposed natural ceiling: optimized/high-power Bracket 4, not claimed established cEDH. Red-team challenges: Trading Post is slow without untapping; Moonsilver Key costs 3 mana total and taps before tutoring; Oni-Cult Anvil is modest absent Ashnod; 33 lands are relatively lean; Citadel needs substantial board to fire activated finisher; Time Sieve consumes five artifacts and copy does not return costs. These are accepted tradeoffs, not unconditional advantages.

## Approval gate
Proposed list: 100 cards, commander first, singleton except basic lands, no project exceptions needed. Full 99-slot review and 100-candidate screen completed; no remaining candidate demonstrated a sufficiently clear improvement to displace selected package without significant cost or dilution. This is a *judgment-based* stopping rule, not proof of globally optimal deck or tested win-rate. Await user's **explicit approval** before modifying current_deck_overrides.json, tracker lock status, or moving to #7.
