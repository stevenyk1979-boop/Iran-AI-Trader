"""
Iran AI Trader Professional
Real Pipeline Regime Connection Test
Sprint37
"""


from pipeline_regime_bridge import PipelineRegimeBridge

import pipeline_regime_config as config



print()

print("=" * 70)

print("REAL PIPELINE REGIME CONNECTION TEST")

print("=" * 70)



# -------------------------------------
# Check Configuration
# -------------------------------------

print()

print("Configuration")

print("-" * 40)


print(

    "Market Regime V2 :",

    config.ENABLE_MARKET_REGIME_V2

)


print(

    "Mode             :",

    config.REGIME_MODE

)



# -------------------------------------
# Simulated Pipeline Data
# -------------------------------------

pipeline_market_data = {


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
# Bridge Execution
# -------------------------------------

bridge = PipelineRegimeBridge()



result = bridge.evaluate(

    pipeline_market_data

)



# -------------------------------------
# Output
# -------------------------------------

print()

print("=" * 70)

print("SHADOW REGIME RESULT")

print("=" * 70)



print()


print(

    "Market Regime :",

    result["regime"]["regime"]

)


print(

    "Score         :",

    result["regime"]["score"]

)



print()


print(

    "Trading Allowed:",

    result["permission"]["allowed"]

)


print(

    "Trading Mode   :",

    result["permission"]["mode"]

)



print()

print("=" * 70)

print("SHADOW CONNECTION TEST FINISHED")

print("=" * 70)