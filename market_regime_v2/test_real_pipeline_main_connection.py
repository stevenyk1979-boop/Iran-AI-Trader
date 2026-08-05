"""
Iran AI Trader Professional

Real Pipeline Main Connection Test
Sprint43

Safe simulation before modifying real_pipeline.py
"""


from market_regime_v2.real_pipeline_runtime_bridge import (
    RealPipelineRuntimeBridge
)



print()

print("=" * 70)

print("REAL PIPELINE MAIN CONNECTION TEST")

print("=" * 70)



bridge = RealPipelineRuntimeBridge()



# -------------------------------------
# Simulated real_pipeline market input
# -------------------------------------

pipeline_market_input = {


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
# Pipeline startup check
# -------------------------------------

runtime_result = bridge.check_market(

    pipeline_market_input

)



print()

print("=" * 70)

print("PIPELINE STARTUP CHECK")

print("=" * 70)


print()

print("Success :", runtime_result["success"])

print("Allowed :", runtime_result["allowed"])

print("Mode    :", runtime_result["mode"])

print("Regime  :", runtime_result["regime"])

print("Score   :", runtime_result["score"])





# -------------------------------------
# Simulated Scanner candidates
# -------------------------------------

candidates = [

    {

        "symbol": "TEST_A",

        "score": 91

    },

    {

        "symbol": "TEST_B",

        "score": 73

    },

    {

        "symbol": "TEST_C",

        "score": 48

    }

]



print()

print("=" * 70)

print("PIPELINE CANDIDATE FILTER")

print("=" * 70)



if runtime_result["allowed"]:


    for item in candidates:


        decision = bridge.check_stock(

            runtime_result,

            item["score"]

        )


        print()

        print("Symbol :", item["symbol"])

        print("Score  :", item["score"])

        print("Action :", decision["action"])

        print("Mode   :", decision["mode"])



else:


    print()

    print("Pipeline blocked by market regime")





print()

print("=" * 70)

print("MAIN CONNECTION TEST FINISHED")

print("=" * 70)