import math
import unittest

from scripts.analyze_abaddon_baseline_consistency import (
    parse_deck_text,
    probability_at_least,
    probability_joint_lands_and_acceleration,
)


class AbaddonBaselineConsistencyTests(unittest.TestCase):
    def test_source_parser_counts_roles_and_commander(self):
        sample = (
            "1x Abaddon the Despoiler (40k) 171 [Commander{top}]\n"
            "1x Sol Ring (cmm) 396 [Ramp]\n"
            "2x Island (m21) 310 [Land]\n"
        )
        cards, roles, commanders = parse_deck_text(sample)
        self.assertEqual(sum(cards.values()), 4)
        self.assertEqual(roles["Land"], 2)
        self.assertEqual(roles["Ramp"], 1)
        self.assertEqual(sum(commanders.values()), 1)

    def test_exact_hypergeometric_reference_values(self):
        self.assertTrue(math.isclose(
            probability_at_least(99, 34, 7, 2), 0.7645902428807267, abs_tol=1e-12
        ))
        self.assertTrue(math.isclose(
            probability_at_least(99, 34, 7, 3), 0.4533262306896876, abs_tol=1e-12
        ))
        self.assertTrue(math.isclose(
            probability_joint_lands_and_acceleration(99, 34, 12, 7, 2),
            0.43486308790748673, abs_tol=1e-12
        ))
        self.assertTrue(math.isclose(
            probability_joint_lands_and_acceleration(99, 34, 12, 10, 3),
            0.523032187282957, abs_tol=1e-12
        ))

    def test_invalid_hypergeometric_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            probability_at_least(99, 100, 7, 1)
        with self.assertRaises(ValueError):
            probability_joint_lands_and_acceleration(99, 90, 20, 7, 2)


if __name__ == "__main__":
    unittest.main()
