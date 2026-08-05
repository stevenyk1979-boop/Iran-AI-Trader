"""
Iran AI Trader Professional

Adaptive Score Engine Test
Sprint38.5
"""


from market_regime_v2.adaptive_score_engine import AdaptiveScoreEngine


print()

print("=" * 70)

print("ADAPTIVE SCORE ENGINE TEST")

print("=" * 70)



engine = AdaptiveScoreEngine()



# -------------------------------------
# Bull Market Test
# -------------------------------------

bull_result = engine.calculate(

    regime="BULL",

    technical_score=80,

    momentum_score=75,

    liquidity_score=70,

    risk_score=60

)



print()

print("=" * 70)

print("BULL MARKET RESULT")

print("=" * 70)


print()

print("Regime :", bull_result["regime"])

print("Score  :", bull_result["score"])

print()

print("Weights")

print("----------------------------------------")


for key, value in bull_result["weights"].items():

    print(

        key,

        ":",

        value

    )



# -------------------------------------
# Bear Market Test
# -------------------------------------

bear_result = engine.calculate(

    regime="BEAR",

    technical_score=80,

    momentum_score=75,

    liquidity_score=70,

    risk_score=60

)



print()

print("=" * 70)

print("BEAR MARKET RESULT")

print("=" * 70)


print()

print("Regime :", bear_result["regime"])

print("Score  :", bear_result["score"])

print()

print("Weights")

print("----------------------------------------")


for key, value in bear_result["weights"].items():

    print(

        key,

        ":",

        value

    )



print()

print("=" * 70)

print("TEST FINISHED")

print("=" * 70)