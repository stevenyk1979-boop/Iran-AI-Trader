"""
Iran AI Trader Professional

Real Pipeline Runtime Bridge Test
Sprint42.5
"""


from market_regime_v2.real_pipeline_runtime_bridge import (
    RealPipelineRuntimeBridge
)



print()

print("=" * 70)

print("REAL PIPELINE RUNTIME BRIDGE TEST")

print("=" * 70)



bridge = RealPipelineRuntimeBridge()



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
# Market Check
# -------------------------------------

market_result = bridge.check_market(

    market_data

)



print()

print("=" * 70)

print("BRIDGE MARKET RESULT")

print("=" * 70)


print()

print("Success :", market_result["success"])

print("Allowed :", market_result["allowed"])

print("Mode    :", market_result["mode"])

print("Regime  :", market_result["regime"])

print("Score   :", market_result["score"])

print("Message :", market_result["message"])





# -------------------------------------
# Stock Check
# -------------------------------------

stock_result = bridge.check_stock(

    market_result,

    92

)



print()

print("=" * 70)

print("BRIDGE STOCK RESULT")

print("=" * 70)


print()

print("Allowed :", stock_result["allowed"])

print("Mode    :", stock_result["mode"])

print("Action  :", stock_result["action"])

print("Reason  :", stock_result["reason"])





# -------------------------------------
# Status
# -------------------------------------

status = bridge.status()



print()

print("=" * 70)

print("BRIDGE STATUS")

print("=" * 70)


print()

print("Module :", status["module"])

print("Mode   :", status["mode"])

print("Hook   :", status["hook"]["module"])

print("Active :", status["hook"]["enabled"])





print()

print("=" * 70)

print("RUNTIME BRIDGE TEST FINISHED")

print("=" * 70)