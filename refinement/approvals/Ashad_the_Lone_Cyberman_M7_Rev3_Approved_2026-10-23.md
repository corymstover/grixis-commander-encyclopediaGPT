# Ashad, the Lone Cyberman — explicit M7 Rev3 owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED** — exact Deck #5 ChatGPT independent M7 Rev3 ten-swap candidate, raw SHA-256 `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267`.

## Exact owner authorization in context

Cory replied:

> Approved

This was immediately in response to ChatGPT's explicit question:

> Cory, do you explicitly approve **Ashad, the Lone Cyberman M7 Rev3**, exact SHA-256 `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267`?

That same assistant response displayed the **complete proposed 100 physical cards**, ten one-for-one additions/cuts, precise raw SHA and verified GitHub source, plus expressly promised to seek approval before canonically locking. Thus the reply approves **only these exact bytes**, not a different list, a generic "proceed" authorization, the original Grok five-swap proposal, or aggregate M6.10/M7/M8 acceptance.

- Canonical approved source: `refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt`.
- Immutable prior October 13 approval source: `refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt`, raw SHA `087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25`. **Do not rewrite or delete it**; previous approval preserved.
- Engineering final proposed source: `corymstover/GrokBotMTGCompanion:data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_M7_Rev3_Ten_Approval_Candidate.txt`, exact PR [#653](https://github.com/corymstover/GrokBotMTGCompanion/pull/653) head `ef7a1f726f26648886cf9b44069f2c8e205df189`, raw SHA `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267`.
- Engineering independent decision review: `data/grixis/m7/decision_reviews/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_mana_and_identity_review.md` (includes Rev3 selection).
- New independently scoped Rev3 M6 I and strict J: `data/grixis/m6/ij/certificates/ashad-the-lone-cyberman-m7-rev3.json` and `data/grixis/m6/ij/revision_bundles/ashad-the-lone-cyberman-m7-rev3.json`; original five-swap I/J bytes preserved.
- Selected 95-name primary Oracle evidence copied into canonical verification: `refinement/verification/Ashad_the_Lone_Cyberman_M7_Rev3_Scryfall_Selected_2026-10-23.json`. The 118-name exploratory pool also contains two rejected ineligible names **not selected in the deck**.

## Exact ten net commander-first changes

| Add | Cut |
| --- | --- |
| Skullclamp | Fellwar Stone |
| Piggy Bank | Reckless Fireweaver |
| Razorlash Transmogrant | Thoughtcast |
| Necron Deathmark | Noxious Gearhulk |
| Royal Warden | Thopter Spy Network |
| Mishra's Workshop | Tezzeret, Master of the Bridge |
| Ancient Tomb | Delete |
| City of Brass | Crumbling Necropolis |
| Mana Confluence | Shipwreck Marsh |
| Liberator, Urza's Battlethopter | Kappa Cannoneer |

Marionette Master (artifact-sacrifice drain), Unwinding Clock (opponent-turn artifact untap), and Ichor Wellspring (copyable value and sacrifice draw) are preserved. New Liberator is a second flash-artifact enabler beside Shimmer Myr, directly increasing access to Ashad's once-per-turn casualty condition on other players' turns, though legendary Liberator cannot itself receive nonlegendary casualty. Technomancer, Cyberman Patrol, and original nine full-100 variants were retained as documented alternative hypotheses; no quota padding.

## Verified full-list characteristics

- **Exactly 100 physical cards across 95 lines/distinct names**, commander first; basics Island ×3, Mountain ×2, Swamp ×3, only legal repetitions.
- **32 lands + eight rocks**; source probability of ≥4 lands/rocks among 10 random draws is ~0.6363, **not** a guarantee of UBR colored mana or turn-four Ashad.
- **All selected 95** current sourced Oracle entries Commander-legal within U/B/R; no designated project-ban exception.
- **Five** Game Changers: Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Ancient Tomb, Mishra's Workshop.
- Power Bracket **4 — Optimized**; Archidekt tags **Artifact Copy / Casualty Aristocrats / Artifact Combo**.
- Independent source-bound rules include casualty 2 on the first *nonlegendary artifact spell* each turn; finite opponent-turn flash rules, spell copy not cast/token-creation distinction; Razorlash / Pitiless Plunderer / Phyrexian Altar loop conditionally **mana-neutral**, not an unrestricted infinite-mana loop; Workshop only casts artifact spells; mana/life tradeoffs.
- **All seven GitHub focused check runs SUCCESS** on exact engineering head `ef7a1f726f26648886cf9b44069f2c8e205df189`, including two strict Rev3 I/J executions, exact source and the owner-equivalent Pass C provenance guard. This is **not** statistical multiplayer simulation or comprehensive historical-suite certification.

## Locking and scope

Only this exact 100/SHA can be transferred to the canonical approval file and `state/current_deck_overrides.json` / deck index 4 of the tracker. All older approvals, prior four M7 locks, and remaining 57 canonical deck states stay untouched. Canonical exact-head CI is required before merge. After merge, refetch `main` and independently confirm SHA, registry, tracker, and unchanged historical file, recording actual PR/commit provenance. Never reopen without Cory's explicit request.

**Owner approval is explicit.** Technical I/J is finite, candidate-scoped and does not automatically accept project-wide M6.10/M7/M8 milestones.
