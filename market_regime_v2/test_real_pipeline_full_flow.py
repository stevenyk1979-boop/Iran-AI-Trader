"""
Iran AI Trader Professional

Real Pipeline Full Flow Test
Sprint41.5
"""


from market_regime_v2.real_pipeline_integration import (
    RealPipelineIntegration
)



print()

print("=" * 70)

print("REAL PIPELINE FULL FLOW TEST")

print("=" * 70)



pipeline = RealPipelineIntegration()



# -------------------------------------
# Simulated Market Data
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
# Market Regime
# -------------------------------------

regime = pipeline.market_check(

    market_data

)



print()

print("=" * 70)

print("MARKET STATE")

print("=" * 70)


print()

print("Regime :", regime["regime"])

print("Score  :", regime["score"])

print("Status :", regime["success"])





# -------------------------------------
# Candidate Stocks
# -------------------------------------

stocks = [


    {

        "symbol": "TEST_A",

        "score": 92

    },


    {

        "symbol": "TEST_B",

        "score": 76

    },


    {

        "symbol": "TEST_C",

        "score": 55

    }

]




print()

print("=" * 70)

print("SCANNER DECISIONS")

print("=" * 70)



for stock in stocks:


    decision = pipeline.stock_check(

        regime,

        stock["score"]

    )


    print()

    print(

        stock["symbol"]

    )


    print(

        "Score :", 

        stock["score"]

    )


    print(

        "Allowed :", 

        decision["allowed"]

    )


    print(

        "Action  :", 

        decision["action"]

    )





print()

print("=" * 70)

print("FULL FLOW TEST FINISHED")

print("=" * 70)