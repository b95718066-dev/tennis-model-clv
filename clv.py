"""Closing-line-value diagnostics for complete decimal-odds markets."""
from __future__ import annotations

from math import isfinite
from typing import Mapping


def _fair_probabilities(odds: Mapping[str, float]) -> dict[str, float]:
    if len(odds) < 2:
        raise ValueError("A complete market must contain at least two outcomes.")
    implied: dict[str, float] = {}
    for outcome, price in odds.items():
        value = float(price)
        if not isfinite(value) or value <= 1.0:
            raise ValueError("All decimal odds must be finite and greater than 1.")
        implied[outcome] = 1.0 / value
    total = sum(implied.values())
    if not isfinite(total) or total <= 0:
        raise ValueError("Market implied probability total must be positive and finite.")
    return {key: value / total for key, value in implied.items()}


def calculate_clv(
    *,
    entry_odds: Mapping[str, float],
    closing_odds: Mapping[str, float],
    selection: str,
) -> dict[str, float | str]:
    """Calculate de-vigged probability CLV and raw odds CLV for one selection."""
    if set(entry_odds) != set(closing_odds):
        raise ValueError("Entry and closing markets must contain identical outcome keys.")
    if selection not in entry_odds:
        raise ValueError("selection must be one of the market outcome keys.")

    entry_fair = _fair_probabilities(entry_odds)
    closing_fair = _fair_probabilities(closing_odds)
    probability_clv = closing_fair[selection] - entry_fair[selection]
    odds_clv = float(entry_odds[selection]) / float(closing_odds[selection]) - 1.0

    return {
        "selection": selection,
        "entry_fair_probability": entry_fair[selection],
        "closing_fair_probability": closing_fair[selection],
        "probability_clv": probability_clv,
        "odds_clv": odds_clv,
        "beat_closing_price": probability_clv > 0.0 and odds_clv > 0.0,
        "method": "proportional_de_vig_on_each_complete_market",
    }
