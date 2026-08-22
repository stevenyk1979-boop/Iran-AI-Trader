"""
Iran AI Trader Professional

Scanner V2

Sprint47

Recovery Analytics Engine Test
"""

from scanner_v2.recovery_analytics_engine import (
    RecoveryAnalyticsEngine
)


def test_recovery_analytics_engine():

    engine = (
        RecoveryAnalyticsEngine(
            starting_capital=100_000_000
        )
    )

    trades = [

        {
            "pnl": 15_000_000
        },

        {
            "pnl": -12_000_000
        },

        {
            "pnl": 5_000_000
        },

        {
            "pnl": 7_000_000
        }

    ]

    history = (
        engine.process_trades(
            trades
        )
    )

    assert len(history) == 4

    # -------------------------------------------------
    # TEST1
    # Peak = 115M
    # -------------------------------------------------

    assert (
        history[0]["equity"]
        == 115_000_000
    )

    assert (
        history[0]["recovery_status"]
        == "FULLY RECOVERED"
    )

    # -------------------------------------------------
    # TEST2
    # Equity = 103M
    # Bottom = 103M
    # -------------------------------------------------

    assert (
        history[1]["equity"]
        == 103_000_000
    )

    assert (
        history[1]["drawdown_bottom"]
        == 103_000_000
    )

    assert (
        history[1]["recovery_amount"]
        == 0.0
    )

    assert (
        history[1]["recovery_percent"]
        == 0.0
    )

    assert (
        history[1]["recovery_status"]
        == "DRAWDOWN"
    )

    # -------------------------------------------------
    # TEST3
    # Equity = 108M
    #
    # Recovery:
    # 108 - 103 = 5M
    #
    # Required:
    # 115 - 103 = 12M
    #
    # Recovery = 41.67%
    # -------------------------------------------------

    assert (
        history[2]["equity"]
        == 108_000_000
    )

    assert (
        history[2]["recovery_amount"]
        == 5_000_000
    )

    assert (
        history[2]["recovery_percent"]
        == 41.67
    )

    assert (
        history[2]["recovery_status"]
        == "RECOVERING"
    )

    # -------------------------------------------------
    # TEST4
    # Equity = 115M
    # Full recovery
    # -------------------------------------------------

    assert (
        history[3]["equity"]
        == 115_000_000
    )

    assert (
        history[3]["recovery_status"]
        == "FULLY RECOVERED"
    )

    assert (
        history[3]["recovery_percent"]
        == 100.0
    )

    assert (
        engine.max_drawdown
        == 12_000_000
    )

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "RECOVERY ANALYTICS ENGINE"
    )

    print("=" * 60)

    for index, item in enumerate(
        history,
        start=1
    ):

        print(

            f"TEST{index}",

            "| Equity:",
            item["equity"],

            "| Peak:",
            item["peak_equity"],

            "| DD:",
            item["max_drawdown"],

            "| Recovery:",
            item["recovery_percent"],

            "%",

            "| Status:",
            item["recovery_status"]

        )

    print("-" * 60)

    print(
        "Maximum Drawdown:",
        engine.max_drawdown
    )

    print("=" * 60)