# Abaddon the Despoiler — explicit M7 Rev3 owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)
Cycle: `global-restart-2026-10-13`
Decision: **APPROVED / LOCKED, EXACT REV3 SUPERSESSION**

## Exact authorization

Owner message in this conversation:

> I explicitly approve and authorize locking Abaddon the Despoiler Rev3, exact SHA-256 5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24, replacing the previous approved Rev2. Proceed with the GitHub canonical update and verification.

This approves exactly one 100-card decklist and **supersedes the current approved Rev2**; it is not approval of other proposed deck changes, M6.10 milestone acceptance, or M7/M8 aggregate milestones.

Canonical Rev3 source: `refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt`
Raw UTF-8 LF SHA-256: `5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24`
Source engineering approved candidate: `corymstover/GrokBotMTGCompanion:chatgpt-cycle76-m6-refinement:data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev3.txt`.
Prior Rev2 approved/locked raw SHA-256: `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`, retained unchanged at `refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt`.
Prior Oct13 approved artifact is also retained unchanged.

## Owner-approved six real replacements

| Added | Removed |
| --- | --- |
| Impact Tremors | Thermo-Alchemist |
| Sanctum of Stone Fangs | The Ruinous Powers |
| Coruscation Mage | Kessig Flamebreather |
| Sakashima of a Thousand Faces | Keeper of Secrets |
| Mount Doom | Mountain |
| Sheoldred, the Apocalypse | Ponder |

**Deck checks:** precisely 100 physical cards, 95 distinct card names; singleton except 3 Island, 2 Mountain, 3 Swamp; 34 lands; one Abaddon commander; Grixis U/B/R color identity; official Commander legality for all names per live-source-bound Oct 23 snapshots; no project legality exception. **Bracket 4 — Optimized**. Tags: **Cascade / Exile Cast / 40K Chaos**.

**Engineering verification:** [M7 full 100 Rev3 owner gate PR #645](https://github.com/corymstover/GrokBotMTGCompanion/pull/645) and [successful exact-head CI 39911935249](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39911935249), 93 successful steps. [Oracle-documentation correction #648](https://github.com/corymstover/GrokBotMTGCompanion/pull/648), exact-head CI 39913153403 success, corrected `Call Forth the Tempest`'s printed cost to `{5}{R}{R}{R}` (MV8) with no cardlist change. Stage20 source-bound candidate I/J tested-pool and reproducibility [engineering PR #644](https://github.com/corymstover/GrokBotMTGCompanion/pull/644).

Pass C is an **owner-waived, non-independent GPT-6 equivalent review**, not an independent third-model execution. The finite mechanic checks do not assert multiplayer matchup percentages or global mathematical optimality. M6.10 / aggregate M7 / M8 acceptance remains separate.

This exact approval has no authority to change **Admiral Beckett Brass** or the other 60 canonical approved deck records. Only an explicit later instruction may reopen this Rev3 lock.
