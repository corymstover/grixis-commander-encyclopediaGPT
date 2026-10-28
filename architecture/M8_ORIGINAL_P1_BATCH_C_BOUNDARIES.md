# M8 original-P1 bounded batch C — source-bound Bolas / Thraximundar mechanics

October 28, 2026. **Seventeen** original P1 cases, all in the still-deferred source-hash set, now have positive and adverse executable predicates with exact-current 100-card inventory checks. This batch does **not** change decks, owner approvals, existing test receipts, project exceptions or release status. The Git commit, test blob and successful exact-head CI must be available **before** a separate case-disposition PR can add these 17 to the canonical M8 register.

| Deck exact approved SHA | Newly tested bounded P1 | Deliberately deferred |
|---|---|---|
| Nicol Bolas `a6079935...` | K4–K6, E1–E2, F2 (6) | W1–W2; broad no-deterministic-combo F3 |
| Nicol Bolas, the Ravager `acfa7922...` | K4–K6, E1–E2, F2–F3 (7) | W1–W3; complete loyalty-win proof |
| Thraximundar `f3e71b71...` | K4, E1–E2, F3 (4) | W1–W2; subjective counterspell-density F2 |

The original **No Mercy** claim (Nicol Bolas K7) is **already superseded in the existing M8 evidence register** and must not be counted again. One **additional separately candidate supersession** concerns Force of Will (absent from current Thraximundar list, original K5). It must reference its exact-current M7 transfer receipt and explicitly distinguish still-surviving lines in the second PR; it is not an executed match result.

## Technical boundaries

- **Nicol Bolas:** The printed upkeep UBR tax must be paid each time or Bolas is sacrificed. Chandra's Ignition uses the source creature's power against *other* creatures, including your own, and each opponent; it is noncombat damage. A creature being Nicol Bolas as the damage source controls the hand-discard trigger. Real opposing discards matter to Waste Not and Geth's Grimoire. The numeric tests do not count new mana sources, combat blocks, alternate costs or prove there is no combo elsewhere in 99.
- **Nicol Bolas, the Ravager:** Displacer Kitten requires a noncreature cast and controlled eligible nonland target; a flickered transforming DFC will return front-side up, not retain a prior planeswalker face. Deliver Unto Evil recognizes a Bolas planeswalker on battlefield, whereas casting a creature Ravager and later transforming it is *not* casting a Bolas planeswalker spell for Dark Intimations. A Spark Double copy of a planeswalker is nonlegendary and adds a loyalty counter. Ravager transforms only at sorcery speed for `{4}{U}{B}{R}` (or `{2}{U}{B}{R}` with Training Grounds on the creature). The Chain Veil permits an added loyalty activation if resolved and paid; **Rings of Brighthearth merely copies one activated ability**, not a third loyalty activation. Defending combat damage can remove a planeswalker at zero loyalty, while artifact removal stops future Veil uses.
- **Thraximundar:** Gravecrawler may be cast from grave with another Zombie controlled and payable `{B}`. Thraximundar gets counters from any player actually sacrificing a creature (not merely being targeted by a sacrifice effect). Grave Pact/Dictate effects cannot force opponents to sacrifice a creature they do not have; two effects resolve separately. Exiled Gravecrawler is not a graveyard cast target.

These tests deliberately model **finite prerequisites and counterexamples** only. They are not an entire Magic rules engine, stack-legal engine simulation, adversarial strategic opponent, mana-curve randomization, or independently executed infinite combo. The remaining W and global F cases stay unproven until appropriately tested or explicitly accepted under owner policy. Full M8 release still requires comprehensive remaining original case coverage, final export and owner acceptance.
