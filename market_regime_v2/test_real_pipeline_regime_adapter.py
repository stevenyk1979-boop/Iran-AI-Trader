"""
Iran AI Trader Professional

Real Pipeline Regime Adapter Test
Sprint40
"""


from market_regime_v2.real_pipeline_regime_adapter import (
    RealPipelineRegimeAdapter
)



print()

print("=" * 70)

print("REAL PIPELINE REGIME ADAPTER TEST")

print("=" * 70)



adapter = RealPipelineRegimeAdapter()



# -------------------------------------
# Market Analysis Test
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



market_result = adapter.analyze_market(

    market_data

)



print()

print("=" * 70)

print("MARKET ANALYSIS RESULT")

print("=" * 70)


print()

print("Regime :", market_result["regime"]["regime"])

print("Score  :", market_result["regime"]["score"])

print("Active :", market_result.get("active", True))



# -------------------------------------
# Stock Evaluation Test
# -------------------------------------

stock_result = adapter.evaluate_stock(

    regime="BULL",

    market_score=82.5,

    stock_score=90

)



print()

print("=" * 70)

print("STOCK EVALUATION RESULT")

print("=" * 70)


print()

print("Allowed :", stock_result["allowed"])

print("Mode    :", stock_result["mode"])

print("Action  :", stock_result["action"])

print("Reason  :", stock_result["reason"])





print()

print("=" * 70)

print("ADAPTER TEST FINISHED")

print("=" * 70)