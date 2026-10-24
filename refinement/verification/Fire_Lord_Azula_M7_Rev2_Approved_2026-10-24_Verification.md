# Fire Lord Azula M7 Rev2 — source-bound verification and release gate

This is the reproducible certificate for Cory's explicitly approved **`77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`** exact 100-card file (2026-10-24). The accompanying Python unittest and GitHub Actions workflow implement the assertions; **this text does not imply results before CI executes**.

## Scope

- Candidate file: `refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt`, 100 `1x` lines, commander first, 100 distinct names.
- Baseline: `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt`, immutable raw SHA `b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`.
- Five add/cut pairs in `refinement/approvals/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.md`, no sixth padding.
- Saved Oct23 Scryfall source `refinement/verification/Fire_Lord_Azula_M7_Rev2_Scryfall_Selected_2026-10-23.json`: 100 exact names, 100 Oracle IDs, each official Commander legal, UBR identity, zero project exceptions, 26 land faces (one MDFC), exactly 20 archived Game Changers.
- Commander-specific rules: Azula copies cast spells in attack; copy not cast; Electro's new free casts trigger Azula only if still attacking, and only if target legal at resolution; Turnabout + Narset Reversal loop conditional; Samut split-second self-blocking issue; flashback mana/zone costs; big score vs Windfall pay same two additional mana after RR; Sink MDFC 3 life/Ad Nauseam cost.

## Source-bound research

- Engineering [PR #694](https://github.com/corymstover/GrokBotMTGCompanion/pull/694) and [exact-head Actions SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40067171128), derived from archived Grok first pass #667 and independent adversarial comparison of five exact 100-card alternatives.
- Official mechanics/rulings: https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes and https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes
- No GrokBot paid credits or current Colab/research pipeline rerun.

## Reproducible release checks

`python -m unittest discover -s tests -p 'test_fire_lord_azula_rev2_m7_approval.py' -v`

`python -m unittest discover -s tests -p 'test_evelyn_rev2_m7_approval.py' -v`

Focused owner-SHA verification and all earlier 18 independently SHA-bound M7 locks run in the new `.github/workflows/verify-fire-lord-azula-m7-rev2-approval.yml` workflow. Do not claim unrelated pre-existing pytest suite failures/errors are fixed.

## Result boundary

Canonical PR checks must pass on exact head. On merge, independently compare committed main raw file bytes to `77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`, confirm `state/current_deck_overrides.json`, tracker, prior 18 raw locks, and record PR/merge SHA.
