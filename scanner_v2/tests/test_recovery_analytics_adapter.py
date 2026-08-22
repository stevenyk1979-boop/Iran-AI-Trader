"""
Iran AI Trader Professional

Scanner V2

Sprint51

Recovery Analytics Adapter Test
"""


from scanner_v2.recovery_analytics_adapter import (
    RecoveryAnalyticsAdapter
)


def test_recovery_analytics_adapter():

    adapter = (
        RecoveryAnalyticsAdapter()
    )

    test1 = adapter.calculate({

        "equity": 115000000.0,

        "peak_equity": 115000000.0,

        "max_drawdown": 12000000.0,

        "drawdown": 0.0

    })

    assert (
        test1["recovery_percent"]
        == 100.0
    )

    assert (
        test1["recovery_status"]
        == "FULLY RECOVERED"
    )

    test2 = adapter.calculate({

        "equity": 103000000.0,

        "peak_equity": 115000000.0,

        "max_drawdown": 12000000.0,

        "drawdown": 12000000.0

    })

    assert (
        test2["recovery_percent"]
        == 0.0
    )

    assert (
        test2["recovery_status"]
        == "DRAWDOWN"
    )

    test3 = adapter.calculate({

        "equity": 108000000.0,

        "peak_equity": 115000000.0,

        "max_drawdown": 12000000.0,

        "drawdown": 7000000.0

    })

    assert (
        test3["recovery_percent"]
        == 41.67
    )

    assert (
        test3["recovery_status"]
        == "RECOVERING"
    )

    print()

    print("=" * 60)

    print(
        "RECOVERY ANALYTICS ADAPTER"
    )

    print("=" * 60)

    for index, result in enumerate(

        [
            test1,
            test2,
            test3
        ],

        start=1

    ):

        print(

            f"TEST{index}",

            "| Equity:",
            result["equity"],

            "| Peak:",
            result["peak_equity"],

            "| Max DD:",
            result["max_drawdown"],

            "| Current DD:",
            result["current_drawdown"],

            "| Recovery:",
            result["recovery_percent"],

            "%",

            "| Status:",
            result["recovery_status"]

        )

    print("=" * 60)