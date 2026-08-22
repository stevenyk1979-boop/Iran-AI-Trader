"""
Iran AI Trader Professional

Scanner V2

Sprint45-11

Trade Plan + Pre-Trade Validation Integration Test
"""

from scanner_v2.trade_plan_engine import (
    TradePlanEngine
)

from scanner_v2.pre_trade_validation_engine import (
    PreTradeValidationEngine
)


def test_trade_plan_validation_integration():

    trade_engine = TradePlanEngine()

    validation_engine = (
        PreTradeValidationEngine()
    )

    results = [

        {
            "symbol": "TEST1",
            "base_score": 93.85,
            "regime_adjusted_score": 98.54,
            "candidate_score": 100.0,
            "signal": "STRONG BUY",
            "decision": "STRONG WATCH",
            "risk_status": "LOW RISK",
            "risk_score": 100,
            "risk_reward": 3.0,
            "allocation": 20.0,
            "capital": 20_000_000,
            "entry_price": 1000,
            "quantity": 20_000,
            "order_value": 20_000_000,
            "validation_status": "READY",
            "market_regime": "BULL",
            "market_regime_score": 71.0
        },

        {
            "symbol": "TEST2",
            "base_score": 92.4,
            "regime_adjusted_score": 97.02,
            "candidate_score": 80.5,
            "signal": "BUY",
            "decision": "WATCH",
            "risk_status": "LOW RISK",
            "risk_score": 85.26,
            "risk_reward": 2.0,
            "allocation": 11.94,
            "capital": 11_940_000,
            "entry_price": 2000,
            "quantity": 5970,
            "order_value": 11_940_000,
            "validation_status": "READY",
            "market_regime": "BULL",
            "market_regime_score": 71.0
        },

        {
            "symbol": "TEST3",
            "base_score": 72.0,
            "regime_adjusted_score": 72.0,
            "candidate_score": 60.0,
            "signal": "WATCH",
            "decision": "WATCH",
            "risk_status": "HIGH RISK",
            "risk_score": 67.2,
            "risk_reward": 0.6,
            "allocation": 0.0,
            "capital": 0,
            "entry_price": 3000,
            "quantity": 0,
            "order_value": 0,
            "validation_status": "READY",
            "market_regime": "SIDEWAYS",
            "market_regime_score": 50.0
        }
    ]

    # -------------------------------------------------
    # Build trade plans
    # -------------------------------------------------

    plans = trade_engine.build(
        results
    )

    assert len(plans) == 3

    # -------------------------------------------------
    # Convert TradePlan -> Validation Order
    # -------------------------------------------------

    orders = []

    for plan in plans:

        order = {

            "symbol": plan.get(
                "symbol"
            ),

            "signal": plan.get(
                "signal"
            ),

            "price": plan.get(
                "entry_price"
            ),

            "capital": plan.get(
                "capital"
            ),

            "quantity": plan.get(
                "quantity"
            ),

            "order_value": plan.get(
                "order_value"
            ),

            "status": (
                "READY"
                if plan.get(
                    "final_status"
                ) == "READY"
                else "REJECTED"
            ),

            # Broker execution must
            # remain disabled.
            "broker_execution": False
        }

        orders.append(
            order
        )

    # -------------------------------------------------
    # Validate orders
    # -------------------------------------------------

    validated = (
        validation_engine.validate_orders(
            orders
        )
    )

    rejected = (
        validation_engine.get_rejected_orders()
    )

    # -------------------------------------------------
    # Assertions
    # -------------------------------------------------

    assert len(orders) == 3

    assert len(validated) == 2

    assert len(rejected) == 1

    assert validated[0][
        "validation_status"
    ] == "READY"

    assert validated[1][
        "validation_status"
    ] == "READY"

    assert rejected[0][
        "validation_status"
    ] == "REJECTED"

    assert rejected[0][
        "symbol"
    ] == "TEST3"

    # -------------------------------------------------
    # Safety assertions
    # -------------------------------------------------

    assert (
        validation_engine.statistics()[
            "broker_execution"
        ]
        is False
    )

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    print()

    print(
        "=" * 60
    )

    print(
        "TRADE PLAN + PRE-TRADE VALIDATION"
    )

    print(
        "=" * 60
    )

    for order in validated:

        print(
            order["symbol"],
            "| Status:",
            order["validation_status"],
            "| Value:",
            order["order_value"]
        )

    for order in rejected:

        print(
            order["symbol"],
            "| Status:",
            order["validation_status"],
            "| Errors:",
            order["validation_errors"]
        )

    print()

    print(
        "Valid:",
        len(validated)
    )

    print(
        "Rejected:",
        len(rejected)
    )

    print(
        "=" * 60
    )