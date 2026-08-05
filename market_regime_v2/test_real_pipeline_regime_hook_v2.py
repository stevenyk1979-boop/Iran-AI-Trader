"""
Iran AI Trader Professional

Real Pipeline Regime Hook V2 Test
Sprint40.5
"""


from market_regime_v2.real_pipeline_regime_hook_v2 import (
    RealPipelineRegimeHookV2
)



print()

print("=" * 70)

print("REAL PIPELINE REGIME HOOK V2 TEST")

print("=" * 70)



hook = RealPipelineRegimeHookV2()



# -------------------------------------
# Market Data
# -------------------------------------

market_data = {


    "price": 125,

    "ema20": 120,

    "ema50": 116,

    "ema100": 110,

    "ema50_prev": 114,


    "positive": 420,

    "negative": 180,

    "unchanged": 40,


    "volume": 28000000,

    "avg_volume": 18000000,


    "value": 520000000000,

    "avg_value": 350000000000,


    "money_flow": 82,


    "atr_percent": 2.3,

    "market_volatility": 1.4,

    "drawdown": 6,


    "index_change": 2.39,

    "equal_change": 1.85

}




# -------------------------------------
# Hook Analysis
# -------------------------------------

result = hook.analyze(

    market_data

)



print()

print("=" * 70)

print("HOOK MARKET RESULT")

print("=" * 70)


print()

print("Success :", result["success"])

print("Active  :", result["active"])

print("Regime  :", result["regime"])

print("Score   :", result["score"])





# -------------------------------------
# Stock Decision
# -------------------------------------

stock = hook.evaluate_stock(

    regime=result["regime"],

    market_score=result["score"],

    stock_score=90

)



print()

print("=" * 70)

print("STOCK DECISION")

print("=" * 70)


print()

print("Allowed :", stock["allowed"])

print("Mode    :", stock["mode"])

print("Action  :", stock["action"])

print("Reason  :", stock["reason"])





# -------------------------------------
# Status
# -------------------------------------

status = hook.status()



print()

print("=" * 70)

print("HOOK STATUS")

print("=" * 70)


print()

print("Active :", status["active"])

print("Module :", status["module"])





print()

print("=" * 70)

print("HOOK V2 TEST FINISHED")

print("=" * 70)