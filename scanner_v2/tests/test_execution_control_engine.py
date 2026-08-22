"""
Iran AI Trader Professional

Scanner V2

Sprint46-02

Execution Control Engine Test
"""

from scanner_v2.execution_control_engine import (
    ExecutionControlEngine
)


def test_execution_control_engine():

    engine = ExecutionControlEngine()

    orders = [

        {
            "symbol": "TEST1",
            "side": "BUY",
            "price": 1000,
            "quantity": 20_000,
            "order_value": 20_000_000,
            "execution_status": "READY",
            "broker_execution": False
        },

        {
            "symbol": "TEST2",
            "side": "BUY",
            "price": 2000,
            "quantity": 5_970,
            "order_value": 11_940_000,
            "execution_status":
                "READY_WITH_WARNING",
            "broker_execution": False
        },

        {
            "symbol": "TEST3",
            "side": "BUY",
            "price": 2000,
            "quantity": 10_000,
            "order_value": 20_000_000,
            "execution_status": "BLOCKED",
            "broker_execution": False
        },

        {
            "symbol": "TEST4",
            "side": "BUY",
            "price": 1000,
            "quantity": 20_000,
            "order_value": 25_000_000,
            "execution_status": "READY",
            "broker_execution": False
        }

    ]

    results = engine.control_orders(
        orders
    )

    assert len(results) == 4

    # TEST1
    assert results[0][
        "execution_control"
    ] == "APPROVED"

    assert results[0][
        "approved"
    ] is True

    # TEST2
    assert results[1][
        "execution_control"
    ] == "APPROVED_WITH_WARNING"

    assert results[1][
        "approved"
    ] is True

    # TEST3
    assert results[2][
        "execution_control"
    ] == "BLOCKED"

    assert results[2][
        "approved"
    ] is False

    # TEST4
    assert results[3][
        "execution_control"
    ] == "BLOCKED"

    assert results[3][
        "approved"
    ] is False

    print()

    print("=" * 60)
    print("EXECUTION CONTROL ENGINE TEST")
    print("=" * 60)

    for result in results:

        print(
            result["symbol"],
            "| Control:",
            result["execution_control"],
            "| Reason:",
            result["execution_reason"]
        )

    print("=" * 60)

    stats = engine.statistics()

    assert stats[
        "approved"
    ] == 1

    assert stats[
        "approved_with_warning"
    ] == 1

    assert stats[
        "blocked"
    ] == 2

    assert stats[
        "broker_execution"
    ] is False