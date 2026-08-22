"""
Iran AI Trader Professional

Scanner V2

Sprint46

Equity Curve + Drawdown Engine Test
"""

from scanner_v2.equity_drawdown_engine import (
    EquityDrawdownEngine
)


def test_equity_drawdown_engine():

    engine = (
        EquityDrawdownEngine(
            starting_capital=100_000_000
        )
    )

    trades = [

        {
            "symbol": "TEST1",
            "pnl": 15_000_000
        },

        {
            "symbol": "TEST2",
            "pnl": -2_000_000
        },

        {
            "symbol": "TEST3",
            "pnl": -10_000_000
        },

        {
            "symbol": "TEST4",
            "pnl": 5_000_000
        }

    ]

    curve = (
        engine.process_trades(
            trades
        )
    )

    assert len(curve) == 4

    # -------------------------------------------------
    # TRADE 1
    # -------------------------------------------------

    assert (
        curve[0]["equity"]
        == 115_000_000
    )

    assert (
        curve[0]["peak_equity"]
        == 115_000_000
    )

    assert (
        curve[0]["drawdown"]
        == 0.0
    )

    # -------------------------------------------------
    # TRADE 2
    # -------------------------------------------------

    assert (
        curve[1]["equity"]
        == 113_000_000
    )

    assert (
        curve[1]["drawdown"]
        == 2_000_000
    )

    # -------------------------------------------------
    # TRADE 3
    # -------------------------------------------------

    assert (
        curve[2]["equity"]
        == 103_000_000
    )

    assert (
        curve[2]["drawdown"]
        == 12_000_000
    )

    # -------------------------------------------------
    # TRADE 4
    # -------------------------------------------------

    assert (
        curve[3]["equity"]
        == 108_000_000
    )

    assert (
        curve[3]["drawdown"]
        == 7_000_000
    )

    # -------------------------------------------------
    # MAX DRAWDOWN
    # -------------------------------------------------

    assert (
        engine.max_drawdown()
        == 12_000_000
    )

    assert (
        engine.max_drawdown_percent()
        == 10.43
    )

    # -------------------------------------------------
    # CURRENT STATE
    # -------------------------------------------------

    state = (
        engine.current_state()
    )

    assert (
        state["equity"]
        == 108_000_000
    )

    assert (
        state["peak_equity"]
        == 115_000_000
    )

    assert (
        state["drawdown"]
        == 7_000_000
    )

    assert (
        state["drawdown_percent"]
        == 6.09
    )

    assert (
        state["max_drawdown"]
        == 12_000_000
    )

    assert (
        state["trades"]
        == 4
    )

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "EQUITY CURVE + DRAWDOWN ENGINE"
    )

    print("=" * 60)

    for index, item in enumerate(
        curve,
        start=1
    ):

        print(

            f"TEST{index}",

            "| Equity:",
            item["equity"],

            "| Peak:",
            item["peak_equity"],

            "| Drawdown:",
            item["drawdown"],

            "| DD %:",
            item["drawdown_percent"]

        )

    print("-" * 60)

    print(
        "Final Equity:",
        engine.current_equity()
    )

    print(
        "Maximum Drawdown:",
        engine.max_drawdown()
    )

    print(
        "Maximum Drawdown %:",
        engine.max_drawdown_percent()
    )

    print("=" * 60)