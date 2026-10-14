# Anhelo, the Painter — Approval-Ready Closeout

**Cycle:** global-restart-2026-10-13
**State:** APPROVAL_READY / UNLOCKED
**Whole-list review:** PASS
**Closure pass:** zero additional material improvements after the changes below.

## Final changes vs frozen baseline

1. Talrand's Invocation → Cryptic Pursuit
2. Fury Storm → Jadar, Ghoulcaller of Nephalia
3. Double Vision → Deekah, Fractal Theorist
4. Flawless Forgery → Startle

## Why the second closure pass changed two more slots

### Double Vision → Deekah, Fractal Theorist
Double Vision is a five-mana copy engine that overlaps Anhelo's defining ability and only copies the first instant/sorcery cast each turn. Deekah costs the same but supplies Fractal bodies whenever an instant or sorcery is cast **or copied**, so an Anhelo casualty spell produces two Deekah triggers. Those Fractals have X +1/+1 counters where X is the spell's mana value. Spells of mana value 2+ therefore produce future casualty-2 bodies; one-mana spells make 1/1s and do not independently qualify. Deekah's activated ability also creates an unblockability conversion line.

### Flawless Forgery → Startle
Flawless Forgery is five mana, sorcery speed, and depends on a useful instant/sorcery in an opponent's graveyard. Startle is two mana at instant speed, creates a 2/2 decayed Zombie and draws a card. With Anhelo and existing fodder, casualty copies Startle, yielding two cards and two 2/2 Zombies while also shrinking creatures. It is substantially lower ceiling as a standalone spell but much better at keeping the casualty engine supplied across turn cycles.

## Candidate exhaustion / rejected alternatives

- **Metallurgic Summonings:** powerful token engine, but another five-mana noncreature setup card. Deekah is a creature and triggers on both cast and copied instants/sorceries, more directly converting casualty into bodies.
- **Sedgemoor Witch:** excellent magecraft engine, but its Pests are 1/1 and cannot pay casualty 2 without another pump effect.
- **Rotten Reunion:** one mana, flashback, graveyard interaction and a 2/2 decayed Zombie; narrowly missed Startle because Startle replaces itself and is a higher-value casualty copy. Reunion remains a strong metagame swap if graveyard hate becomes necessary.
- **Dogged Detective / Sinister Concierge:** recurring or death-value bodies, but neither improves the spell-casting engine as directly as Jadar, Cryptic Pursuit, Deekah or Startle.
- **Maestros Confluence / Mystic Confluence / Drawn from Dreams:** copyable card-quality spells, but current list already has premium draw/interaction and needs reliable casualty fuel more than additional expensive value.
- **Exsanguinate:** excellent duplicated finisher, but Torment of Hailfire and Crackle with Power already occupy scalable finisher slots; adding another reduces engine density.
- **Squee, the Immortal:** recurring 2-power body but expensive to repeatedly cast and does not create spell-cast payoffs.
- **River's Rebuke:** strong copied one-sided reset but six mana sorcery and redundant with Cyclonic Rift for this list's interaction allocation.
- **Fury Storm:** commander-cast-count dependent and unreliable early.
- **Talrand's Invocation:** excellent when copied but one-shot four-mana fodder; Cryptic Pursuit has higher engine longevity.
- **Double Vision:** redundant five-mana copy layer; replaced by a token engine that rewards the copy Anhelo already provides.
- **Flawless Forgery:** opponent-graveyard-dependent five-mana value; replaced by cheap instant-speed casualty fuel.

## Rules / combo review

- Anhelo gives the **first instant or sorcery spell you cast each turn** casualty 2. The casualty copy is created on the stack and is not cast.
- Casualty requires sacrificing a creature with power 2 or greater as an additional cost; sacrificing cannot be answered after the spell has been cast.
- Cryptic Pursuit triggers only when a qualifying spell is cast from hand. Copies are not casts.
- Jadar checks at the beginning of your end step and creates a decayed 2/2 only if you control no creature with decayed.
- Deekah triggers whenever you cast **or copy** an instant/sorcery spell. A normal Anhelo casualty sequence therefore causes Deekah to trigger for the original cast and the casualty copy. The Fractal size uses the spell's mana value.
- Startle's Zombie is 2/2 and can pay casualty 2 on a later spell. If Startle itself is copied, the copy also creates a Zombie and draws a card.
- Dualcaster Mage + Twinflame remains a deterministic creature-token loop when Twinflame targets a creature you control and Dualcaster is flashed in to copy it, with each copied Twinflame targeting the newest Dualcaster token; hasty tokens enable combat conversion. No Anhelo casualty payment is required for the core loop.
- Storm-Kiln Artist triggers when an instant/sorcery is cast **or copied**, making casualty a mana-positive resource engine in suitable sequences.
- Ral, Storm Conduit triggers when an instant/sorcery is cast or copied and supplies damage conversion for copy loops.

## Structural and legality gates

- Exact quantity: 100.
- Distinct card names: 94.
- Repeats: Island ×3, Mountain ×3, Swamp ×3 only.
- Singleton: PASS.
- Commander identity: UBR.
- New cards: Cryptic Pursuit (UR), Jadar (B), Deekah (U), Startle (U); all within identity.
- Official Commander legality: PASS for all four additions.
- No project-specific exception required.
- Mana base: 31 lands by quantity (28 distinct land names plus repeated basics), supplemented by Sol Ring, Arcane Signet, Fellwar Stone, three Signets, three Talismans, Dark Ritual, Jeska's Will, Goblin Electromancer, Thunderclap Drake, Storm-Kiln Artist and Mana Geyser. This is aggressive but defensible for an optimized list with extensive fast mana/filtering; no land cut is recommended.
- Commander necessity: PASS. The revised creature engines are selected specifically to sustain casualty 2 and convert Anhelo's spell copies into additional bodies/resources; removing Anhelo materially changes the deck's engine.
- Candidate exhaustion: PASS.
- Red-team: PASS.
- Zero-new-material-improvement closure: PASS.

## Approval recommendation

Approve the exact 100-card list at `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt`. Do not lock until explicit user approval.
