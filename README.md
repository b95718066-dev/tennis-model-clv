# Model 03 — CLV Lab

CLV (closing-line value) is an evaluation workflow, not a predictive model. It measures whether the price taken was better than the closing market price.

For a selected outcome, this module removes the margin from the complete entry market and the complete closing market separately, then calculates:

- **Probability CLV:** closing fair probability minus entry fair probability. Positive means the market moved toward the selected outcome after entry.
- **Odds CLV:** entry decimal odds divided by closing decimal odds, minus one. Positive means the entry odds were larger than the closing odds.

Both metrics require complete markets with the same outcome keys and comparable bookmaker/source definitions. The code does not infer timestamps or validate that a quote was genuinely the closing price.

## Example

```python
from experiments.model_03_clv_lab.clv import calculate_clv

result = calculate_clv(
    entry_odds={"player_1": 2.10, "player_2": 1.80},
    closing_odds={"player_1": 1.95, "player_2": 1.92},
    selection="player_1",
)
```

Do not compare a bookmaker's entry price with an exchange close or a different market definition without explicitly recording that difference.

Run the illustrative example:

```bash
python experiments/model_03_clv_lab/example.py
```
