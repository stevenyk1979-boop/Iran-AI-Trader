
"""
Iran AI Trader Professional

Scanner V2

Sprint46-06

Risk Alert Decision Engine Test
"""

from scanner_v2.risk_alert_decision_engine import (
    RiskAlertDecisionEngine
)


def test_risk_alert_decision_engine():

    engine = (
        RiskAlertDecisionEngine()
    )

    positions = [

        {
            "symbol": "TEST1",
            "risk_alert": "NORMAL"
        },

        {
            "symbol": "TEST2",
            "risk_alert": "WARNING"
        },

        {
            "symbol": "TEST3",
            "risk_alert": "CRITICAL"
        },

        {
            "symbol": "TEST4",
            "risk_alert": "STOPPED"
        },

        {
            "symbol": "TEST5",
            "risk_alert": "CLOSED"
        }

    ]

    results = engine.evaluate_all(
        positions
    )

    assert len(
        results
    ) == 5

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

    assert (
        results[4]["decision"]
        == "BLOCK"
    )

    assert (
        engine.statistics(
            positions
        )
        == {
            "total": 5,
            "allowed": 1,
            "warning": 1,
            "blocked": 3
        }
    )

    print(
        "============================================================"
    )

    print(
        "RISK ALERT DECISION ENGINE TEST"
    )

    print(
        "============================================================"
    )

    for result in results:

        print(
            result["symbol"],
            "| Alert:",
            result["risk_alert"],
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

