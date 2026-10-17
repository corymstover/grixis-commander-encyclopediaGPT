# Grixis Encyclopedia — Authority and Operating Contract

Snapshot: 2026-10-17. Source repository: `corymstover/grixis-commander-encyclopediaGPT`.

## Authority precedence

1. Explicit user decisions and current Project Instructions define intent, approvals and exceptions.
2. Live `main/state/current_deck_overrides.json` defines current-cycle approval/lock state; inspect it before any work. The tracker supplies ordered inventory and supporting stage metadata. Report contradictions rather than silently reconciling them.
3. SHA-bound approved lists and associated verification artifacts define the exact approved deck contents. A status marker alone is not the full decklist.
4. Frozen 2026-10-12 `GrixisFINAL` CSV/TXT exports define the historical baseline, not automatic replacements for approved current-cycle lists.
5. Commander blueprints, decision ledgers, audit evidence, candidate rankings and community research are supporting evidence; none authorizes edits to a locked list.

## Permanent optimization rules

- Commander identity first: maximize the commander's distinctive strategy, not generic Grixis power.
- Optimize within the commander's realistic natural ceiling.
- Avoid homogenization. Popularity and candidate scores are not mandatory additions.
- Verify exact 100-card configuration, commander and companion handling, singleton/copy rules, Grixis identity, Oracle text, legality, relevant rules and combo lines, and strategic coherence before proposing approval.
- Present additions/cuts with reasons and secure explicit user approval. Do not silently unlock or revise an approved deck.
- Do not claim mathematical perfection or gameplay evidence not actually obtained. An automated PASS does not replace substantive review.

## Project exceptions (distinct from official Commander legality)

- Cecily__Bjorna__Lutri: "Lutri, the Spellchaser" — project companion exception.
- Cecily__Bjorna__Lutri: Trade Secrets — project banned-card exception.
- Cecily__Bjorna__Lutri: Yawgmoth's Bargain — project banned-card exception.
- Sauron__Lord_of_the_Rings: Nazgûl — card-specific singleton rule.
- Sauron__the_Dark_Lord: Nazgûl — card-specific singleton rule.
- The_Madcap_Jester: The Madcap Jester — future-release commander.
- The_Madcap_Jester: Dragon's Smile — future-release or project card.
- Tresserhorn_s_Lord__Returned: "Tresserhorn's Lord, Returned" — future-release commander.

These are project-authorized exceptions or card-specific copy rules; they are **not** blanket official legality declarations. Check the live registry and current legality before making a new certification.

## Source pointers

- [Live state](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/state/current_deck_overrides.json)
- [Tracker](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/Deck_Refinement_Tracker_2026-10-12.csv)
- [Exceptions registry](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/source-package/research/Project_Exceptions_Current_2026-10-12.csv)
- [Quality gates](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/architecture/DECK_QUALITY_GATES_V3.md)
- [README](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/README.md)
