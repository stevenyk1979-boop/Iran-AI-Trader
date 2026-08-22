"""
Iran AI Trader Professional

Scanner V2

Sprint45-12

Pre-Trade Validation + Order Planning
Integration Test

IMPORTANT:
Validation must happen before order planning.
Rejected orders must never reach OrderPlanningEngine.
"""


from scanner_v2.pre_trade_validation_engine import (
    PreTradeValidationEngine
)

from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)


def test_validation_order_planning_integration():

    validation_engine = (
        PreTradeValidationEngine()
    )

    order_engine = (
        OrderPlanningEngine(
            lot_size=1
        )
    )

    # -------------------------------------------------
    # Input planned orders
    # -------------------------------------------------

    planned_orders = [

        {
            "symbol": "TEST1",

            "signal": "STRONG BUY",

            "price": 1000,

            "capital": 20_000_000,

            "allocation_percent": 20.0,

            "quantity": 20_000,

            "order_value": 20_000_000,

            "status": "READY",

            "broker_execution": False
        },

        {
            "symbol": "TEST2",

            "signal": "BUY",

            "price": 2000,

            "capital": 11_940_000,

            "allocation_percent": 11.94,

            "quantity": 5970,

            "order_value": 11_940_000,

            "status": "READY",

            "broker_execution": False
        },

        # Deliberately invalid order.
        {
            "symbol": "TEST3",

            "signal": "WATCH",

            "price": 3000,

            "capital": 0,

            "allocation_percent": 0,

            "quantity": 0,

            "order_value": 0,

            "status": "REJECTED",

            "broker_execution": False
        }
    ]

    # -------------------------------------------------
    # STEP 1
    # Validate first
    # -------------------------------------------------

    validated_orders = (
        validation_engine.validate_orders(
            planned_orders
        )
    )

    rejected_orders = (
        validation_engine.get_rejected_orders()
    )

    # -------------------------------------------------
    # Validation assertions
    # -------------------------------------------------

    assert len(planned_orders) == 3

    assert len(validated_orders) == 2

    assert len(rejected_orders) == 1

    assert (
        validated_orders[0]["symbol"]
        == "TEST1"
    )

    assert (
        validated_orders[1]["symbol"]
        == "TEST2"
    )

    assert (
        rejected_orders[0]["symbol"]
        == "TEST3"
    )

    # -------------------------------------------------
    # STEP 2
    # Only validated orders enter planning.
    #
    # OrderPlanningEngine expects portfolio-style
    # input containing symbol, signal, capital,
    # price and allocation.
    # -------------------------------------------------

    portfolio_input = []

    for order in validated_orders:

        portfolio_input.append({

            "symbol": order.get(
                "symbol"
            ),

            "signal": order.get(
                "signal"
            ),

            "capital": order.get(
                "capital"
            ),

            "price": order.get(
                "price"
            ),

            "allocation_percent": order.get(
                "allocation_percent",
                0
            )
        })

    # -------------------------------------------------
    # STEP 3
    # Build executable order plans.
    # -------------------------------------------------

    executable_orders = (
        order_engine.build_orders(
            portfolio_input
        )
    )

    # -------------------------------------------------
    # Final assertions
    # -------------------------------------------------

    assert len(executable_orders) == 2

    symbols = [

        order.get(
            "symbol"
        )

        for order in executable_orders
    ]

    assert symbols == [
        "TEST1",
        "TEST2"
    ]

    for order in executable_orders:

        assert order[
            "status"
        ] == "READY"

        assert order[
            "broker_execution"
        ] is False

        assert order[
            "quantity"
        ] > 0

        assert order[
            "order_value"
        ] > 0

    # -------------------------------------------------
    # Safety:
    # rejected TEST3 must never appear.
    # -------------------------------------------------

    assert "TEST3" not in symbols

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    print()

    print(
        "=" * 60
    )

    print(
        "PRE-TRADE VALIDATION + ORDER PLANNING"
    )

    print(
        "=" * 60
    )

    print(
        "Planned:",
        len(planned_orders)
    )

    print(
        "Validated:",
        len(validated_orders)
    )

    print(
        "Rejected:",
        len(rejected_orders)
    )

    print()

    print(
        "EXECUTABLE ORDERS"
    )

    print(
        "-" * 60
    )

    for order in executable_orders:

        print(
            order["symbol"],
            "| Signal:",
            order["signal"],
            "| Quantity:",
            order["quantity"],
            "| Value:",
            order["order_value"],
            "| Status:",
            order["status"]
        )

    print()

    print(
        "TEST3 BLOCKED:",
        "TEST3" not in symbols
    )

    print(
        "=" * 60
    )