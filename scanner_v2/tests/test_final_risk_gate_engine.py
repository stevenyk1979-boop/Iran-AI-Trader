
"""
Iran AI Trader Professional

Scanner V2

Sprint46-07

Final Risk Gate Engine Test
"""

from scanner_v2.final_risk_gate_engine import (
    FinalRiskGateEngine
)


def test_final_risk_gate_engine():

    engine = (
        FinalRiskGateEngine()
    )

    plans = [

        {
            "symbol": "TEST1",
            "final_status": "READY",
            "quantity": 20000,
            "order_value": 20000000
        },

        {
            "symbol": "TEST2",
            "final_status": "READY",
            "quantity": 5970,
            "order_value": 11940000
        },

        {
            "symbol": "TEST3",
            "final_status": "READY",
            "quantity": 10000,
            "order_value": 10000000
        },

        {
            "symbol": "TEST4",
            "final_status": "REJECTED",
            "quantity": 0,
            "order_value": 0
        }

    ]

    portfolio_risk = {

        "status": "CONTROLLED"

    }

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
        },

        {
            "symbol": "TEST4",
            "decision": "BLOCK",
            "reason":
                "TRADE_PLAN_NOT_READY"
        }

    ]

    results = engine.evaluate_all(
        plans,
        portfolio_risk,
        risk_decisions
    )

    assert len(
        results
    ) == 4

    assert (
        results[0]["decision"]
        == "ALLOW"
    )

    assert (
        results[1]["decision"]
        == "ALLOW_WITH_WARNING"
    )

    assert (
        results[2]["decision"]
        == "BLOCK"
    )

    assert (
        results[3]["decision"]
        == "BLOCK"
    )

    stats = (
        engine.statistics()
    )

    assert stats == {

        "approved": 1,

        "warning": 1,

        "blocked": 2,

        "total": 4

    }

    print(
        "============================================================"
    )

    print(
        "FINAL RISK GATE ENGINE TEST"
    )

    print(
        "============================================================"
    )

    for result in results:

        print(
            result["symbol"],
            "| Decision:",
            result["decision"],
            "| Reason:",
            result["reason"]
        )

    print(
        "============================================================"
    )

    print(
        "PASSED"
    )

