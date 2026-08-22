"""
Iran AI Trader Professional

Scanner V2

Sprint46

Performance Analytics Engine Test
"""

from scanner_v2.performance_analytics_engine import (
    PerformanceAnalyticsEngine
)


def test_performance_analytics_engine():

    trades = [

        {
            "symbol": "TEST1",
            "pnl": 15_000_000,
            "result": "WIN"
        },

        {
            "symbol": "TEST2",
            "pnl": -2_000_000,
            "result": "LOSS"
        },

        {
            "symbol": "TEST3",
            "pnl": 0,
            "result": "BREAKEVEN"
        }

    ]

    engine = (
        PerformanceAnalyticsEngine(
            trades
        )
    )

    # -------------------------------------------------
    # BASIC PERFORMANCE
    # -------------------------------------------------

    assert engine.total_pnl() == 13_000_000

    assert engine.total_profit() == 15_000_000

    assert engine.total_loss() == -2_000_000

    assert engine.win_rate() == 33.33

    assert engine.average_win() == 15_000_000

    assert engine.average_loss() == -2_000_000

    # -------------------------------------------------
    # EXPECTANCY
    # -------------------------------------------------

    assert engine.expectancy() == 4_333_333.33

    # -------------------------------------------------
    # PROFIT FACTOR
    # -------------------------------------------------

    assert engine.profit_factor() == 7.5

    # -------------------------------------------------
    # DRAWDOWN
    # -------------------------------------------------

    assert (
        engine.max_drawdown(
            100_000_000
        )
        == 2_000_000
    )

    # -------------------------------------------------
    # RETURN
    # -------------------------------------------------

    assert (
        engine.return_percent(
            100_000_000
        )
        == 13.0
    )

    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    assert (
        engine.performance_status()
        == "STRONG"
    )

    # -------------------------------------------------
    # STATISTICS
    # -------------------------------------------------

    stats = (
        engine.statistics(
            100_000_000
        )
    )

    assert stats[
        "total_trades"
    ] == 3

    assert stats[
        "wins"
    ] == 1

    assert stats[
        "losses"
    ] == 1

    assert stats[
        "win_rate_percent"
    ] == 33.33

    assert stats[
        "net_pnl"
    ] == 13_000_000

    assert stats[
        "expectancy"
    ] == 4_333_333.33

    assert stats[
        "profit_factor"
    ] == 7.5

    assert stats[
        "max_drawdown"
    ] == 2_000_000

    assert stats[
        "return_percent"
    ] == 13.0

    assert stats[
        "performance_status"
    ] == "STRONG"

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "PERFORMANCE ANALYTICS ENGINE"
    )

    print("=" * 60)

    print(
        "Total Trades:",
        stats[
            "total_trades"
        ]
    )

    print(
        "Win Rate:",
        stats[
            "win_rate_percent"
        ],
        "%"
    )

    print(
        "Net P/L:",
        stats[
            "net_pnl"
        ]
    )

    print(
        "Expectancy:",
        stats[
            "expectancy"
        ]
    )

    print(
        "Profit Factor:",
        stats[
            "profit_factor"
        ]
    )

    print(
        "Max Drawdown:",
        stats[
            "max_drawdown"
        ]
    )

    print(
        "Return:",
        stats[
            "return_percent"
        ],
        "%"
    )

    print(
        "Performance:",
        stats[
            "performance_status"
        ]
    )

    print("=" * 60)