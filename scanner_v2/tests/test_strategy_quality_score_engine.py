"""
Iran AI Trader Professional

Scanner V2

Sprint49

Strategy Quality Score Engine Test
"""

from scanner_v2.strategy_quality_score_engine import (
    StrategyQualityScoreEngine
)


def test_strategy_quality_score_engine():

    engine = (
        StrategyQualityScoreEngine()
    )

    test1 = engine.evaluate({

        "return_percent": 25.0,
        "win_rate_percent": 70.0,
        "profit_factor": 3.0,
        "max_drawdown_percent": 5.0,
        "recovery_percent": 100.0

    })

    assert (
        test1["status"]
        == "EXCELLENT"
    )

    assert (
        test1["score"]
        >= 85.0
    )

    test2 = engine.evaluate({

        "return_percent": 10.0,
        "win_rate_percent": 50.0,
        "profit_factor": 1.5,
        "max_drawdown_percent": 15.0,
        "recovery_percent": 50.0

    })

    assert (
        test2["status"]
        == "ACCEPTABLE"
    )

    assert (
        50.0
        <= test2["score"]
        < 70.0
    )

    test3 = engine.evaluate({

        "return_percent": 4.0,
        "win_rate_percent": 35.0,
        "profit_factor": 0.9,
        "max_drawdown_percent": 20.0,
        "recovery_percent": 20.0

    })

    assert (
        test3["status"]
        == "WEAK"
    )

    assert (
        30.0
        <= test3["score"]
        < 50.0
    )

    test4 = engine.evaluate({

        "return_percent": -5.0,
        "win_rate_percent": 25.0,
        "profit_factor": 0.5,
        "max_drawdown_percent": 40.0,
        "recovery_percent": 0.0

    })

    assert (
        test4["status"]
        == "DANGEROUS"
    )

    assert (
        test4["score"]
        < 30.0
    )

    print()

    print("=" * 60)

    print(
        "STRATEGY QUALITY SCORE ENGINE"
    )

    print("=" * 60)

    for index, result in enumerate(

        [
            test1,
            test2,
            test3,
            test4
        ],

        start=1

    ):

        print(

            f"TEST{index}",

            "| Score:",
            result["score"],

            "| Return:",
            result["return_percent"],

            "%",

            "| Win Rate:",
            result["win_rate_percent"],

            "%",

            "| PF:",
            result["profit_factor"],

            "| Max DD:",
            result["max_drawdown_percent"],

            "%",

            "| Recovery:",
            result["recovery_percent"],

            "%",

            "| Status:",
            result["status"]

        )

    print("=" * 60)