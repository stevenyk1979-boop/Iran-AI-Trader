"""
Iran AI Trader Professional

Real Pipeline Runtime Hook Test
Sprint42
"""


from market_regime_v2.real_pipeline_runtime_hook import (
    RealPipelineRuntimeHook
)



print()

print("=" * 70)

print("REAL PIPELINE RUNTIME HOOK TEST")

print("=" * 70)



hook = RealPipelineRuntimeHook()



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
# Pre Scan Check
# -------------------------------------

market_result = hook.pre_scan_check(

    market_data

)



print()

print("=" * 70)

print("PRE SCAN RESULT")

print("=" * 70)


print()

print("Success :", market_result["success"])

print("Allowed :", market_result["allowed"])

print("Regime  :", market_result["regime"])

print("Score   :", market_result["score"])

print("Message :", market_result["message"])





# -------------------------------------
# Stock Decision
# -------------------------------------

stock_result = hook.stock_check(

    market_result,

    92

)



print()

print("=" * 70)

print("STOCK CHECK")

print("=" * 70)


print()

print("Allowed :", stock_result["allowed"])

print("Mode    :", stock_result["mode"])

print("Action  :", stock_result["action"])

print("Reason  :", stock_result["reason"])





# -------------------------------------
# Status
# -------------------------------------

status = hook.status()



print()

print("=" * 70)

print("RUNTIME STATUS")

print("=" * 70)


print()

print("Enabled :", status["enabled"])

print("Module  :", status["module"])





print()

print("=" * 70)

print("RUNTIME HOOK TEST FINISHED")

print("=" * 70)