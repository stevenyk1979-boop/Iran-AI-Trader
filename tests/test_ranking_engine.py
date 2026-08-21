"""
Iran AI Trader Professional

Scanner V2
Ranking Engine Test
"""

from scanner_v2.config import ScannerConfig
from scanner_v2.ranking_engine import RankingEngine


class FakeHistory:

    def __init__(self, prices):
        self._prices = prices

    def close_prices(self):
        return self._prices


def test_ranking_engine():

    config = ScannerConfig()

    engine = RankingEngine(
        config=config
    )

    history = FakeHistory(
        [
            100,
            101,
            102,
            104,
            106,
            108,
            110,
            112,
            114,
            116,
            118,
            120,
            122,
            124,
            126,
            128,
            130,
            132,
            134,
            136
        ]
    )

    result = engine.analyze(
        history,
        "TEST1"
    )

    print()
    print("=" * 60)
    print("RANKING ENGINE TEST")
    print("=" * 60)

    print()
    print("Result:")
    print(result)

    assert result is not None

    assert result["symbol"] == "TEST1"

    assert 0 <= result["score"] <= 100

    assert 0 <= result["price_score"] <= 100

    assert 0 <= result["trend_score"] <= 100

    assert 0 <= result["momentum_score"] <= 100

    assert 0 <= result["direction_score"] <= 100

    assert 0 <= result["strength_score"] <= 100

    assert 0 <= result["consistency_score"] <= 100

    assert result["decision"] in [
        "STRONG WATCH",
        "WATCH",
        "IGNORE",
        "FAILED"
    ]

    assert "ranking_breakdown" in result