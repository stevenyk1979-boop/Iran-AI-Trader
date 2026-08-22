"""
Iran AI Trader Professional

Scanner V2

Sprint45-05

Trailing Stop Engine Test
"""

from scanner_v2.trailing_stop_engine import (
    TrailingStopEngine
)


def test_trailing_stop_engine():

    engine = TrailingStopEngine(
        trailing_percent=5
    )

    positions = [

        {
            "symbol": "TEST1",
            "entry_price": 1000.0,
            "stop_loss": 750.0,
            "take_profit": 1750.0,
            "current_price": 1000.0,
            "status": "OPEN",
            "exit_reason": None
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000.0,
            "stop_loss": 1333.33,
            "take_profit": 3333.33,
            "current_price": 2000.0,
            "status": "OPEN",
            "exit_reason": None
        }

    ]

    print()
    print("=" * 60)
    print("TRAILING STOP ENGINE TEST")
    print("=" * 60)

    # -------------------------------------------------
    # TEST1
    # -------------------------------------------------

    updated = engine.update(
        positions[0],
        1200
    )

    print(
        "TEST1 | Price:",
        updated["current_price"],
        "| Stop:",
        updated["stop_loss"],
        "| Status:",
        updated["status"]
    )

    # 1200 * 0.95 = 1140

    assert updated[
        "stop_loss"
    ] == 1140.0

    assert updated[
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # Stop must never move downward
    # -------------------------------------------------

    updated = engine.update(
        positions[0],
        1150
    )

    print(
        "TEST1 | Price:",
        updated["current_price"],
        "| Stop:",
        updated["stop_loss"],
        "| Status:",
        updated["status"]
    )

    # 1150 * 0.95 = 1092.50
    # But the existing stop is 1140.
    # Therefore stop must remain at 1140.

    assert updated[
        "stop_loss"
    ] == 1140.0

    assert updated[
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # Price reaches trailing stop
    # -------------------------------------------------

    updated = engine.update(
        positions[0],
        1130
    )

    print(
        "TEST1 | Price:",
        updated["current_price"],
        "| Stop:",
        updated["stop_loss"],
        "| Status:",
        updated["status"],
        "| Exit:",
        updated["exit_reason"]
    )

    assert updated[
        "status"
    ] == "CLOSED"

    assert updated[
        "exit_reason"
    ] == "TRAILING STOP"

    # -------------------------------------------------
    # TEST2
    # -------------------------------------------------

    updated = engine.update(
        positions[1],
        3000
    )

    print(
        "TEST2 | Price:",
        updated["current_price"],
        "| Stop:",
        updated["stop_loss"],
        "| Status:",
        updated["status"]
    )

    # 3000 * 0.95 = 2850

    assert updated[
        "stop_loss"
    ] == 2850.0

    assert updated[
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # Multiple positions
    # -------------------------------------------------

    positions = [

        {
            "symbol": "A",
            "stop_loss": 90,
            "status": "OPEN"
        },

        {
            "symbol": "B",
            "stop_loss": 180,
            "status": "OPEN"
        }

    ]

    prices = {
        "A": 100,
        "B": 200
    }

    updated_positions = (
        engine.update_positions(
            positions,
            prices
        )
    )

    assert updated_positions[0][
        "stop_loss"
    ] == 95.0

    assert updated_positions[1][
        "stop_loss"
    ] == 190.0