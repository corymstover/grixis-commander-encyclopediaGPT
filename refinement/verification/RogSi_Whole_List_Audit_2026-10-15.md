# Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #47 of 62  
Status: working audit; not user approval

Authoritative baseline: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`, FINAL TXT member `RogSi.txt`.

Candidate: `refinement/decklists/RogSi_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c`

## Audit result

- Commanders: **2** — Rograkh, Son of Rohgahh / Silas Renn, Seeker Adept.
- Noncommander copies adjudicated: **98/98**.
- Result: **91 KEEP / 7 CUT**.
- Baseline: **100 cards / 100 distinct names / 25 lands**.
- Candidate target: **100 cards / 100 distinct names / 24 lands**.
- Singleton: **PASS target — no repeated names**.
- Project legality exception required: **NO**.
- Per-card adjudication ledger: `refinement/decisions/RogSi_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final seven-card delta

| Cut | Replacement | Decision basis |
|---|---|---|
| Timetwister | Final Fortune | Final Fortune is near-universal current RogSi core and its instant timing is uniquely valuable around end-step reloads. Timetwister is now minority flex and shuffles away graveyard resources needed by Breach and Mnemonic Betrayal. |
| Retraction Helix | Mnemonic Betrayal | Helix has a legitimate Valley Floodcaller combo line, but this list has no redundant eligible creature type and therefore asks Floodcaller to survive a turn. Mnemonic Betrayal is current RogSi core and a much broader recovery/storm engine. |
| Orcish Bowmasters | Vexing Bauble | Bowmasters is strong generic interaction but a low-inclusion RogSi flex slot. Bauble is a signature proactive protection piece that suppresses free interaction and can be cashed in before our own free-spell sequence. |
| Talisman of Indulgence | Talisman of Dominance | Preserve two-mana rock density while moving the fixing toward blue/black, which better supports the deck's stack interaction, Consultation/Pact lines, and black draw engines. |
| Training Center | Demonic Counsel | Reduce 25 to 24 lands in a turbo shell with unusually dense fast mana/rituals; add a two-mana tutor that becomes unrestricted once delirium is online. |
| Luxury Suite | Wooded Foothills | Replace a nonfetchable multiplayer dual with a fetch that reaches the typed red dual/shock suite, adds graveyard material, and improves shuffle/fetch sequencing. |
| Morphic Pool | Undercity Sewers | Replace a nonfetchable dual with an Island Swamp fetch target whose surveil directly supports Breach, threshold/delirium, and top-card quality. |

## Current tournament evidence used as a challenger, not an autopilot

Fresh RogSi six-month data on 2026-10-15 covers **1,767 parsed tournament lists**. The most decision-relevant missing cards are Final Fortune (98.4%), Mnemonic Betrayal (92.2%), Vexing Bauble (84.2%), and Demonic Counsel (60.3%). Timetwister is a 47.1% minority card with a negative descriptive PPG signal, while Orcish Bowmasters is 19.5% and Talisman of Indulgence 46.4%. These numbers informed the red team but did not substitute for card-role analysis.

## Material challengers rejected

- **Last Chance:** strong and common, but Warrior's Oath already occupies the exact same two-mana sorcery role. A name-only swap is not an improvement, and a third lose-the-game extra-turn spell did not beat the remaining interaction/value slots.
- **Snapback:** excellent current performance signal, but Deadly Rollick is retained because Rograkh makes its free mode nearly automatic and exile is materially stronger against permanent hatebears. Chain of Vapor and Into the Flood Maw already cover bounce.
- **Chromatic Star:** inherited ranking #1, but fresh tournament evidence shows a negative descriptive performance signal and the shell does not need another low-impact cantrip artifact merely to inflate artifact count.
- **Starting Town / Gemstone Mine:** viable lands, but after moving to 24 lands they do not materially beat the selected fetch/dual/fast-mana land configuration.
- **Fellwar Stone:** playable positive-signal flex card, but the candidate already has deep acceleration and preserving card quality/tutor density is more important than adding another two-mana rock.
- **Commandeer / Misdirection:** powerful free interaction but high card-cost; the retained counter suite plus Samut/Hexing/Bauble protection package is more efficient for this exact turbo plan.
- **Artifact/Monolith full conversion:** rejected as a wholesale identity change. Recent artifact-heavy RogSi lists are legitimate, but the 1,767-list field still overwhelmingly preserves Ad Nauseam/Breach turbo core. This encyclopedia deck remains the strongest realistic version of classic RogSi rather than chasing one branch's recent result.

## Rules-critical review queued for the complete gate

- Vexing Bauble self-interaction with Rograkh, zero-mana artifacts, Pact, Fierce/Swat, pitch spells, Hexing Squelcher, and its sacrifice ability.
- Samut split second on our instants/sorceries, including what split second does and does not stop.
- Final Fortune / Warrior's Oath delayed lose-the-game triggers.
- Demonic Counsel delirium and pre-delirium Demon-only restriction.
- Mnemonic Betrayal timing and exile/return behavior.
- Rograkh enabling Mox Amber, Drum, Mantle, sacrifice rituals/tutors, commander-presence free spells, and Flare of Duplication.
- Silas Renn artifact-recursion timing after combat damage.
- Breach + LED + Brain Freeze and Grinding Station variant lines.
- Tainted Pact singleton integrity.

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
