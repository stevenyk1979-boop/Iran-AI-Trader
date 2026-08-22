"""
Iran AI Trader Professional

Scanner V2

Sprint46

Performance + Equity/Drawdown Integration Test
"""

from scanner_v2.performance_risk_analytics_engine import (
    PerformanceRiskAnalyticsEngine
)


def test_performance_risk_analytics_integration():

    starting_capital = 100_000_000

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
            "pnl": -10_000_000,
            "result": "LOSS"
        },

        {
            "symbol": "TEST4",
            "pnl": 5_000_000,
            "result": "WIN"
        }

    ]

    engine = (
        PerformanceRiskAnalyticsEngine(
            trades=trades,
            starting_capital=starting_capital
        )
    )

    summary = (
        engine.refresh()
    )

    # -------------------------------------------------
    # PERFORMANCE
    # -------------------------------------------------

    assert (
        summary["total_trades"]
        == 4
    )

    assert (
        summary["wins"]
        == 2
    )

    assert (
        summary["losses"]
        == 2
    )

    assert (
        summary["net_pnl"]
        == 8_000_000
    )

    assert (
        summary["return_percent"]
        == 8.0
    )

    # -------------------------------------------------
    # EQUITY
    # -------------------------------------------------

    assert (
        summary["equity"]
        == 108_000_000
    )

    assert (
        summary["peak_equity"]
        == 115_000_000
    )

    # -------------------------------------------------
    # DRAWDOWN
    # -------------------------------------------------

    assert (
        summary["max_drawdown"]
        == 12_000_000
    )

    assert (
        summary["max_drawdown_percent"]
        == 10.43
    )

    assert (
        summary["drawdown"]
        == 7_000_000
    )

    assert (
        summary["drawdown_percent"]
        == 6.09
    )

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "PERFORMANCE + EQUITY/DRAWDOWN INTEGRATION"
    )

    print("=" * 60)

    print(
        "Trades:",
        summary[
            "total_trades"
        ]
    )

    print(
        "Wins:",
        summary[
            "wins"
        ]
    )

    print(
        "Losses:",
        summary[
            "losses"
        ]
    )

    print(
        "Win Rate:",
        summary[
            "win_rate_percent"
        ],
        "%"
    )

    print(
        "Net P/L:",
        summary[
            "net_pnl"
        ]
    )

    print(
        "Equity:",
        summary[
            "equity"
        ]
    )

    print(
        "Peak Equity:",
        summary[
            "peak_equity"
        ]
    )

    print(
        "Current Drawdown:",
        summary[
            "drawdown"
        ]
    )

    print(
        "Current Drawdown %:",
        summary[
            "drawdown_percent"
        ],
        "%"
    )

    print(
        "Maximum Drawdown:",
        summary[
            "max_drawdown"
        ]
    )

    print(
        "Maximum Drawdown %:",
        summary[
            "max_drawdown_percent"
        ],
        "%"
    )

    print(
        "Performance:",
        summary[
            "performance_status"
        ]
    )

    print("=" * 60)