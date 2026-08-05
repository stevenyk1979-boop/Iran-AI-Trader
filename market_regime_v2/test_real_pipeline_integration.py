"""
Iran AI Trader Professional

Real Pipeline Integration Test
Sprint41
"""


from market_regime_v2.real_pipeline_integration import (
    RealPipelineIntegration
)



print()

print("=" * 70)

print("REAL PIPELINE INTEGRATION TEST")

print("=" * 70)



integration = RealPipelineIntegration()



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

regime_result = integration.market_check(

    market_data

)



print()

print("=" * 70)

print("MARKET REGIME RESULT")

print("=" * 70)


print()

print("Success :", regime_result["success"])

print("Regime  :", regime_result["regime"])

print("Score   :", regime_result["score"])





# -------------------------------------
# Stock Check
# -------------------------------------

stock_result = integration.stock_check(

    regime_result,

    stock_score=90

)



print()

print("=" * 70)

print("STOCK DECISION RESULT")

print("=" * 70)


print()

print("Allowed :", stock_result["allowed"])

print("Mode    :", stock_result["mode"])

print("Action  :", stock_result["action"])

print("Reason  :", stock_result["reason"])





# -------------------------------------
# Status
# -------------------------------------

status = integration.pipeline_status()



print()

print("=" * 70)

print("PIPELINE STATUS")

print("=" * 70)


print()

print("Module :", status["module"])

print("Hook   :", status["regime_hook"]["module"])

print("Active :", status["regime_hook"]["active"])





print()

print("=" * 70)

print("INTEGRATION TEST FINISHED")

print("=" * 70)