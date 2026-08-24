"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Quality Ranking Integration Test
"""


from scanner_v2.strategy_quality_ranking_engine import (
    StrategyQualityRankingEngine
)


def test_strategy_quality_ranking_engine():

    strategies = [

        {
            "symbol": "STRATEGY_A",
            "strategy_quality_score": 90.0,
            "strategy_quality_status": "EXCELLENT"
        },

        {
            "symbol": "STRATEGY_B",
            "strategy_quality_score": 74.0,
            "strategy_quality_status": "STRONG"
        },

        {
            "symbol": "STRATEGY_C",
            "strategy_quality_score": 61.0,
            "strategy_quality_status": "ACCEPTABLE"
        },

        {
            "symbol": "STRATEGY_D",
            "strategy_quality_score": 43.0,
            "strategy_quality_status": "WEAK"
        }

    ]

    engine = (
        StrategyQualityRankingEngine()
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
            "score"
        ]
        == 90.0
    )

    assert (
        ranked[0][
            "rank"
        ]
        == 1
    )

    assert (
        ranked[0][
            "status"
        ]
        == "EXCELLENT"
    )

    assert (
        ranked[1][
            "rank"
        ]
        == 2
    )

    assert (
        ranked[2][
            "rank"
        ]
        == 3
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
            2
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

    found = (
        engine.find_rank(
            strategies,
            "STRATEGY_C"
        )
    )

    assert (
        found["rank"]
        == 3
    )

    assert (
        found["score"]
        == 61.0
    )

    print()

    print("=" * 65)

    print(
        "STRATEGY QUALITY RANKING ENGINE"
    )

    print("=" * 65)

    for item in ranked:

        print(

            f'RANK {item["rank"]}',

            "| Strategy:",
            item["symbol"],

            "| Score:",
            item["score"],

            "| Quality:",
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

    print(
        "LOOKUP STRATEGY_C:", 
        found["rank"]
    )

    print("=" * 65)