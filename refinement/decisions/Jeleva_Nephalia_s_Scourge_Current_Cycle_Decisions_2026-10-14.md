# Jeleva, Nephalia's Scourge — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Authoritative source: `GrixisFINAL60--2026.zip / Jeleva__Nephalia_s_Scourge.csv`  
Source CSV SHA-256: `d5c4b5dfb27a5721136e23912cfe79fc097707f2177a0dc78d7a2c1b49f50ce0`  
Source TXT SHA-256: `e70f66fc89946f6777586b0bd6538cb79d09501ec395b0ab26abc2af46bece87`  
Baseline artifact: `refinement/decklists/Jeleva_Nephalia_s_Scourge_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline artifact SHA-256: `82a12467aa33a115e33f90e340148d611cb55398316c49de051cb54ff5017883`  
Approval candidate: `refinement/decklists/Jeleva_Nephalia_s_Scourge_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f`

## Source reconciliation

The FINAL60 CSV and FINALTXT exports agree on card membership and remain the authoritative current-cycle baseline. The baseline is structurally valid at 100 cards, 99 distinct names, and 36 lands; only Island repeats. Older v8.1.4 candidate/audit material is supporting research and does not overwrite the latest FINAL export.

## Commander blueprint and natural ceiling

**Primary plan:** make Jeleva herself the card-advantage and spell-cheating engine. The optimized sequence is top-library setup/tutoring -> cast Jeleva -> exile a deliberately staged instant/sorcery -> grant haste -> attack and cast the exiled spell for free. Recasts naturally increase Jeleva's X through commander tax, and Harmonic Prodigy doubles both Jeleva's ETB and attack triggers.

**Natural ceiling:** **Power Bracket 5 — fringe cEDH.** Current EDHREC Bracket-5/cEDH data contains an active Jeleva population and a contemporary turbo/Oracle/Breach shell. EDHTop16 also records multiple 2026 Jeleva entries in 50+ player cEDH events, including an 18th-place finish in a 103-player event, but current large-event conversion is 0%. The deck is therefore treated as a legitimate lower-tier/fringe cEDH commander rather than a top-tier tournament commander. The list must earn Bracket 5 through Jeleva-centric lines instead of merely becoming generic Grixis turbo.

### Commander-specific spine

- `Mystical Tutor`, `Vampiric Tutor`, `Imperial Seal`, and `Personal Tutor` deliberately stage high-impact spells on top before Jeleva is cast.
- `Scheming Symmetry` is unusually strong here: after both selected players tutor to the top, a Jeleva cast can exile both staged cards before either player draws them, subject to normal interaction/top-library changes.
- `Long-Term Plans` puts any card third from the top. A normal four-mana Jeleva cast exiles at least the top four cards, so the tutored card is captured if library order is unchanged before Jeleva's ETB resolves.
- `Brainstorm`, `Scroll Rack`, and `Sensei's Divining Top` convert otherwise awkward high-mana spells in hand/top-library texture into Jeleva fuel.
- `Lightning Greaves`, `Torch Courier`, and `Arena of Glory` let Jeleva attack immediately, minimizing the time opponents have to remove her before the free-cast trigger.
- `Harmonic Prodigy` is a two-mana Wizard payoff that causes Jeleva's Wizard triggered abilities to trigger an additional time, doubling both exile setup and attack-cast opportunities.
- `Mind's Desire`, `Peer into the Abyss`, `Mnemonic Betrayal`, `Doomsday`, and `Yawgmoth's Will` are high-leverage Jeleva targets; `Final Fortune` is an efficient extra-turn target that can produce another Jeleva attack while remaining castable from hand.

### Secondary competitive routes

- `Thassa's Oracle` + `Demonic Consultation` or `Tainted Pact`.
- `Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze` with sufficient graveyard resources.
- `Doomsday` remains a historically and currently supported Jeleva cEDH route; approval does not depend on an undocumented fixed five-card pile.

## Material baseline defects corrected

The baseline is optimized as a large-spell/exile-value Commander deck, but it is too slow for Jeleva's demonstrated competitive ceiling. It contains many seven- to ten-mana haymakers, duplicated value engines, slow three-mana rocks, tapped/check lands, and payoff permanents that do not improve the probability that Jeleva resolves and attacks before opponents win.

The candidate removes that high-variance battlecruiser shell and replaces it with fast mana, cheap interaction, efficient tutors, a singleton Tainted Pact mana base, and explicit top-deck/haste infrastructure. Importantly, `Harmonic Prodigy`, `Brainstorm`, `Lightning Greaves`, the black top-deck tutors, and Jeleva herself are retained from the baseline so the rebuild grows from the commander's existing identity rather than replacing it.

## Mandatory 99-slot whole-list audit

Every noncommander baseline card slot was reviewed. Accounting is exact: **37 retained noncommander card slots + 61 named cuts + the second copy of Island removed = all 99 baseline noncommander slots.** The candidate adds 62 new singleton names and returns to exactly 100 cards / 100 distinct names including Jeleva.

### Retained 37 noncommander cards

`An Offer You Can't Refuse`; `Ancient Tomb`; `Arcane Signet`; `Badlands`; `Blood Crypt`; `Bloodstained Mire`; `Brainstorm`; `City of Brass`; `Command Tower`; `Dark Ritual`; `Deflecting Swat`; `Demonic Tutor`; `Exotic Orchard`; `Fellwar Stone`; `Fierce Guardianship`; `Harmonic Prodigy`; `Island`; `Jeska's Will`; `Lightning Greaves`; `Mana Confluence`; `Morphic Pool`; `Mystical Tutor`; `Otawara, Soaring City`; `Polluted Delta`; `Ponder`; `Scalding Tarn`; `Sol Ring`; `Steam Vents`; `Swamp`; `Swan Song`; `Talisman of Creativity`; `Talisman of Dominance`; `Toxic Deluge`; `Underground Sea`; `Vampiric Tutor`; `Volcanic Island`; `Watery Grave`.

### Cut 61 named baseline cards plus one excess Island

`Aminatou's Augury`; `Apex of Power`; `Arcane Denial`; `Blasphemous Act`; `Blatant Thievery`; `Blood for the Blood God!`; `Bojuka Bog`; `Breach the Multiverse`; `Bribery`; `Call Forth the Tempest`; `Capture of Jingzhou`; `Chaos Warp`; `Cormela, Glamour Thief`; `Cover of Darkness`; `Cruel Ultimatum`; `Crumbling Necropolis`; `Cyclonic Rift`; `Deadly Rollick`; `Dimir Signet`; `Double Vision`; `Dragonskull Summit`; `Dream Harvest`; `Drowned Catacomb`; `Etali, Primal Storm`; `Expropriate`; `Fabled Passage`; `Feed the Swarm`; `Fevered Suspicion`; `Frantic Search`; `Haunted Ridge`; `Improvisation Capstone`; `Izzet Signet`; `Keeper of Secrets`; `Luxury Suite`; `Mana Drain`; `Memory Plunder`; `Mizzix's Mastery`; `Mnemonic Deluge`; `Mountain`; `Nalfeshnee`; `Nexus of Fate`; `Nightscape Familiar`; `Passionate Archaeologist`; `Path of Ancestry`; `Rakdos Signet`; `Riptide Laboratory`; `Rise of the Dark Realms`; `Roaming Throne`; `Shipwreck Marsh`; `Shivan Reef`; `Sulfur Falls`; `Sulfurous Springs`; `Swiftfoot Boots`; `Talisman of Indulgence`; `Tasha, the Witch Queen`; `Time Stretch`; `Training Center`; `Urborg, Tomb of Yawgmoth`; `Volcanic Vision`; `Wild-Magic Sorcerer`; `Xander's Lounge`; plus the second baseline copy of `Island`.

### Added 62 cards

`Ad Nauseam`; `Arena of Glory`; `Arid Mesa`; `Borne Upon a Wind`; `Brain Freeze`; `Cabal Ritual`; `Chain of Vapor`; `Chrome Mox`; `City of Traitors`; `Demonic Consultation`; `Doomsday`; `Final Fortune`; `Flooded Strand`; `Flusterstorm`; `Force of Negation`; `Force of Will`; `Gamble`; `Gemstone Caverns`; `Gitaxian Probe`; `Grim Monolith`; `Hexing Squelcher`; `Imperial Seal`; `Into the Flood Maw`; `Lim-Dûl's Vault`; `Lion's Eye Diamond`; `Long-Term Plans`; `Lotus Petal`; `Mana Vault`; `Marsh Flats`; `Mental Misstep`; `Mind's Desire`; `Mindbreak Trap`; `Misty Rainforest`; `Mnemonic Betrayal`; `Mox Diamond`; `Mox Opal`; `Mystic Remora`; `Necropotence`; `Opposition Agent`; `Pact of Negation`; `Peer into the Abyss`; `Personal Tutor`; `Preordain`; `Pyroblast`; `Ragavan, Nimble Pilferer`; `Red Elemental Blast`; `Rhystic Study`; `Rite of Flame`; `Scheming Symmetry`; `Scroll Rack`; `Sensei's Divining Top`; `Simian Spirit Guide`; `Tainted Pact`; `Thassa's Oracle`; `Torch Courier`; `Underworld Breach`; `Verdant Catacombs`; `Wheel of Fortune`; `Windfall`; `Wishclaw Talisman`; `Wooded Foothills`; `Yawgmoth's Will`.

## Adversarial second pass

- **Opposition Agent — RETAINED.** Generic, but its current cEDH disruption rate is high enough to justify the slot in a fringe competitive deck, and it interacts favorably with opposing tutors and the same tutoring axis Jeleva exploits.
- **Hexing Squelcher — RETAINED.** It protects Jeleva, top-deck setup, and proactive win attempts without requiring the commander to be on the battlefield first.
- **Scroll Rack — RETAINED.** It is slower than a pure turbo card, but uniquely converts expensive spells stranded in hand into known Jeleva exile targets and therefore survives the identity-first test.
- **Long-Term Plans — RETAINED over Mana Drain.** The third-from-top placement is effectively a Jeleva tutor when she is cast normally, making it materially more commander-specific than another two-mana counterspell.
- **Burnt Offering / Rain of Filth — REJECTED.** Both increase one-turn mana, but Burnt Offering is only attractive after Jeleva has already been deployed and sacrifices the engine, while Rain of Filth overcommits the 27-land base. Existing rituals/fast mana are sufficient.
- **Nexus of Fate / Time Stretch / Capture of Jingzhou — REJECTED.** Extra turns synergize with Jeleva attacks, but `Final Fortune` performs the role at two mana and avoids excessive Ad Nauseam burden.
- **The One Ring — REJECTED.** Excellent generic cEDH value, but four mana and no direct Jeleva setup is weaker here than the commander's dedicated top-deck package.
- **Beseech the Mirror / Praetor's Grasp — REJECTED.** Both are strong competitive tutors/value tools, but the chosen suite already reaches the compact win packages while preserving more Jeleva-specific top-deck effects.
- **Notion Thief / Dauthi Voidwalker / Orcish Bowmasters — REJECTED.** Powerful generic interaction, but they do less to advance Jeleva than the retained commander infrastructure.
- **Valley Floodcaller — REJECTED.** Flash for noncreatures is strong but its untap trigger does not grant Jeleva haste and only pumps/untaps Birds, Frogs, Otters, and Rats, so it is less commander-specific than it initially appears.
- **Roaming Throne / Strionic Resonator — REJECTED.** They can copy Jeleva triggers but are significantly slower than Harmonic Prodigy at the fringe-cEDH ceiling.
- **Cyclonic Rift / Mana Drain — REJECTED as additional interaction.** Credible staples, but `Chain of Vapor`, `Into the Flood Maw`, the free/one-mana counter suite, and commander-specific tutors are higher-priority slots.

## Closure

The final candidate is **100 cards, 100 distinct names, and 27 lands**. It preserves Jeleva as the reason to choose this commander by building around deliberate exile setup, trigger multiplication, and immediate attacks, while Oracle and Breach remain secondary resilience packages required at the intended ceiling.

After the whole-list audit, contemporary cEDH comparison, commander-specific tutor/haste challenge, fast-mana challenge, and generic-staple challenge, the final serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

Candidate remains **NOT APPROVED** until the exact SHA-bound list passes fresh Oracle/color-identity, current official Commander legality, and rules verification and the user explicitly approves it.