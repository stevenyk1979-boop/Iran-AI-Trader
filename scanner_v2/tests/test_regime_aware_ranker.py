"""
Iran AI Trader Professional

Scanner V2

Regime-Aware Ranking Engine Test
Sprint45-01
"""

from scanner_v2.regime_aware_ranker import RegimeAwareRanker


def test_regime_aware_ranker():

    ranker = RegimeAwareRanker()

    results = [
        {
            "symbol": "TEST1",
            "score": 85,
            "market_regime": "STRONG BULL",
            "market_regime_score": 90
        },
        {
            "symbol": "TEST2",
            "score": 72,
            "market_regime": "BULL",
            "market_regime_score": 70
        },
        {
            "symbol": "TEST3",
            "score": 55,
            "market_regime": "SIDEWAYS",
            "market_regime_score": 50
        }
    ]

    ranked = ranker.rank(results)

    print()
    print("=" * 60)
    print("REGIME AWARE RANKER TEST")
    print("=" * 60)

    print()
    print("Ranked:")
    print(ranked)

    assert ranked is not None
    assert len(ranked) == 3

    assert ranked[0]["symbol"] == "TEST1"

    assert "regime_adjusted_score" in ranked[0]

    assert ranked[0]["regime_adjusted_score"] == 93.5
    assert ranked[1]["regime_adjusted_score"] == 75.6
    assert ranked[2]["regime_adjusted_score"] == 55.0