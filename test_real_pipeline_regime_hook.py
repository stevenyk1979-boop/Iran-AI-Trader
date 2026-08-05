"""
Iran AI Trader Professional
Real Pipeline Regime Hook Test
Sprint38
"""


from real_pipeline_regime_hook import RealPipelineRegimeHook



print()

print("=" * 70)

print("REAL PIPELINE REGIME HOOK TEST")

print("=" * 70)



# -------------------------------------
# Simulated Real Pipeline Market Data
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
# Hook Execution
# -------------------------------------

hook = RealPipelineRegimeHook()



result = hook.analyze(

    market_data

)



summary = hook.summary(

    result

)



# -------------------------------------
# Report
# -------------------------------------

print()

print("=" * 70)

print("HOOK REPORT")

print("=" * 70)



print()


print("Active :", summary["active"])


print("Mode   :", summary["mode"])


print("Regime :", summary["regime"])


print("Score  :", summary["score"])


print("Trade Allowed :", summary["trade_allowed"])



print()

print("=" * 70)

print("HOOK TEST FINISHED")

print("=" * 70)