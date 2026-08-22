"""
Iran AI Trader Professional

Scanner V2

Sprint45-13

Order Planning + Position Management
Integration Test

IMPORTANT:
This test does NOT connect to a broker.
"""


from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)

from scanner_v2.position_management_engine import (
    PositionManagementEngine
)


def test_order_position_integration():

    order_engine = OrderPlanningEngine(
        lot_size=1
    )

    position_engine = PositionManagementEngine()

    # -------------------------------------------------
    # Approved portfolio allocation results
    # -------------------------------------------------

    portfolio = [

        {
            "symbol": "TEST1",

            "signal": "STRONG BUY",

            "capital": 20_000_000,

            "price": 1000,

            "allocation_percent": 20.0
        },

        {
            "symbol": "TEST2",

            "signal": "BUY",

            "capital": 11_940_000,

            "price": 2000,

            "allocation_percent": 11.94
        }
    ]

    # -------------------------------------------------
    # STEP 1
    # Build orders
    # -------------------------------------------------

    orders = order_engine.build_orders(
        portfolio
    )

    assert len(orders) == 2

    assert orders[0][
        "status"
    ] == "READY"

    assert orders[1][
        "status"
    ] == "READY"

    assert orders[0][
        "broker_execution"
    ] is False

    assert orders[1][
        "broker_execution"
    ] is False

    # -------------------------------------------------
    # STEP 2
    # Convert order plans into trade plans
    #
    # PositionManagementEngine expects:
    # final_status
    # entry_price
    # quantity
    # risk_reward
    # -------------------------------------------------

    trade_plans = [

        {

            "symbol": orders[0][
                "symbol"
            ],

            "final_status": "READY",

            "entry_price": orders[0][
                "price"
            ],

            "quantity": orders[0][
                "quantity"
            ],

            "risk_reward": 3.0

        },

        {

            "symbol": orders[1][
                "symbol"
            ],

            "final_status": "READY",

            "entry_price": orders[1][
                "price"
            ],

            "quantity": orders[1][
                "quantity"
            ],

            "risk_reward": 2.0

        }
    ]

    # -------------------------------------------------
    # STEP 3
    # Build positions
    # -------------------------------------------------

    positions = position_engine.build(
        trade_plans
    )

    assert len(positions) == 2

    assert positions[0][
        "symbol"
    ] == "TEST1"

    assert positions[1][
        "symbol"
    ] == "TEST2"

    assert positions[0][
        "status"
    ] == "OPEN"

    assert positions[1][
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # Verify risk levels
    # -------------------------------------------------

    assert positions[0][
        "stop_loss"
    ] < positions[0][
        "entry_price"
    ]

    assert positions[0][
        "take_profit"
    ] > positions[0][
        "entry_price"
    ]

    assert positions[1][
        "stop_loss"
    ] < positions[1][
        "entry_price"
    ]

    assert positions[1][
        "take_profit"
    ] > positions[1][
        "entry_price"
    ]

    # -------------------------------------------------
    # STEP 4
    # Normal price update
    # -------------------------------------------------

    updated = position_engine.update_price(
        positions[0],
        1100
    )

    assert updated[
        "status"
    ] == "OPEN"

    assert updated[
        "current_price"
    ] == 1100

    # -------------------------------------------------
    # STEP 5
    # Take profit
    # -------------------------------------------------

    target = positions[0][
        "take_profit"
    ]

    updated = position_engine.update_price(
        positions[0],
        target
    )

    assert updated[
        "status"
    ] == "CLOSED"

    assert updated[
        "exit_reason"
    ] == "TAKE PROFIT"

    # -------------------------------------------------
    # STEP 6
    # Stop loss on second position
    # -------------------------------------------------

    stop = positions[1][
        "stop_loss"
    ]

    updated = position_engine.update_price(
        positions[1],
        stop
    )

    assert updated[
        "status"
    ] == "CLOSED"

    assert updated[
        "exit_reason"
    ] == "STOP LOSS"

    # -------------------------------------------------
    # Final statistics
    # -------------------------------------------------

    statistics = (
        position_engine.statistics()
    )

    assert statistics[
        "total_positions"
    ] == 2

    assert statistics[
        "open"
    ] == 0

    assert statistics[
        "closed"
    ] == 2

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    print()

    print(
        "=" * 60
    )

    print(
        "ORDER + POSITION MANAGEMENT"
    )

    print(
        "=" * 60
    )

    for position in positions:

        print(
            position["symbol"],
            "| Entry:",
            position["entry_price"],
            "| Stop:",
            position["stop_loss"],
            "| Target:",
            position["take_profit"],
            "| Status:",
            position["status"],
            "| Exit:",
            position["exit_reason"]
        )

    print()

    print(
        "Open:",
        statistics["open"]
    )

    print(
        "Closed:",
        statistics["closed"]
    )

    print(
        "=" * 60
    )