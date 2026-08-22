
"""
Iran AI Trader Professional

Scanner V2

Sprint46-08

Final Risk Gate + Order Planning Integration Test

No broker connection.
No real order execution.
"""

from scanner_v2.final_risk_gate_engine import (
    FinalRiskGateEngine
)

from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)


def test_final_risk_gate_order_integration():

    gate_engine = (
        FinalRiskGateEngine()
    )

    order_engine = (
        OrderPlanningEngine()
    )

    # -------------------------------------------------
    # Trade plans
    # -------------------------------------------------

    plans = [

        {
            "symbol": "TEST1",

            "final_status": "READY",

            "signal": "STRONG BUY",

            "price": 1000,

            "capital": 20000000,

            "allocation_percent": 20,

            "quantity": 20000,

            "order_value": 20000000
        },

        {
            "symbol": "TEST2",

            "final_status": "READY",

            "signal": "BUY",

            "price": 2000,

            "capital": 11940000,

            "allocation_percent": 11.94,

            "quantity": 5970,

            "order_value": 11940000
        },

        {
            "symbol": "TEST3",

            "final_status": "READY",

            "signal": "BUY",

            "price": 1000,

            "capital": 10000000,

            "allocation_percent": 10,

            "quantity": 10000,

            "order_value": 10000000
        }

    ]

    # -------------------------------------------------
    # Portfolio risk
    # -------------------------------------------------

    portfolio_risk = {

        "status": "CONTROLLED"

    }

    # -------------------------------------------------
    # Risk decisions
    # -------------------------------------------------

    risk_decisions = [

        {
            "symbol": "TEST1",

            "decision": "ALLOW",

            "reason": "RISK_NORMAL"

        },

        {
            "symbol": "TEST2",

            "decision":
                "ALLOW_WITH_WARNING",

            "reason": "RISK_WARNING"

        },

        {
            "symbol": "TEST3",

            "decision": "BLOCK",

            "reason":
                "RISK_ALERT_CRITICAL"

        }

    ]

    # -------------------------------------------------
    # Final gate
    # -------------------------------------------------

    gate_results = (
        gate_engine.evaluate_all(
            plans,
            portfolio_risk,
            risk_decisions
        )
    )

    assert len(
        gate_results
    ) == 3

    assert (
        gate_results[0]["decision"]
        == "ALLOW"
    )

    assert (
        gate_results[1]["decision"]
        == "ALLOW_WITH_WARNING"
    )

    assert (
        gate_results[2]["decision"]
        == "BLOCK"
    )

    # -------------------------------------------------
    # Build only approved orders
    # -------------------------------------------------

    executable_plans = []

    for index, gate_result in enumerate(
        gate_results
    ):

        if gate_result.get(
            "decision"
        ) in (
            "ALLOW",
            "ALLOW_WITH_WARNING"
        ):

            plan = dict(
                plans[index]
            )

            plan[
                "gate_decision"
            ] = gate_result[
                "decision"
            ]

            plan[
                "gate_reason"
            ] = gate_result[
                "reason"
            ]

            executable_plans.append(
                plan
            )

    orders = (
        order_engine.build_orders(
            executable_plans
        )
    )

    # -------------------------------------------------
    # Assertions
    # -------------------------------------------------

    assert len(
        orders
    ) == 2

    assert (
        orders[0]["symbol"]
        == "TEST1"
    )

    assert (
        orders[0]["status"]
        == "READY"
    )

    assert (
        orders[0]["broker_execution"]
        is False
    )

    assert (
        orders[1]["symbol"]
        == "TEST2"
    )

    assert (
        orders[1]["status"]
        == "READY"
    )

    assert (
        orders[1]["broker_execution"]
        is False
    )

    # -------------------------------------------------
    # Blocked symbol must never become order
    # -------------------------------------------------

    assert not any(

        order.get(
            "symbol"
        ) == "TEST3"

        for order in orders

    )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    stats = (
        order_engine.statistics()
    )

    assert (
        stats["orders"]
        == 2
    )

    assert (
        stats["total_order_value"]
        == 31940000.0
    )

    print(
        "============================================================"
    )

    print(
        "FINAL RISK GATE + ORDER PLANNING"
    )

    print(
        "============================================================"
    )

    for order in orders:

        print(
            order["symbol"],
            "| Gate:",
            order["gate_decision"],
            "| Quantity:",
            order["quantity"],
            "| Value:",
            order["order_value"],
            "| Status:",
            order["status"]
        )

    print(
        "TEST3 BLOCKED:",
        not any(
            order.get(
                "symbol"
            ) == "TEST3"
            for order in orders
        )
    )

    print(
        "============================================================"
    )

    print(
        "PASSED"
    )

