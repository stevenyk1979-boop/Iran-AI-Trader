from scanner_v2.regime_aware_decision import (
    RegimeAwareDecision
)


def test_regime_aware_decision():

    engine = RegimeAwareDecision()


    print()
    print("=" * 60)
    print("REGIME AWARE DECISION TEST")
    print("=" * 60)


    # ---------------------------------------------
    # Strong Bull
    # ---------------------------------------------

    result = engine.decide(
        85,
        "STRONG BULL"
    )

    print()
    print("STRONG BULL:")
    print(result)

    assert result["decision"] == "STRONG WATCH"


    # ---------------------------------------------
    # Sideways
    # ---------------------------------------------

    result = engine.decide(
        80,
        "SIDEWAYS"
    )

    print()
    print("SIDEWAYS:")
    print(result)

    assert result["decision"] == "WATCH"


    # ---------------------------------------------
    # Bear
    # ---------------------------------------------

    result = engine.decide(
        80,
        "BEAR"
    )

    print()
    print("BEAR:")
    print(result)

    assert result["decision"] == "WATCH"


    # ---------------------------------------------
    # Strong Bear
    # ---------------------------------------------

    result = engine.decide(
        80,
        "STRONG BEAR"
    )

    print()
    print("STRONG BEAR:")
    print(result)

    assert result["decision"] == "IGNORE"


    # ---------------------------------------------
    # Validation
    # ---------------------------------------------

    assert "decision" in result
    assert "regime" in result
    assert "score" in result