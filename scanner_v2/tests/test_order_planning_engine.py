from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)


def test_order_planning_engine():

    engine = OrderPlanningEngine(
        lot_size=1
    )

    portfolio = [

        {
            "symbol": "TEST1",
            "signal": "STRONG BUY",
            "capital": 20_000_000,
            "allocation_percent": 20.0,
            "price": 1000
        },

        {
            "symbol": "TEST2",
            "signal": "BUY",
            "capital": 11_940_000,
            "allocation_percent": 11.94,
            "price": 2000
        },

        {
            "symbol": "TEST3",
            "signal": "WATCH",
            "capital": 8_060_000,
            "allocation_percent": 8.06,
            "price": 1500
        },

        {
            "symbol": "TEST4",
            "signal": "IGNORE",
            "capital": 5_000_000,
            "allocation_percent": 5.0,
            "price": 1000
        }
    ]

    orders = engine.build_orders(
        portfolio
    )

    print(
        "=" * 60
    )

    print(
        "ORDER PLANNING ENGINE TEST"
    )

    print(
        "=" * 60
    )

    for index, order in enumerate(
        orders,
        start=1
    ):

        print(
            index,
            order["symbol"],
            "| Signal:",
            order["signal"],
            "| Quantity:",
            order["quantity"],
            "| Price:",
            order["price"],
            "| Value:",
            order["order_value"],
            "| Status:",
            order["status"]
        )

    assert len(
        orders
    ) == 2

    assert orders[0][
        "symbol"
    ] == "TEST1"

    assert orders[0][
        "quantity"
    ] == 20_000

    assert orders[0][
        "order_value"
    ] == 20_000_000

    assert orders[1][
        "symbol"
    ] == "TEST2"

    assert orders[1][
        "quantity"
    ] == 5_970

    assert orders[1][
        "order_value"
    ] == 11_940_000

    assert all(
        order[
            "status"
        ] == "READY"
        for order in orders
    )

    assert all(
        order[
            "broker_execution"
        ] is False
        for order in orders
    )