"""
Iran AI Trader Professional

Scanner V2

Sprint48

Risk Adjusted Performance Engine Test
"""

from scanner_v2.risk_adjusted_performance_engine import (
    RiskAdjustedPerformanceEngine
)


def test_risk_adjusted_performance_engine():

    engine = (
        RiskAdjustedPerformanceEngine()
    )

    # -------------------------------------------------
    # TEST1 - STRONG
    # -------------------------------------------------

    test1 = engine.evaluate({

        "return_percent": 20.0,

        "win_rate_percent": 60.0,

        "profit_factor": 2.5,

        "max_drawdown_percent": 8.0,

        "recovery_percent": 100.0

    })

    assert (
        test1["status"]
        == "STRONG"
    )

    assert (
        test1["reason"]
        == "STRONG_RISK_ADJUSTED_PERFORMANCE"
    )

    # -------------------------------------------------
    # TEST2 - ACCEPTABLE
    # -------------------------------------------------

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

    # -------------------------------------------------
    # TEST3 - WEAK
    # -------------------------------------------------

    test3 = engine.evaluate({

        "return_percent": 4.0,

        "win_rate_percent": 35.0,

        "profit_factor": 0.9,

        "max_drawdown_percent": 12.0,

        "recovery_percent": 20.0

    })

    assert (
        test3["status"]
        == "WEAK"
    )

    # -------------------------------------------------
    # TEST4 - DANGEROUS
    # -------------------------------------------------

    test4 = engine.evaluate({

        "return_percent": 30.0,

        "win_rate_percent": 70.0,

        "profit_factor": 3.0,

        "max_drawdown_percent": 30.0,

        "recovery_percent": 100.0

    })

    assert (
        test4["status"]
        == "DANGEROUS"
    )

    assert (
        test4["reason"]
        == "MAX_DRAWDOWN_TOO_HIGH"
    )

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "RISK-ADJUSTED PERFORMANCE ENGINE"
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

            "| Return:",
            result[
                "return_percent"
            ],

            "%",

            "| PF:",
            result[
                "profit_factor"
            ],

            "| Max DD:",
            result[
                "max_drawdown_percent"
            ],

            "%",

            "| Recovery:",
            result[
                "recovery_percent"
            ],

            "%",

            "| Status:",
            result[
                "status"
            ]

        )

    print("=" * 60)