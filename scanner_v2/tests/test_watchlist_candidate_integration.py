"""
Iran AI Trader Professional

Scanner V2

Sprint45-02

Watchlist + Candidate Integration Test
"""

from scanner_v2.watchlist_engine import WatchlistEngine


def test_watchlist_candidate_integration():

    candidates = [
        {
            "symbol": "TEST1",
            "score": 98.54,
            "regime": "BULL",
            "trend_component": 100,
            "candidate_score": 100.0,
            "candidate_status": "READY",
        },
        {
            "symbol": "TEST2",
            "score": 97.02,
            "regime": "BULL",
            "trend_component": 100,
            "candidate_score": 80.5,
            "candidate_status": "READY",
        },
        {
            "symbol": "TEST3",
            "score": 95.01,
            "regime": "BULL",
            "trend_component": 98.46,
            "candidate_score": 55.5,
            "candidate_status": "READY",
        },
        {
            "symbol": "TEST4",
            "score": 92.78,
            "regime": "BULL",
            "trend_component": 96.2,
            "candidate_score": 52.0,
            "candidate_status": "READY",
        },
        {
            "symbol": "TEST5",
            "score": 90.52,
            "regime": "BULL",
            "trend_component": 93.88,
            "candidate_score": 48.5,
            "candidate_status": "READY",
        },
        {
            "symbol": "TEST6",
            "score": 73.50,
            "regime": "BULL",
            "trend_component": 70.0,
            "candidate_score": 40.0,
            "candidate_status": "READY",
        },
    ]

    assert len(candidates) == 6

    # Explicitly request Top 5.
    watchlist_engine = WatchlistEngine(
        top_n=5
    )

    ranked = watchlist_engine.build(
        candidates
    )

    print()
    print("=" * 60)
    print("WATCHLIST + CANDIDATE INTEGRATION TEST")
    print("=" * 60)

    print()
    print("Candidates:", len(candidates))
    print("Watchlist:", len(ranked))

    print()
    print("TOP 5 WATCHLIST")
    print("-" * 60)

    for item in ranked:

        print(
            item.get(
                "watchlist_rank"
            ),
            item.get(
                "symbol"
            ),
            "| Score:",
            item.get(
                "final_watchlist_score"
            ),
            "| Candidate:",
            item.get(
                "candidate_score"
            ),
            "| Status:",
            item.get(
                "candidate_status"
            )
        )

    # ---------------------------------------------
    # Validation
    # ---------------------------------------------

    assert len(ranked) <= 5

    assert len(ranked) == 5

    # Highest score must be first.
    assert (
        ranked[0]["symbol"]
        == "TEST1"
    )

    assert (
        ranked[1]["symbol"]
        == "TEST2"
    )

    assert (
        ranked[2]["symbol"]
        == "TEST3"
    )

    assert (
        ranked[3]["symbol"]
        == "TEST4"
    )

    assert (
        ranked[4]["symbol"]
        == "TEST5"
    )

    # TEST6 must not enter Top 5.
    assert all(
        item.get("symbol")
        != "TEST6"
        for item in ranked
    )

    # Watchlist ranks must be consecutive.
    assert [
        item.get(
            "watchlist_rank"
        )
        for item in ranked
    ] == [1, 2, 3, 4, 5]