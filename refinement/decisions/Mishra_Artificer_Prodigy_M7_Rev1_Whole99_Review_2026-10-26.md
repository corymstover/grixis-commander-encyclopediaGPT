# Deck #36 Mishra, Artificer Prodigy — M7 Rev1 whole-99 and alternative-package disposition

Date 2026-10-26; exact new raw SHA-256 `45c0d559f0aa859b84e2fb52baf31fdbb683de3e7bc7f211821b50420dee9761`; old October 15 baseline preserved `9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d`.

Commander-first plan: turn symmetric artifact-spell counters into asymmetric prison through Mishra's cast trigger recovering the same card from graveyard or library, while low-curve artifact recursion and conditional finishing packages provide paths through resistant opponents. Six selected trades:

1. **+Lotus Petal / −Nullstone Gargoyle**
2. **+Deflecting Swat / −Praetor's Grasp**
3. **+Imperial Seal / −Fabricate**
4. **+Otawara, Soaring City / −Academy Ruins**
5. **+Flusterstorm / −Mana Drain**
6. **+Grinding Station / −Thought Monitor**

The complete decision packet in engineering repository `data/grixis/m7/decision_reviews/Mishra__Artificer_Prodigy_rev1.json` records 16 material judgments, challenged retained incumbents Wishclaw Talisman and Planar Chaos, 99-card role coverage, full 100 alternatives with 7 changes (+Reshape/−Wishclaw or +Defense Grid/−Planar Chaos), plus an alternate prison-first Uthros cut and alternate value-first Sculpting Steel cut. Neither higher-swap package dominates the primary on actual role costs. No five/six swap cap used.

Rationale: Lotus Petal and Otawara improve exact UBR commander deployment while losing Gargoyle's nine-mana prison and Academy Ruins recursion; Flusterstorm and Deflecting Swat defend deployed combo/commander plans but their nonartifact/free forms conflict with some pilot lock pieces; Imperial Seal trades artifact-tutor specificity for cheaper universal tutoring; Grinding Station provides a sacrifice-based artifact throughput/payoff line while losing Thought Monitor's affinity card draw. Remaining self-counter cards intentionally kept.

Live 100/100 Scryfall current Oracle/legality and one-for-one exact source verified on 2026-10-26; tests `tests/test_m7_mishra_artificer_rev1.py` pass all 12 bounded methods, exact GitHub certification https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40308662195 and shared M7 contract https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40308662192 both success at `cc12a8179ba560a4f2409c22790b648ad45f9f57`.

**Not proven:** complete opponent artifact-hate F2 game-state matchup, global I/J seal for changed SHA, unbounded deterministic multiplayer win percentages. The P1 F2 coverage limitation is explicit, not presented as a passed fixture. Owner approved the complete SHA-bound candidate in one message.
