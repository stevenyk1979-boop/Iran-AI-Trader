"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Selection Engine Test
"""


from scanner_v2.strategy_selection_engine import (
    StrategySelectionEngine
)


def test_strategy_selection_engine():

    strategies = [

        {
            "symbol": "STRATEGY_A",
            "score": 85.0,
            "status": "STRONG",

            "performance": {
                "max_drawdown_percent": 5.0
            }
        },

        {
            "symbol": "STRATEGY_B",
            "score": 70.0,
            "status": "ACCEPTABLE",

            "performance": {
                "max_drawdown_percent": 15.0
            }
        },

        {
            "symbol": "STRATEGY_C",
            "score": 55.0,
            "status": "ACCEPTABLE",

            "performance": {
                "max_drawdown_percent": 8.0
            }
        },

        {
            "symbol": "STRATEGY_D",
            "score": 90.0,
            "status": "DANGEROUS",

            "performance": {
                "max_drawdown_percent": 10.0
            }
        },

        {
            "symbol": "STRATEGY_E",
            "score": 80.0,
            "status": "STRONG",

            "performance": {
                "max_drawdown_percent": 25.0
            }
        }

    ]

    engine = (
        StrategySelectionEngine(
            minimum_score=60.0,
            maximum_drawdown_percent=20.0
        )
    )

    selected = (
        engine.select(
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

    assert (
        engine.is_qualified(
            strategies[0]
        )
        is True
    )

    assert (
        engine.is_qualified(
            strategies[2]
        )
        is False
    )

    assert (
        engine.is_qualified(
            strategies[3]
        )
        is False
    )

    assert (
        engine.is_qualified(
            strategies[4]
        )
        is False
    )

    top = (
        engine.select_top(
            strategies,
            limit=1
        )
    )

    assert len(
        top
    ) == 1

    assert (
        top[0][
            "symbol"
        ]
        == "STRATEGY_A"
    )

    print()

    print("=" * 65)

    print(
        "STRATEGY SELECTION ENGINE"
    )

    print("=" * 65)

    for item in selected:

        print(

            "SELECTED:",
            item["symbol"],

            "| Score:",
            item["score"],

            "| Quality:",
            item["status"],

            "| Max DD:",
            item[
                "performance"
            ][
                "max_drawdown_percent"
            ],
            "%"

        )

    print()

    print(
        "Selected Strategies:",
        len(selected)
    )

    print(
        "Top Strategy:",
        top[0]["symbol"]
    )

    print("=" * 65)