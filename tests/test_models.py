import unittest

from clv import calculate_clv


class ClvTests(unittest.TestCase):
    def test_positive_clv_when_entry_price_beats_close(self):
        result = calculate_clv(
            entry_odds={"player_1": 2.10, "player_2": 1.80},
            closing_odds={"player_1": 1.95, "player_2": 1.92},
            selection="player_1",
        )
        self.assertGreater(result["probability_clv"], 0.0)
        self.assertGreater(result["odds_clv"], 0.0)
        self.assertTrue(result["beat_closing_price"])

    def test_rejects_different_market_outcomes(self):
        with self.assertRaises(ValueError):
            calculate_clv(
                entry_odds={"player_1": 2.0, "player_2": 1.9},
                closing_odds={"player_1": 2.0, "player_3": 1.9},
                selection="player_1",
            )

    def test_rejects_invalid_odds(self):
        with self.assertRaises(ValueError):
            calculate_clv(
                entry_odds={"player_1": 1.0, "player_2": 2.0},
                closing_odds={"player_1": 1.9, "player_2": 2.0},
                selection="player_1",
            )


if __name__ == "__main__":
    unittest.main()
