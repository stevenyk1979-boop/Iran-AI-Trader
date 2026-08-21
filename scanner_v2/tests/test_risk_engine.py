"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Risk Engine Test
"""

from scanner_v2.risk_engine import RiskEngine


def test_risk_engine():

    engine = RiskEngine()

    results = [

        {
            "symbol": "TEST1",
            "score": 98.54,
            "candidate_score": 100.0,
            "regime": "BULL",
            "entry_price": 100,
            "stop_loss": 95,
            "take_profit": 115
        },

        {
            "symbol": "TEST2",
            "score": 85.0,
            "candidate_score": 75.0,
            "regime": "BULL",
            "entry_price": 100,
            "stop_loss": 95,
            "take_profit": 110
        },

        {
            "symbol": "TEST3",
            "score": 72.0,
            "candidate_score": 60.0,
            "regime": "SIDEWAYS",
            "entry_price": 100,
            "stop_loss": 95,
            "take_profit": 103
        },

        {
            "symbol": "TEST4",
            "score": 55.0,
            "candidate_score": 45.0,
            "regime": "BEAR",
            "entry_price": 100,
            "stop_loss": 98,
            "take_profit": 101
        }
    ]


    evaluated = engine.evaluate_all(
        results
    )


    print()
    print("=" * 60)
    print("RISK ENGINE TEST")
    print("=" * 60)


    for item in evaluated:

        print(
            item["risk_rank"],
            item["symbol"],
            "| Risk Score:",
            item["risk_score"],
            "| R/R:",
            item["risk_reward"],
            "| Status:",
            item["risk_status"]
        )


    # ---------------------------------------------
    # Basic validation
    # ---------------------------------------------

    assert len(
        evaluated
    ) == 4


    # ---------------------------------------------
    # Risk/Reward validation
    # ---------------------------------------------

    assert (
        evaluated[0]["risk_reward"]
        >=
        evaluated[-1]["risk_reward"]
    )


    # TEST1:
    # risk = 5
    # reward = 15
    # R/R = 3

    test1 = next(
        item
        for item in evaluated
        if item["symbol"] == "TEST1"
    )

    assert (
        test1["risk_reward"]
        == 3.0
    )


    # TEST2:
    # risk = 5
    # reward = 10
    # R/R = 2

    test2 = next(
        item
        for item in evaluated
        if item["symbol"] == "TEST2"
    )

    assert (
        test2["risk_reward"]
        == 2.0
    )


    # TEST3:
    # risk = 5
    # reward = 3
    # R/R = 0.6

    test3 = next(
        item
        for item in evaluated
        if item["symbol"] == "TEST3"
    )

    assert (
        test3["risk_reward"]
        == 0.6
    )


    # ---------------------------------------------
    # Risk status validation
    # ---------------------------------------------

    assert (
        test1["risk_status"]
        == "LOW RISK"
    )

    assert (
        test2["risk_status"]
        == "LOW RISK"
    )

    assert (
        test3["risk_status"]
        == "HIGH RISK"
    )


    # ---------------------------------------------
    # Statistics
    # ---------------------------------------------

    stats = engine.statistics()

    assert (
        stats["total"]
        == 4
    )

    assert (
        stats["low_risk"]
        == 2
    )

    assert (
        stats["high_risk"]
        >= 1
    )