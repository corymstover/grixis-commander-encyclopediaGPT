# Garza Zol, Plague Queen M7 Rev2 — reproducible canonical approval verification

This certificate is bound to Cory's exact explicitly approved SHA **353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244**. Its checks are implemented by tests/test_garza_zol_m7_rev2_approval.py and the exact-head GitHub Actions workflow; the file does not itself pre-assert CI success or a merged lock.

- Owner approved: 2026-10-24, exact 100-card SHA 353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244.
- Historical October 14 raw baseline preserved byte-for-byte SHA 32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f.
- Candidate path: refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt.
- Seven physical substitutions, complete 100 singleton and 38 land faces, all original 11 accelerants preserved, 20 Equipment, nine Game Changers.
- Bracket 4 — Optimized; tags Voltron / Commander Damage / Deathtouch-Control, no project exceptions.

## Evidence and limitations

- ChatGPT independent [PR #695](https://github.com/corymstover/GrokBotMTGCompanion/pull/695) exact head d816097a24a4d302f50222457e6c0b21f79579e5 and [exact-head Actions SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40070632545). Underlying Grok #668 was research-only and is preserved separately.
- Exact list independently re-fetched from engineering GitHub and hashed by system sha256sum before construction of this PR. All 19 previous canonical raw approvals had already been re-fetched/hash-checked and are rechecked in dedicated approval tests.
- 97 of candidate's names from GrokBot PR #668 Scryfall October 23 218-name archived oracle; exact archived IDs/text/legality retained. Three additional cards independently published on Scryfall/Gatherer, URLs in selected JSON, without fabricated API Oracle IDs; Commander-legal with UBR-compatible identity. No claim of a new October 24 full-list API collection response.
- Garza's damage/death +1/+1 triggers; Lizard two damage steps; Scythe reattachment; Two-Handed Axe attack-time power doubling (including post-combat Garza-sourced effects); Seize targeted extra combat + flashback; Malakir Rebirth death/command-zone state-based action choice; Temur Battle Rage Ferocious/trample; Kediss secondary noncombat damage and infect; mana/timing risks verified in bounded scenarios. Not a multiplayer rules engine, actual game simulation or win-rate model.
- Equipment and combat side effects, opponent spell-ability response windows, mandatory colored and generic mana and life costs are described in owner receipt, without implying free protection or infinite loops.
- Do not claim baseline turn-six castability proxy 0.4724 applies exactly to the new list: Mire enters tapped, unlike Takenuma.

## Exact-head and post-merge

Run the new focused unittest on PR head and rehash all prior nineteen approvals via the new workflow. Merge with expected HEAD SHA only after exact-head success; then verify the new approved deck's raw SHA on main, registry and tracker entry, historical baseline preservation, and regression of all 19 locks. Record canonical PR number and merge commit in handoff. Deck #21 follows after lock.
