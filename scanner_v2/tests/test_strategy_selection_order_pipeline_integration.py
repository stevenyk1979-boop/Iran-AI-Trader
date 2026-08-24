"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Selection + Validation + Order Planning
Integration Test

Pipeline:

Strategy Quality
        ↓
Strategy Ranking
        ↓
Strategy Selection
        ↓
Trade Plan
        ↓
Pre-Trade Validation
        ↓
Order Planning

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


def test_strategy_selection_order_pipeline_integration():

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

            "score": 55.0,

            "status": "ACCEPTABLE",

            "performance": {
                "max_drawdown_percent": 8.0
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

    assert len(
        selected
    ) == 2

    assert (
        selected[0][
            "symbol"
        ]
        == "STRATEGY_A"
    )

    assert (
        selected[1][
            "symbol"
        ]
        == "STRATEGY_B"
    )

    # =================================================
    # STEP 2 — TRADE PLANS
    # =================================================

    trade_plans = [

        strategy[
            "trade_plan"
        ]

        for strategy in selected

    ]

    assert len(
        trade_plans
    ) == 2

    # =================================================
    # STEP 3 — PRE-TRADE VALIDATION
    # =================================================

    validation_engine = (
        PreTradeValidationEngine()
    )

    validated = (
        validation_engine.validate_orders(
            trade_plans
        )
    )

    assert len(
        validated
    ) == 2

    assert all(

        item[
            "validation_status"
        ]
        == "READY"

        for item in validated

    )

    # =================================================
    # STEP 4 — ORDER PLANNING
    # =================================================

    order_engine = (
        OrderPlanningEngine(
            lot_size=1
        )
    )

    portfolio_input = [

        {

            "symbol":
                item[
                    "symbol"
                ],

            "signal":
                item[
                    "signal"
                ],

            "capital":
                item[
                    "capital"
                ],

            "price":
                item[
                    "price"
                ],

            "allocation_percent":
                item[
                    "allocation_percent"
                ]

        }

        for item in validated

    ]

    orders = (
        order_engine.build_orders(
            portfolio_input
        )
    )

    assert len(
        orders
    ) == 2

    assert (
        orders[0][
            "symbol"
        ]
        == "TEST_A"
    )

    assert (
        orders[1][
            "symbol"
        ]
        == "TEST_B"
    )

    assert (
        orders[0][
            "status"
        ]
        == "READY"
    )

    assert (
        orders[1][
            "status"
        ]
        == "READY"
    )

    assert (
        orders[0][
            "broker_execution"
        ]
        is False
    )

    assert (
        orders[1][
            "broker_execution"
        ]
        is False
    )

    print()

    print("=" * 70)

    print(
        "STRATEGY SELECTION + ORDER PIPELINE"
    )

    print("=" * 70)

    print(
        "Total Strategies:",
        len(strategies)
    )

    print(
        "Selected Strategies:",
        len(selected)
    )

    print()

    for strategy, order in zip(
        selected,
        orders
    ):

        print(

            "Strategy:",
            strategy[
                "symbol"
            ],

            "| Score:",
            strategy[
                "score"
            ],

            "| Quality:",
            strategy[
                "status"
            ],

            "| Trade:",
            order[
                "symbol"
            ],

            "| Order:",
            order[
                "status"
            ],

            "| Quantity:",
            order[
                "quantity"
            ],

            "| Value:",
            order[
                "order_value"
            ]

        )

    print()

    print(
        "Rejected Strategy:",
        "STRATEGY_C"
    )

    print(
        "Rejected Trade:",
        "TEST_C"
    )

    print()

    print(
        "Broker Execution:",
        False
    )

    print("=" * 70)