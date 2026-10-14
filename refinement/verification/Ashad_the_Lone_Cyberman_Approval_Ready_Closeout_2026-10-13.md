# Ashad, the Lone Cyberman — Approval-Ready Current-Cycle Closeout

**Cycle:** global-restart-2026-10-13
**State:** APPROVAL_READY / UNLOCKED
**Baseline:** frozen 2026-10-12 export, with historical artifacts used as evidence only.

## Final changes vs frozen baseline

1. **Jadar, Ghoulcaller of Nephalia → Solemn Simulacrum**
2. **Dalek Drone → Ichor Wellspring**

The prior-cycle proposal **Twinning Staff → Canoptek Spyder is rejected** in the current cycle. Twinning Staff's first replacement effect applies whenever its controller would copy *a spell*, not merely an instant or sorcery, so it adds an additional copy to Ashad's casualty copy of a nonlegendary artifact spell. The activated ability is the part limited to instant/sorcery spells.

## Final slot decisions

### Solemn Simulacrum over Jadar
Solemn is a 2/2 nonlegendary artifact creature, therefore it is simultaneously a legal casualty-2 body and a spell Ashad can copy. A copied Solemn becomes a token copy and each resolving Solemn produces its own ETB basic-land search. A Solemn later sacrificed to casualty also produces its death draw. Jadar supplies recurring 2/2 bodies but does not participate in the artifact-spell copy axis.

### Ichor Wellspring over Dalek Drone
Dalek Drone is a 3/3 artifact creature whose ETB makes each opponent lose 2 life. It is valid casualty fodder and a reasonable copy target, but its copied ceiling is modest. Ichor Wellspring costs two, draws on ETB, and draws again when put into a graveyard from the battlefield. If Wellspring is the first nonlegendary artifact spell cast on a turn, Ashad can casualty-copy it; the original and token each draw on ETB, and sacrifice outlets can convert them into further draw. Wellspring itself cannot pay casualty 2, so the deck must provide a separate eligible body.

## Critical retained cards

- **Twinning Staff:** core multiplier. Ashad casualty produces an artifact-spell copy; Twinning Staff's replacement effect creates an additional copy.
- **Poetic Ingenuity:** first artifact spell each turn creates a 3/1 Dinosaur, which qualifies for casualty 2 on a later artifact spell; attacking with Dinosaurs produces Treasure.
- **Shimmer Myr:** flash for artifact spells enables Ashad's 'first ... each turn' wording across opponents' turns.
- **Unwinding Clock:** untaps artifacts during other players' untap steps, supporting multi-turn-cycle artifact mana and flash sequencing.
- **Biotransference:** expensive but unusually synergistic: creatures are artifacts in addition to other types, and casting artifact spells creates 2/2 Necron artifact creature tokens that qualify for casualty.
- **Portal to Phyrexia:** nine mana but exceptional when copied; two Portals create two separate sacrifice ETBs and persistent reanimation engines.
- **Simulacrum Synthesizer / Worldwalker Helm / Brudiclad / Cyberdrive Awakener:** preserve the copied-artifact/token conversion plan rather than reducing the deck to generic artifact combo.
- **KCI / Ashnod's Altar / Phyrexian Altar:** sacrifice infrastructure converts artifact creatures/tokens into resources while growing Ashad when creatures are sacrificed.
- **Scrap Trawler / Emry / Goblin Welder / Academy Ruins:** recursion package protects the engine from attrition and recycles artifacts.

## Rules verification

- Ashad applies casualty 2 to the first nonlegendary artifact spell you cast each turn.
- Casualty is an additional cost paid during casting. The sacrifice occurs before opponents can respond to the spell.
- Ashad's casualty copy of an artifact spell becomes a token as it resolves.
- Twinning Staff's first ability is a replacement effect for copying spells generally. If Ashad's casualty would copy the artifact spell once, Staff changes that event to copying it twice.
- Copies of permanent spells become tokens when they resolve.
- Ashad receives a +1/+1 counter whenever **another creature** is sacrificed; Ashad sacrificing itself would not trigger that ability.
- Ichor Wellspring's death-style trigger is broader than dying: it triggers whenever it is put into a graveyard from the battlefield.
- Poetic Ingenuity's Dinosaur token is 3/1, satisfying casualty 2.
- Canoptek Scarab Swarm is 1/1 and is not in the final candidate.
- Canoptek Spyder is not in the final candidate.

## Candidate exhaustion

Reconsidered: Canoptek Spyder, Canoptek Scarab Swarm, Sai, Jadar, Dalek Drone, Twinning Staff, Poetic Ingenuity, Ichor Wellspring and the existing expensive token/artifact payoffs. After correcting Oracle-text errors, no additional candidate produces a sufficiently clear commander-specific improvement without degrading casualty fuel, artifact density, flash-per-turn exploitation, interaction, recursion, or finishing capacity.

**Zero-new-material-improvement closure:** PASS.

## Structural / final gates

- Exact cards including commander: **100 — PASS**
- Distinct names: **95**
- Repeated names: Island ×3, Mountain ×2, Swamp ×3 only — **PASS**
- Singleton: **PASS**
- Commander color identity: UBR — **PASS**
- Additions: Solemn Simulacrum and Ichor Wellspring are colorless — **PASS**
- Official Commander legality of final additions: **PASS**
- No project exception required.
- Commander necessity: **PASS**
- Whole-list audit: **PASS**
- Candidate exhaustion: **PASS**
- Red-team / Oracle correction pass: **PASS**
- Approval: **OPEN — explicit user approval required before lock**

## Recommendation

Approve and lock the exact list at `refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt`.
