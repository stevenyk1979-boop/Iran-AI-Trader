
from scanner_v2.ranking_breakdown import RankingBreakdown


print("============================================================")
print("RANKING BREAKDOWN VALIDATION TEST")
print("============================================================")


# ------------------------------------------------------------
# 1. NORMAL
# ------------------------------------------------------------

try:

    breakdown = RankingBreakdown()

    breakdown.add(
        "price",
        69.0,
        0.6
    )

    breakdown.add(
        "trend",
        97.4,
        0.4
    )

    print(
        "NORMAL:",
        breakdown.to_dict()
    )

except Exception as error:

    print(
        "NORMAL ERROR:",
        error
    )


# ------------------------------------------------------------
# 2. NEGATIVE WEIGHT
# ------------------------------------------------------------

try:

    breakdown = RankingBreakdown()

    breakdown.add(
        "price",
        69.0,
        -0.1
    )

    print(
        "NEGATIVE WEIGHT: FAILED - ERROR NOT RAISED"
    )

except Exception as error:

    print(
        "NEGATIVE WEIGHT: PASS",
        error
    )


# ------------------------------------------------------------
# 3. ZERO TOTAL WEIGHT
# ------------------------------------------------------------

try:

    breakdown = RankingBreakdown()

    breakdown.add(
        "price",
        69.0,
        0
    )

    breakdown.add(
        "trend",
        97.4,
        0
    )

    breakdown.final_score()

    print(
        "ZERO TOTAL WEIGHT: FAILED - ERROR NOT RAISED"
    )

except Exception as error:

    print(
        "ZERO TOTAL WEIGHT: PASS",
        error
    )


# ------------------------------------------------------------
# 4. DUPLICATE COMPONENT
# ------------------------------------------------------------

try:

    breakdown = RankingBreakdown()

    breakdown.add(
        "price",
        69.0,
        0.6
    )

    breakdown.add(
        "price",
        80.0,
        0.4
    )

    print(
        "DUPLICATE COMPONENT:",
        breakdown.to_dict()
    )

except Exception as error:

    print(
        "DUPLICATE COMPONENT ERROR:",
        error
    )


# ------------------------------------------------------------
# 5. INVALID SCORE
# ------------------------------------------------------------

try:

    breakdown = RankingBreakdown()

    breakdown.add(
        "invalid",
        None,
        0.2
    )

    print(
        "INVALID SCORE: FAILED - ERROR NOT RAISED"
    )

except Exception as error:

    print(
        "INVALID SCORE: PASS",
        error
    )


print("============================================================")
print("VALIDATION FINISHED")
print("============================================================")

