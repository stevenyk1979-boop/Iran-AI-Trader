"""
Iran AI Trader Professional

Regime Score Integration Test
Sprint38.6

Test adaptive scoring behavior
"""


from market_regime_v2.adaptive_score_engine import AdaptiveScoreEngine


print()

print("=" * 70)

print("REGIME SCORE INTEGRATION TEST")

print("=" * 70)



engine = AdaptiveScoreEngine()



# ثابت‌های سهم

technical = 80

momentum = 75

liquidity = 70

risk = 60



# -------------------------------------
# BULL TEST
# -------------------------------------

bull = engine.calculate(

    regime="BULL",

    technical_score=technical,

    momentum_score=momentum,

    liquidity_score=liquidity,

    risk_score=risk

)



print()

print("=" * 70)

print("BULL MARKET")

print("=" * 70)


print()

print("Score :", bull["score"])


if bull["score"] >= 75:

    print("Decision : BUY READY")

else:

    print("Decision : WATCH")





# -------------------------------------
# SIDEWAYS TEST
# -------------------------------------

sideways = engine.calculate(

    regime="SIDEWAYS",

    technical_score=technical,

    momentum_score=momentum,

    liquidity_score=liquidity,

    risk_score=risk

)



print()

print("=" * 70)

print("SIDEWAYS MARKET")

print("=" * 70)


print()

print("Score :", sideways["score"])



if sideways["score"] >= 75:

    print("Decision : BUY READY")

else:

    print("Decision : WATCH")





# -------------------------------------
# BEAR TEST
# -------------------------------------

bear = engine.calculate(

    regime="BEAR",

    technical_score=technical,

    momentum_score=momentum,

    liquidity_score=liquidity,

    risk_score=risk

)



print()

print("=" * 70)

print("BEAR MARKET")

print("=" * 70)


print()

print("Score :", bear["score"])



if bear["score"] >= 75:

    print("Decision : BUY READY")

else:

    print("Decision : RISK BLOCK")





print()

print("=" * 70)

print("INTEGRATION TEST FINISHED")

print("=" * 70)