"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Position Management Engine Test
"""

from scanner_v2.position_management_engine import (
    PositionManagementEngine
)


def test_position_management_engine():

    engine = PositionManagementEngine()

    plans = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "quantity": 20000,
            "risk_reward": 3.0,
            "final_status": "READY"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "quantity": 5970,
            "risk_reward": 2.0,
            "final_status": "READY"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1500,
            "quantity": 0,
            "risk_reward": 2.0,
            "final_status": "REJECTED"
        }

    ]

    positions = engine.build(
        plans
    )

    print()
    print("=" * 60)
    print("POSITION MANAGEMENT ENGINE TEST")
    print("=" * 60)

    for index, position in enumerate(
        positions,
        start=1
    ):

        print(
            index,
            position["symbol"],
            "| Entry:",
            position["entry_price"],
            "| Stop:",
            position["stop_loss"],
            "| Target:",
            position["take_profit"],
            "| Status:",
            position["status"]
        )

    # -------------------------------------------------
    # Only READY trade plans become positions
    # -------------------------------------------------

    assert len(
        positions
    ) == 2

    # -------------------------------------------------
    # TEST1
    # -------------------------------------------------

    assert positions[0][
        "symbol"
    ] == "TEST1"

    assert positions[0][
        "status"
    ] == "OPEN"

    # R/R = 3
    # Risk = 25%
    # Stop = 750
    # Target = 1750

    assert positions[0][
        "stop_loss"
    ] == 750.0

    assert positions[0][
        "take_profit"
    ] == 1750.0

    # -------------------------------------------------
    # Test Stop Loss
    # -------------------------------------------------

    updated = engine.update_price(
        positions[0],
        740
    )

    assert updated[
        "status"
    ] == "CLOSED"

    assert updated[
        "exit_reason"
    ] == "STOP LOSS"

    # -------------------------------------------------
    # TEST2
    # -------------------------------------------------

    assert positions[1][
        "symbol"
    ] == "TEST2"

    assert positions[1][
        "status"
    ] == "OPEN"

    # R/R = 2
    # Risk = 33.33%
    # Stop ≈ 1333.33
    # Target ≈ 3333.33

    assert positions[1][
        "stop_loss"
    ] == 1333.33

    assert positions[1][
        "take_profit"
    ] == 3333.33

    # -------------------------------------------------
    # Test Take Profit
    #
    # 3000 is below the target.
    # 3400 is above the target.
    # -------------------------------------------------

    updated = engine.update_price(
        positions[1],
        3400
    )

    assert updated[
        "status"
    ] == "CLOSED"

    assert updated[
        "exit_reason"
    ] == "TAKE PROFIT"

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    stats = engine.statistics()

    assert stats[
        "total_positions"
    ] == 2

    assert stats[
        "closed"
    ] == 2

    assert stats[
        "open"
    ] == 0