from scanner_v2.pre_trade_validation_engine import (
    PreTradeValidationEngine
)


def test_pre_trade_validation_engine():

    engine = PreTradeValidationEngine(
        max_order_value=35_000_000
    )

    orders = [

        {
            "symbol": "TEST1",
            "side": "BUY",
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
            "side": "BUY",
            "signal": "BUY",
            "price": 2000,
            "capital": 11_940_000,
            "allocation_percent": 11.94,
            "quantity": 5970,
            "order_value": 11_940_000,
            "status": "READY",
            "broker_execution": False
        },

        # Invalid signal
        {
            "symbol": "TEST3",
            "side": "BUY",
            "signal": "WATCH",
            "price": 1500,
            "capital": 8_060_000,
            "quantity": 5373,
            "order_value": 8_059_500,
            "status": "READY",
            "broker_execution": False
        },

        # Inconsistent order value
        {
            "symbol": "TEST4",
            "side": "BUY",
            "signal": "BUY",
            "price": 1000,
            "capital": 5_000_000,
            "quantity": 4000,
            "order_value": 3_000_000,
            "status": "READY",
            "broker_execution": False
        },

        # Broker execution must remain disabled
        {
            "symbol": "TEST5",
            "side": "BUY",
            "signal": "BUY",
            "price": 1000,
            "capital": 2_000_000,
            "quantity": 2000,
            "order_value": 2_000_000,
            "status": "READY",
            "broker_execution": True
        }
    ]


    valid = engine.validate_orders(
        orders
    )


    print()
    print("=" * 60)
    print("PRE-TRADE VALIDATION ENGINE TEST")
    print("=" * 60)


    for order in valid:

        print(
            order["symbol"],
            "| Status:",
            order["validation_status"],
            "| Value:",
            order["order_value"]
        )


    print()
    print(
        "Rejected:",
        len(
            engine.get_rejected_orders()
        )
    )


    assert len(valid) == 2

    assert valid[0][
        "symbol"
    ] == "TEST1"

    assert valid[1][
        "symbol"
    ] == "TEST2"

    assert len(
        engine.get_rejected_orders()
    ) == 3

    assert all(
        order[
            "validation_status"
        ] == "READY"
        for order in valid
    )

    assert all(
        order[
            "broker_execution"
        ] is False
        for order in valid
    )

    assert (
        engine.statistics()[
            "broker_execution"
        ] is False
    )