# test_scanner_regime_integration.py


from scanner_v2.scanner import Scanner


def test_scanner_regime_integration():

    scanner = Scanner()

    market_regime_data = {
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

    results = scanner.scan(
        market_regime_data=market_regime_data
    )

    print()
    print("=" * 60)
    print("SCANNER + MARKET REGIME INTEGRATION TEST")
    print("=" * 60)

    print()

    print(
        "Market Regime:",
        scanner.market_regime["regime"]
    )

    print(
        "Market Regime Score:",
        scanner.market_regime["score"]
    )

    print(
        "Total Results:",
        len(results)
    )

    for result in results:

        print(
            result["symbol"],
            "| Score:",
            result["score"],
            "| Decision:",
            result["decision"],
            "| Regime:",
            result["market_regime"],
            "| Regime Score:",
            result["market_regime_score"]
        )

    assert results is not None
    assert len(results) > 0

    assert scanner.market_regime["regime"] == "BULL"
    assert scanner.market_regime["score"] == 71.0

    for result in results:

        assert "market_regime" in result
        assert "market_regime_score" in result

        assert (
            result["market_regime"]
            == "BULL"
        )

        assert (
            result["market_regime_score"]
            == 71.0
        )


