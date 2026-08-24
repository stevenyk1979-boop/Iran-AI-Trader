"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Ranking Engine Test
"""


from scanner_v2.strategy_ranking_engine import (
    StrategyRankingEngine
)


def test_strategy_ranking_engine():

    strategies = [

        {
            "symbol": "STRATEGY_A",
            "score": 82.0,
            "status": "STRONG"
        },

        {
            "symbol": "STRATEGY_B",
            "score": 74.0,
            "status": "STRONG"
        },

        {
            "symbol": "STRATEGY_C",
            "score": 61.0,
            "status": "ACCEPTABLE"
        },

        {
            "symbol": "STRATEGY_D",
            "score": 43.0,
            "status": "WEAK"
        }

    ]

    engine = (
        StrategyRankingEngine()
    )

    ranked = (
        engine.rank(
            strategies
        )
    )

    assert len(
        ranked
    ) == 4

    assert (
        ranked[0][
            "symbol"
        ]
        == "STRATEGY_A"
    )

    assert (
        ranked[0][
            "rank"
        ]
        == 1
    )

    assert (
        ranked[0][
            "score"
        ]
        == 82.0
    )

    assert (
        ranked[1][
            "symbol"
        ]
        == "STRATEGY_B"
    )

    assert (
        ranked[1][
            "rank"
        ]
        == 2
    )

    assert (
        ranked[2][
            "symbol"
        ]
        == "STRATEGY_C"
    )

    assert (
        ranked[2][
            "rank"
        ]
        == 3
    )

    assert (
        ranked[3][
            "symbol"
        ]
        == "STRATEGY_D"
    )

    assert (
        ranked[3][
            "rank"
        ]
        == 4
    )

    top_two = (
        engine.top(
            strategies,
            limit=2
        )
    )

    assert len(
        top_two
    ) == 2

    assert (
        top_two[0][
            "symbol"
        ]
        == "STRATEGY_A"
    )

    assert (
        top_two[1][
            "symbol"
        ]
        == "STRATEGY_B"
    )

    best = (
        engine.best(
            strategies
        )
    )

    assert (
        best["symbol"]
        == "STRATEGY_A"
    )

    print()

    print("=" * 60)

    print(
        "STRATEGY RANKING ENGINE"
    )

    print("=" * 60)

    for item in ranked:

        print(

            f'RANK {item["rank"]}',

            "| Strategy:",
            item["symbol"],

            "| Score:",
            item["score"],

            "| Status:",
            item["status"]

        )

    print()

    print(
        "TOP 2"
    )

    print(
        top_two[0]["symbol"],
        "->",
        top_two[0]["score"]
    )

    print(
        top_two[1]["symbol"],
        "->",
        top_two[1]["score"]
    )

    print()

    print(
        "BEST:",
        best["symbol"]
    )

    print("=" * 60)