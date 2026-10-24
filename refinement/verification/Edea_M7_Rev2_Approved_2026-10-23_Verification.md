# Edea M7 Rev2 — canonical SHA-bound verification record

**Owner decision:** "Approved" on 2026-10-23 after full Edea list, all five substitution pairs and exact raw SHA.
**Approved SHA-256:** `a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`
**Historical SHA-256:** `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`, file unchanged.
**Canonical status:** owner-approved exact candidate; merge and post-merge main rehash required before release certification.
**Engineering source:** PR #691 HEAD `734f2c2b18697e3b420697ac8c3a9bc134b183f1`, exact-head Actions SUCCESS #40062061450 and #40062034383, prior Grok PR #664 unchanged.
**Oracle:** 94 selected records from October 23 live Scryfall archived research, all Commander legal and within UBR; no exceptions. Copy intentionally preserves archived research metadata/status as it existed before owner approval; source is not rewritten as though fetched later.

## Specific audit gates

- 100 physical; 94 distinct; Island/Mountain/Swamp ×3 and no other repeat.
- 35 lands; six permanent mana rocks; three Game Changers Ancient Tomb, Demonic Tutor, Fierce Guardianship.
- Edea five targeted substitutions versus Oct14. Evereth/High Market retained per owner; Ayara also retained; other repeatable sacrifice outlets retained.
- Oracle-specific interactions: each beginning of combat yields theft; Assault requires main-phase sorcery, Celebrant exert attack, Kaya's Ghostform returns stolen creature under controller of Aura if trigger resolves before Edea owner-return, Edea draws nonetheless; Hall activation {5}, clone/legend rule until turn end; Geyadrone −3 temporarily steals a creature or planeswalker.
- Mana-color proxy 140k sample reports modest ~0.7–0.8 point access decline due to colored-source loss, not a win rate.
- Only Edea's authority entry/tracker row touched; exact previously approved 15 M7 lists independently regression tested.
- Historical source preserved byte-for-byte. No broad historical test-suite certification or third-model independence claimed.

Exact-head canonical CI and post-merge main rehash are mandatory external validation steps, **not** inferred from this document's presence.
