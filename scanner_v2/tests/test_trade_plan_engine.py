"""
Iran AI Trader Professional

Scanner V2

Sprint45-03

Trade Plan Engine Test
"""

from scanner_v2.trade_plan_engine import (
    TradePlanEngine
)


def test_trade_plan_engine():

    engine = TradePlanEngine()

    results = [

        {
            "symbol": "TEST1",

            "base_score": 93.85,
            "regime_adjusted_score": 98.54,

            "candidate_score": 100.0,

            "market_regime": "BULL",
            "market_regime_score": 71.0,

            "signal": "STRONG BUY",
            "decision": "STRONG WATCH",

            "risk_status": "LOW RISK",
            "risk_score": 100,

            "risk_reward": 3.0,

            "allocation_percent": 20.0,

            "capital": 20000000,

            "entry_price": 1000,

            "quantity": 20000,

            "order_value": 20000000,

            "validation_status": "READY"
        },

        {
            "symbol": "TEST2",

            "base_score": 85.0,
            "regime_adjusted_score": 89.25,

            "candidate_score": 75.0,

            "market_regime": "BULL",
            "market_regime_score": 71.0,

            "signal": "BUY",
            "decision": "WATCH",

            "risk_status": "LOW RISK",
            "risk_score": 85.26,

            "risk_reward": 2.0,

            "allocation_percent": 11.94,

            "capital": 11940000,

            "entry_price": 2000,

            "quantity": 5970,

            "order_value": 11940000,

            "validation_status": "READY"
        },

        {
            "symbol": "TEST3",

            "base_score": 72.0,
            "regime_adjusted_score": 72.0,

            "candidate_score": 60.0,

            "market_regime": "SIDEWAYS",
            "market_regime_score": 50.0,

            "signal": "WATCH",
            "decision": "WATCH",

            "risk_status": "HIGH RISK",
            "risk_score": 67.2,

            "risk_reward": 0.6,

            "allocation_percent": 0,

            "capital": 0,

            "entry_price": 1500,

            "quantity": 0,

            "order_value": 0,

            "validation_status": "READY"
        }

    ]

    plans = engine.build(
        results
    )

    print()
    print("=" * 60)
    print("TRADE PLAN ENGINE TEST")
    print("=" * 60)

    for index, plan in enumerate(
        plans,
        start=1
    ):

        print(
            index,
            plan["symbol"],
            "| Signal:",
            plan["signal"],
            "| Risk:",
            plan["risk_status"],
            "| Allocation:",
            plan["allocation_percent"],
            "%",
            "| Quantity:",
            plan["quantity"],
            "| Value:",
            plan["order_value"],
            "| Status:",
            plan["final_status"]
        )

    assert len(plans) == 3

    assert plans[0]["symbol"] == "TEST1"

    assert plans[0]["final_status"] == "READY"

    assert plans[1]["final_status"] == "READY"

    assert plans[2]["final_status"] == "REJECTED"

    assert plans[0]["order_value"] == 20000000

    assert plans[0]["quantity"] == 20000

    stats = engine.statistics()

    assert stats["total_plans"] == 3

    assert stats["ready"] == 2

    assert stats["rejected"] == 1