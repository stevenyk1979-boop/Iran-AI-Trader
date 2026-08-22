"""
Iran AI Trader Professional

Scanner V2

Sprint46-01

Execution Readiness Engine Test
"""

from scanner_v2.execution_readiness_engine import (
    ExecutionReadinessEngine
)


def test_execution_readiness_engine():

    engine = ExecutionReadinessEngine()

    orders = [

        {
            "symbol": "TEST1",
            "quantity": 20_000,
            "order_value": 20_000_000,
            "status": "READY",
            "validation_status": "READY",
            "gate_decision": "ALLOW",
            "risk_status": "LOW RISK",
            "broker_execution": False
        },

        {
            "symbol": "TEST2",
            "quantity": 5_970,
            "order_value": 11_940_000,
            "status": "READY",
            "validation_status": "READY",
            "gate_decision": "ALLOW_WITH_WARNING",
            "risk_status": "LOW RISK",
            "broker_execution": False
        },

        {
            "symbol": "TEST3",
            "quantity": 10_000,
            "order_value": 20_000_000,
            "status": "READY",
            "validation_status": "READY",
            "gate_decision": "BLOCK",
            "risk_status": "CRITICAL",
            "broker_execution": False
        },

        {
            "symbol": "TEST4",
            "quantity": 10_000,
            "order_value": 20_000_000,
            "status": "READY",
            "validation_status": "REJECTED",
            "gate_decision": "ALLOW",
            "risk_status": "LOW RISK",
            "broker_execution": False
        }

    ]

    results = engine.evaluate_orders(
        orders
    )

    assert len(results) == 4

    assert results[0][
        "execution_status"
    ] == "READY"

    assert results[0][
        "ready"
    ] is True

    assert results[1][
        "execution_status"
    ] == "READY_WITH_WARNING"

    assert results[1][
        "ready"
    ] is True

    assert results[2][
        "execution_status"
    ] == "BLOCKED"

    assert results[2][
        "ready"
    ] is False

    assert results[3][
        "execution_status"
    ] == "BLOCKED"

    assert results[3][
        "ready"
    ] is False

    print()

    print("=" * 60)
    print("EXECUTION READINESS ENGINE TEST")
    print("=" * 60)

    for result in results:

        print(
            result["symbol"],
            "| Status:",
            result["execution_status"],
            "| Reason:",
            result["execution_reason"]
        )

    print("=" * 60)

    assert engine.statistics()[
        "ready"
    ] == 1

    assert engine.statistics()[
        "ready_with_warning"
    ] == 1

    assert engine.statistics()[
        "blocked"
    ] == 2