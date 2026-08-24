"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Selection + Execution Pipeline
Integration Test

Pipeline:

Strategy Quality
        ↓
Strategy Selection
        ↓
Trade Plan
        ↓
Pre-Trade Validation
        ↓
Order Planning
        ↓
Execution Readiness
        ↓
Execution Control

IMPORTANT:
No broker connection.
No real order execution.
"""


from scanner_v2.strategy_selection_engine import (
    StrategySelectionEngine
)

from scanner_v2.pre_trade_validation_engine import (
    PreTradeValidationEngine
)

from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)

from scanner_v2.execution_readiness_engine import (
    ExecutionReadinessEngine
)

from scanner_v2.execution_control_engine import (
    ExecutionControlEngine
)


def test_strategy_selection_execution_pipeline_integration():

    strategies = [

        {
            "symbol": "STRATEGY_A",
            "score": 85.0,
            "status": "STRONG",

            "performance": {
                "max_drawdown_percent": 5.0
            },

            "trade_plan": {
                "symbol": "TEST_A",
                "signal": "STRONG BUY",
                "price": 1000,
                "capital": 20_000_000,
                "allocation_percent": 20.0,
                "quantity": 20_000,
                "order_value": 20_000_000,
                "status": "READY",
                "broker_execution": False
            }
        },

        {
            "symbol": "STRATEGY_B",
            "score": 70.0,
            "status": "ACCEPTABLE",

            "performance": {
                "max_drawdown_percent": 15.0
            },

            "trade_plan": {
                "symbol": "TEST_B",
                "signal": "BUY",
                "price": 2000,
                "capital": 15_000_000,
                "allocation_percent": 15.0,
                "quantity": 7_500,
                "order_value": 15_000_000,
                "status": "READY",
                "broker_execution": False
            }
        },

        {
            "symbol": "STRATEGY_C",
            "score": 50.0,
            "status": "WEAK",

            "performance": {
                "max_drawdown_percent": 30.0
            },

            "trade_plan": {
                "symbol": "TEST_C",
                "signal": "BUY",
                "price": 1500,
                "capital": 10_000_000,
                "allocation_percent": 10.0,
                "quantity": 6_666,
                "order_value": 9_999_000,
                "status": "READY",
                "broker_execution": False
            }
        }

    ]

    # =================================================
    # STEP 1 — STRATEGY SELECTION
    # =================================================

    selection_engine = (
        StrategySelectionEngine(
            minimum_score=60.0,
            maximum_drawdown_percent=20.0
        )
    )

    selected = (
        selection_engine.select(
            strategies
        )
    )

    assert len(selected) == 2

    assert (
        selected[0]["symbol"]
        == "STRATEGY_A"
    )

    assert (
        selected[1]["symbol"]
        == "STRATEGY_B"
    )

    # =================================================
    # STEP 2 — PRE-TRADE VALIDATION
    # =================================================

    trade_plans = [

        strategy["trade_plan"]

        for strategy in selected
    ]

    validation_engine = (
        PreTradeValidationEngine()
    )

    validated = (
        validation_engine.validate_orders(
            trade_plans
        )
    )

    assert len(validated) == 2

    assert all(
        item["validation_status"] == "READY"
        for item in validated
    )

    # =================================================
    # STEP 3 — ORDER PLANNING
    # =================================================

    order_engine = (
        OrderPlanningEngine(
            lot_size=1
        )
    )

    portfolio_input = [

        {
            "symbol": item["symbol"],
            "signal": item["signal"],
            "capital": item["capital"],
            "price": item["price"],
            "allocation_percent":
                item["allocation_percent"]
        }

        for item in validated
    ]

    orders = (
        order_engine.build_orders(
            portfolio_input
        )
    )

    assert len(orders) == 2

    assert (
        orders[0]["symbol"]
        == "TEST_A"
    )

    assert (
        orders[1]["symbol"]
        == "TEST_B"
    )

    assert (
        orders[0]["status"]
        == "READY"
    )

    assert (
        orders[1]["status"]
        == "READY"
    )

    # =================================================
    # STEP 3.5 — TRANSFER VALIDATION RESULT
    # =================================================

    for order, validation in zip(
        orders,
        validated
    ):

        order[
            "validation_status"
        ] = validation[
            "validation_status"
        ]

        order[
            "validation_reason"
        ] = validation.get(
            "validation_reason",
            "ALL_VALIDATION_CHECKS_PASSED"
        )

    # =================================================
    # STEP 4 — EXECUTION READINESS
    # =================================================

    readiness_engine = (
        ExecutionReadinessEngine()
    )

    readiness_results = []

    for order in orders:

        readiness = (
            readiness_engine.evaluate(
                order
            )
        )

        readiness_results.append(
            readiness
        )

    assert len(
        readiness_results
    ) == 2

    for readiness in readiness_results:

        assert readiness[
            "execution_status"
        ] in (
            "READY",
            "READY_WITH_WARNING"
        )

        assert readiness[
            "ready"
        ] is True

    # =================================================
    # STEP 4.5 — TRANSFER READINESS RESULT
    # =================================================

    for order, readiness in zip(
        orders,
        readiness_results
    ):

        order[
            "execution_status"
        ] = readiness[
            "execution_status"
        ]

        order[
            "execution_reason"
        ] = readiness[
            "execution_reason"
        ]

        order[
            "execution_ready"
        ] = readiness[
            "ready"
        ]

        order[
            "execution_errors"
        ] = readiness.get(
            "errors",
            []
        )

    # =================================================
    # STEP 5 — EXECUTION CONTROL
    # =================================================

    control_engine = (
        ExecutionControlEngine()
    )

    control_results = (
        control_engine.control_orders(
            orders
        )
    )

    assert len(
        control_results
    ) == 2

    # =================================================
    # CONTROL VALIDATION
    # =================================================

    for control in control_results:

        assert control[
            "execution_control"
        ] in (
            "APPROVED",
            "APPROVED_WITH_WARNING"
        )

        assert control[
            "approved"
        ] is True

    # =================================================
    # REPORT
    # =================================================

    print()

    print(
        "=" * 75
    )

    print(
        "STRATEGY SELECTION + EXECUTION PIPELINE"
    )

    print(
        "=" * 75
    )

    print(
        "Total Strategies:",
        len(strategies)
    )

    print(
        "Selected Strategies:",
        len(selected)
    )

    print()

    for strategy, order, readiness, control in zip(
        selected,
        orders,
        readiness_results,
        control_results
    ):

        print(
            "Strategy:",
            strategy["symbol"],

            "| Score:",
            strategy["score"],

            "| Quality:",
            strategy["status"],

            "| Trade:",
            order["symbol"],

            "| Validation:",
            order[
                "validation_status"
            ],

            "| Order:",
            order["status"],

            "| Readiness:",
            readiness[
                "execution_status"
            ],

            "| Control:",
            control[
                "execution_control"
            ]
        )

    print()

    print(
        "Rejected Strategy:",
        "STRATEGY_C"
    )

    print(
        "Broker Execution:",
        False
    )

    print(
        "=" * 75
    )