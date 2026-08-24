"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Selection + Trade Pipeline
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


def test_strategy_selection_trade_pipeline_integration():

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
        },

        {
            "symbol": "STRATEGY_D",

            "score": 90.0,

            "status": "DANGEROUS",

            "performance": {
                "max_drawdown_percent": 10.0
            },

            "trade_plan": {
                "symbol": "TEST_D",
                "signal": "STRONG BUY",
                "price": 1000,
                "capital": 20_000_000,
                "allocation_percent": 20.0,
                "quantity": 20_000,
                "order_value": 20_000_000,
                "status": "READY",
                "broker_execution": False
            }
        }

    ]

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

    selected_trade_plans = [

        strategy[
            "trade_plan"
        ]

        for strategy in selected

        if "trade_plan"
        in strategy

    ]

    assert len(
        selected_trade_plans
    ) == 2

    validation_engine = (
        PreTradeValidationEngine()
    )

    validated = (
        validation_engine.validate_orders(
            selected_trade_plans
        )
    )

    assert len(
        validated
    ) == 2

    assert (
        validated[0][
            "symbol"
        ]
        == "TEST_A"
    )

    assert (
        validated[1][
            "symbol"
        ]
        == "TEST_B"
    )

    assert (
        validated[0][
            "validation_status"
        ]
        == "READY"
    )

    assert (
        validated[1][
            "validation_status"
        ]
        == "READY"
    )

    rejected_symbols = [

        strategy[
            "trade_plan"
        ][
            "symbol"
        ]

        for strategy in strategies

        if strategy
        not in selected
    ]

    assert (
        "TEST_C"
        in rejected_symbols
    )

    assert (
        "TEST_D"
        in rejected_symbols
    )

    print()

    print("=" * 70)

    print(
        "STRATEGY SELECTION + TRADE PIPELINE"
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

    for strategy in selected:

        trade_plan = (
            strategy[
                "trade_plan"
            ]
        )

        validation = next(

            item

            for item in validated

            if item[
                "symbol"
            ]
            == trade_plan[
                "symbol"
            ]

        )

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
            validation[
                "symbol"
            ],

            "| Validation:",
            validation[
                "validation_status"
            ]

        )

    print()

    print(
        "Rejected Strategies:",
        2
    )

    print(
        "Rejected Trades:",
        "TEST_C, TEST_D"
    )

    print()

    print(
        "Broker Execution:",
        False
    )

    print("=" * 70)