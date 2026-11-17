"""Run a small illustrative CLV calculation."""
from __future__ import annotations

from clv import calculate_clv


def main() -> None:
    result = calculate_clv(
        entry_odds={"player_1": 2.10, "player_2": 1.80},
        closing_odds={"player_1": 1.95, "player_2": 1.92},
        selection="player_1",
    )
    print("ILLUSTRATIVE EXAMPLE ONLY — replace with timestamped real quotes")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
