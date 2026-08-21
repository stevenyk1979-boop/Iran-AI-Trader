"""
Iran AI Trader Professional

Scanner V2

Candidate Detection Engine Test
"""

from scanner_v2.candidate_detector import CandidateDetector


def test_candidate_detector():

    detector = CandidateDetector()

    results = [
        {
            "symbol": "TEST1",
            "score": 93.85,
            "regime_adjusted_score": 98.54,
            "trend_score": 100,
            "momentum_score": 100,
            "strength_score": 100,
            "market_regime": "BULL",
        },
        {
            "symbol": "TEST2",
            "score": 78.0,
            "regime_adjusted_score": 81.9,
            "trend_score": 85,
            "momentum_score": 80,
            "strength_score": 75,
            "market_regime": "BULL",
        },
        {
            "symbol": "TEST3",
            "score": 60.0,
            "regime_adjusted_score": 63.0,
            "trend_score": 60,
            "momentum_score": 55,
            "strength_score": 50,
            "market_regime": "SIDEWAYS",
        },
    ]

    detected = detector.detect(
        results
    )

    print()
    print("=" * 60)
    print("CANDIDATE DETECTOR TEST")
    print("=" * 60)

    for item in detected:

        print(
            item["candidate_rank"],
            item["symbol"],
            "| Score:",
            item["score"],
            "| Candidate:",
            item["candidate_score"],
            "| Status:",
            item["status"]
        )

    assert len(detected) == 3

    assert detected[0]["symbol"] == "TEST1"

    assert detected[0]["candidate_score"] == 100.0

    assert detected[0]["status"] == "READY"

    assert detected[1]["status"] == "READY"

    assert detected[2]["status"] == "IGNORE"

    assert detected[0]["candidate_rank"] == 1

    assert detected[1]["candidate_rank"] == 2

    assert detected[2]["candidate_rank"] == 3