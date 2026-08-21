from scanner_v2.scanner import Scanner
from scanner_v2.watchlist_engine import WatchlistEngine


def test_scanner_watchlist_integration():

    scanner = Scanner()

    watchlist_engine = WatchlistEngine(
        top_n=5
    )

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

    ranked_watchlist = watchlist_engine.build(
        results
    )

    print()
    print("=" * 60)
    print("SCANNER + WATCHLIST INTEGRATION TEST")
    print("=" * 60)

    print()

    print(
        "Market Regime:",
        scanner.market_regime.get(
            "regime"
        )
    )

    print(
        "Market Regime Score:",
        scanner.market_regime.get(
            "score"
        )
    )

    print(
        "Total Scanner Results:",
        len(results)
    )

    print()

    print("TOP 5 WATCHLIST")
    print("-" * 60)

    for item in ranked_watchlist:

        print(
            item["watchlist_rank"],
            item["symbol"],
            "| Base:",
            item.get("score"),
            "| Adjusted:",
            item.get(
                "regime_adjusted_score"
            ),
            "| Final:",
            item.get(
                "final_watchlist_score"
            ),
            "| Decision:",
            item.get(
                "decision"
            )
        )

    assert results is not None

    assert isinstance(
        results,
        list
    )

    assert len(results) == 12

    assert len(
        ranked_watchlist
    ) == 5

    assert (
        ranked_watchlist[0]["symbol"]
        == "TEST1"
    )

    assert (
        ranked_watchlist[0][
            "final_watchlist_score"
        ]
        >=
        ranked_watchlist[1][
            "final_watchlist_score"
        ]
    )

    assert (
        ranked_watchlist[-1][
            "final_watchlist_score"
        ]
        >= 0
    )