# Fire Lord Azula — Current-Cycle Refinement Decision Ledger

Cycle: `global-restart-2026-10-13`
Review date: 2026-10-14
Baseline source: `GrixisFINAL60--2026.zip` / `Fire_Lord_Azula.csv`
Baseline source CSV SHA-256: `2d83c6962c8aa6638b19bf248ddb88e2de977854e3737eb5b8f9c7497473ae7b`
Corroborating TXT export SHA-256: `5d7ab12b87d5aac8aa216d1d85eb78037ee2031a90ca96631e97fe10c5ee259c`
Standardized baseline SHA-256: `90ec69182cef0c80828a9bea5e3acf871d5c1017b30ea1fb6b49a8b045a633f9`
Approval-candidate SHA-256: `b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`
Baseline count: 100
Candidate count: 100
Candidate distinct names: 100
Candidate lands: 26
Commander identity: B/R/U
Project exception required: no
Natural ceiling: Power Bracket 5 — cEDH
Proposed tags: Combat-Flash / Spell Copy / Combo

## Commander blueprint

Fire Lord Azula is strongest when the deck can deploy her quickly, attack immediately or safely, and cast high-leverage spells while she is attacking. Her text rewards: (1) flash/timing permission that moves sorceries and permanent spells into combat, (2) haste access, (3) rituals, untap spells, cantrips, rummage/draw spells and tutors whose single paid cost becomes disproportionately valuable when copied, and (4) compact cEDH win packages that leave room for interaction.

Current tournament evidence supports a true cEDH ceiling. The review included current EDHTop16 results, current EDHREC Bracket 5/cEDH evidence, Wizards Oracle/release-note evidence, and the 2026-10-10 cEDH Galicia Top 4 Fire Lord Azula list. The comparator is evidence, not an automatic import.

The v8.1.4 project profile independently seeds Azula around `copy that spell` / `whenever you cast`. The project top-100 candidate pool surfaces commander-specific options including High Fae Trickster, Demand Answers and Redirect Lightning. The preserved October 12 list passed the old structural audits, but those audits do not substitute for this current-cycle strategic review.

## Mandatory whole-list audit — all 99 baseline slots accounted

### Retain — 64 noncommander slots

These cards survived the current cEDH efficiency, commander-fit, mana, interaction and combo review:

An Offer You Can't Refuse; Ancient Tomb; Arcane Signet; Arid Mesa; Badlands; Big Score; Birgi, God of Storytelling // Harnfel, Horn of Bounty; Blood Crypt; Bloodstained Mire; Borne Upon a Wind; Brain Freeze; Chrome Mox; City of Brass; Command Tower; Dark Ritual; Deflecting Swat; Demonic Tutor; Emergence Zone; Exotic Orchard; Fellwar Stone; Fierce Guardianship; Flooded Strand; Flusterstorm; Force of Negation; Force of Will; Frantic Search; Gamble; Gemstone Caverns; Imperial Seal; Jeska's Will; Lotus Petal; Mana Confluence; Mana Vault; Marsh Flats; Misty Rainforest; Mox Diamond; Mystic Remora; Mystical Tutor; Narset's Reversal; Orcish Bowmasters; Otawara, Soaring City; Pact of Negation; Polluted Delta; Ragavan, Nimble Pilferer; Rhystic Study; Rite of Flame; Scalding Tarn; Snap; Sol Ring; Steam Vents; Swan Song; Talisman of Creativity; Talisman of Dominance; Talisman of Indulgence; Thassa's Oracle; Underground Sea; Underworld Breach; Valley Floodcaller; Vampiric Tutor; Vivi Ornitier; Volcanic Island; Watery Grave; Wheel of Fortune; Wooded Foothills.

The retained shell preserves Azula-specific infrastructure rather than merely generic Grixis staples: Borne Upon a Wind, Valley Floodcaller and Emergence Zone create combat timing; Big Score, Frantic Search, Snap and the rituals scale directly with her copy trigger; Narset's Reversal + Frantic Search forms a commander-dependent loop; Underworld Breach + Frantic Search forms another commander-dependent recursive engine.

### Cut — 35 baseline slots

- Archmage Emeritus — four-mana setup engine is too slow for the established ceiling.
- Ashling, Flame Dancer — expensive, board-dependent payoff.
- Brainstorm — excellent generic card, but the rebuilt shell prioritizes Azula-multiplied cantrips/timing pieces and live interaction.
- Comet Storm — mana-intensive finisher redundant beside compact combo wins.
- Deadly Rollick — strong but commander-dependent and narrower than the current bounce/stack suite.
- Desperate Ritual — lower leverage than Cabal Ritual and the optimized fast-mana package.
- Dualcaster Mage — removed with Twinflame; the package is less slot-efficient than the chosen wins.
- Electro, Assaulting Battery — too slow and board dependent.
- Electrodominance — mana intensive and lower floor than the current timing/tutor package.
- Fire Nation Palace — theme land loses to the cEDH unique-name mana base.
- Firebender Ascension — slow setup.
- Firebending Student — insufficient immediate impact.
- Fists of Flame — thematic combat payoff is not a reliable cEDH win route.
- Gitaxian Probe — free information is useful, but the slot is more valuable as live interaction or an Azula-multiplied cantrip.
- Island x2 — removed during Tainted Pact unique-name conversion.
- Lightning Greaves — haste is replaced by Arena of Glory, Crimson Wisps and Expedite, which also advance mana/cards.
- Luxury Suite — replaced during tournament-grade unique-name mana modernization.
- Morphic Pool — replaced during tournament-grade unique-name mana modernization.
- Mountain x2 — removed during Tainted Pact unique-name conversion.
- Nightscape Familiar — lower impact than the new reduction/acceleration suite.
- Seething Song — three-mana ritual is comparatively inefficient and raises Ad Nauseam cost.
- Snapcaster Mage — strong value, but slower than the dedicated tutor/combo/interaction slots.
- Spellseeker — powerful but three-mana tutor body loses on speed to Beseech/Wishclaw/one-mana tutors.
- Storm-Kiln Artist — excellent Azula synergy, but four-mana setup is too slow; Big Score produces immediate resources at the same MV.
- Stormcatch Mentor — compressed creature slots favor Geist of Saint Thalia and higher-impact protection/value bodies.
- Swamp x2 — removed during Tainted Pact unique-name conversion.
- The Last Agni Kai — strong theme, lower floor than universal interaction/card velocity and requires favorable creature combat.
- Training Center — replaced during unique-name mana modernization.
- Twinflame — removed with Dualcaster Mage.
- Twinning Staff — three-mana win-more copy enhancer; Azula already supplies the engine from the command zone.
- Veyran, Voice of Duality — synergistic but a three-mana setup card without enough immediate cEDH impact.
- Zuko, Firebending Master — flavor-forward but insufficient immediate mana/protection/cards/combo leverage.

## Additions — 35 slots

- Ad Nauseam — premier instant-speed cEDH draw engine.
- Arena of Glory — can give Azula haste when its exert mana pays for her creature spell.
- Beseech the Mirror — efficient tutor; if bargained, Azula's copy is also treated as bargained.
- Cabal Ritual — efficient ritual that scales dramatically when copied.
- Cavern of Souls — helps force Human commander Azula through countermagic.
- Chain of Vapor — one-mana flexible bounce.
- Crimson Wisps — haste plus cantrip; Azula can copy it for a second draw.
- Demand Answers — one additional cost paid, then copy + original each draw two.
- Demonic Consultation — compact Thassa's Oracle win piece.
- Expedite — haste plus cantrip; Azula can copy it for a second draw.
- Faerie Mastermind — low-MV flash draw engine.
- Geist of Saint Thalia — reduces noncreature spell costs and improves the spell-dense combat turn.
- Grim Monolith — high-efficiency acceleration.
- Grinding Station — Breach/graveyard-engine redundancy.
- Hexing Squelcher — uncounterable protection piece that makes the deck's spells uncounterable.
- High Fae Trickster — persistent flash permission, directly enabling Azula to copy sorceries/permanent spells in combat.
- Into the Flood Maw — efficient broad interaction.
- Lion's Eye Diamond — core Breach/Brain Freeze engine and fast mana.
- Mental Misstep — zero-mana cEDH interaction.
- Mindbreak Trap — free interaction against overloaded/uncounterable stacks.
- Mox Opal — zero-mana acceleration; candidate has 15 artifacts including Opal.
- Necropotence — elite cEDH card advantage.
- Pyroblast — one-mana protection/blue interaction.
- Quicken — one-mana draw spell plus sorcery timing permission; Azula copies it for a second draw.
- Red Elemental Blast — one-mana protection/blue interaction.
- Redirect Lightning — efficient redirect spell whose paid additional-cost status carries to the copy.
- Repeal — flexible instant interaction that replaces itself.
- Samut, Tyrant of Naktamun — gives instants/sorceries split second; Azula's triggered copy ability still functions through split second.
- Simian Spirit Guide — zero-mana-from-hand acceleration.
- Starting Town — early untapped unique-name rainbow source.
- Strix Serenade — one-mana broad counterspell.
- Tainted Pact — second compact Oracle enabler; candidate has 100 distinct names.
- Verdant Catacombs — additional unique fetchland/fixing.
- Wan Shi Tong, Librarian — flash value engine that punishes opposing searches.
- Wishclaw Talisman — two-mana tutor artifact with very high combo access efficiency.

## Commander-specific combo/rules architecture

1. Fire Lord Azula + Narset's Reversal + Frantic Search is a verified Commander Spellbook loop with an attacking, nonsummoning-sick Azula and sufficient blue-producing lands. Azula's automatic copy of Narset's Reversal returns the original spells to hand while Frantic Search copies untap lands, yielding repeatable looting/draw triggers, storm and mana.
2. Fire Lord Azula + Underworld Breach + Frantic Search is independently recorded by Commander Spellbook as a recursive Azula engine, subject to the graveyard and mana prerequisites.
3. Underworld Breach + Lion's Eye Diamond + Brain Freeze remains the compact noncommander Breach engine.
4. Thassa's Oracle + Demonic Consultation / Tainted Pact are compact primary wins. The candidate's 100 distinct names satisfy the Tainted Pact duplicate-name constraint.
5. Big Score and Demand Answers pay their additional cost only for the original spell. Wizards' Azula ruling states that effects based on additional costs paid for the original are copied as though those same costs were paid for the copy. Big Score therefore resolves for four cards and four Treasures total if both copy and original resolve; Demand Answers draws four total.
6. Bargain is an additional cost; a copied bargained Beseech the Mirror is also bargained.
7. Samut's split second does not stop triggered abilities from triggering. Azula still triggers on an instant/sorcery cast while attacking and creates her copy.
8. Azula copies permanent spells as well. A copied nonlegendary permanent spell resolves as a token; a legendary permanent copy is subject to the legend rule after resolution.

## Red-team deviations from the 2026-10-10 Top 4 comparator

The current Galicia Top 4 shell was not imported verbatim. Two slots changed after the second serious pass:

- Final Fortune -> Big Score. Azula automatically copying Final Fortune creates hazardous multiple delayed loss triggers rather than a clean two-turn multiplier. Big Score is a direct positive multiplier of Azula's text.
- Undercity Sewers -> Mox Opal. The candidate returns to 26 lands and adds zero-mana acceleration while retaining 15 artifacts for metalcraft support.

Serious rejected challengers after the second pass included Leyline of Anticipation, Storm-Kiln Artist, The Last Agni Kai, Dualcaster Mage/Twinflame, Lightning Greaves, the flavor-forward Fire Nation package, Archmage Emeritus, Veyran, Twinning Staff, Electro, Brainstorm, Gitaxian Probe and Deadly Rollick. Each loses on speed, slot efficiency, redundancy or commander-specific output against the frozen candidate.

## Closure

After comparing the full 99-slot baseline, v8.1.4 top-100 candidates, current EDHREC cEDH evidence, current EDHTop16 results, the 2026-10-10 Top 4 shell, newly released Reality Fracture cards and the serious challengers above, the second serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS** beyond Big Score over Final Fortune and Mox Opal over Undercity Sewers.

This candidate is frozen only for complete rules/Oracle/legality/structural verification. It remains **UNAPPROVED / UNLOCKED** until the fail-closed complete gate passes and the user explicitly approves this exact SHA-bound list.
