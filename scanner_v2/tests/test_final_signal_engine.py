"""
Iran AI Trader Professional

Scanner V2

Sprint45-03

Final Signal Engine Test
"""

from scanner_v2.final_signal_engine import FinalSignalEngine


def test_final_signal_engine():

    engine = FinalSignalEngine()

    results = [

        {
            "symbol": "TEST1",
            "regime_adjusted_score": 98.54,
            "candidate_score": 100.0,
            "status": "READY",
            "market_regime": "BULL"
        },

        {
            "symbol": "TEST2",
            "regime_adjusted_score": 85.0,
            "candidate_score": 75.0,
            "status": "READY",
            "market_regime": "BULL"
        },

        {
            "symbol": "TEST3",
            "regime_adjusted_score": 72.0,
            "candidate_score": 60.0,
            "status": "EARLY",
            "market_regime": "SIDEWAYS"
        },

        {
            "symbol": "TEST4",
            "regime_adjusted_score": 55.0,
            "candidate_score": 45.0,
            "status": "IGNORE",
            "market_regime": "BEAR"
        }
    ]


    evaluated = engine.evaluate(
        results
    )


    print()
    print("=" * 60)
    print("FINAL SIGNAL ENGINE TEST")
    print("=" * 60)


    for item in evaluated:

        print(
            item["signal_rank"],
            item["symbol"],
            "| Score:",
            item["score"],
            "| Candidate:",
            item["candidate_score"],
            "| Regime:",
            item["regime"],
            "| Signal:",
            item["signal"]
        )


    # ---------------------------------------------
    # Validate number of results
    # ---------------------------------------------

    assert len(
        evaluated
    ) == 4


    # ---------------------------------------------
    # Validate signals
    # ---------------------------------------------

    signals = {
        item["symbol"]:
        item["signal"]
        for item in evaluated
    }


    assert (
        signals["TEST1"]
        == "STRONG BUY"
    )


    assert (
        signals["TEST2"]
        == "BUY"
    )


    assert (
        signals["TEST3"]
        == "WATCH"
    )


    assert (
        signals["TEST4"]
        == "IGNORE"
    )


    # ---------------------------------------------
    # Validate ranking
    # ---------------------------------------------

    assert (
        evaluated[0]["symbol"]
        == "TEST1"
    )

    assert (
        evaluated[1]["symbol"]
        == "TEST2"
    )

    assert (
        evaluated[2]["symbol"]
        == "TEST3"
    )

    assert (
        evaluated[3]["symbol"]
        == "TEST4"
    )


    # ---------------------------------------------
    # Validate statistics
    # ---------------------------------------------

    stats = engine.statistics()


    assert stats[
        "total"
    ] == 4

    assert stats[
        "strong_buy"
    ] == 1

    assert stats[
        "buy"
    ] == 1

    assert stats[
        "watch"
    ] == 1

    assert stats[
        "ignore"
    ] == 1