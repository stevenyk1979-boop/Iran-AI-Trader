from scanner_v2.market_regime_adapter import MarketRegimeAdapter


def test_market_regime_adapter():

    adapter = MarketRegimeAdapter()

    data = {
        "price": 120,
        "ema20": 118,
        "ema50": 115,
        "ema100": 110,
        "ema50_prev": 114,

        "positive": 180,
        "negative": 60,
        "unchanged": 40,

        "volume": 1500000,
        "avg_volume": 1000000,

        "value": 8500000000,
        "avg_value": 6000000000,

        "money_flow": 0.65,

        "atr_percent": 2.5,
        "market_volatility": 18,
        "drawdown": 4,

        "index_change": 1.8,
        "equal_change": 0.9
    }

    result = adapter.analyze(data)

    print()
    print("=" * 60)
    print("MARKET REGIME ADAPTER TEST")
    print("=" * 60)

    print()
    print("Result:")
    print(result)

    assert result is not None

    assert "regime" in result
    assert "score" in result

    assert 0 <= result["score"] <= 100