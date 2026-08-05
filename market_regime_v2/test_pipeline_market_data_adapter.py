"""
Iran AI Trader Professional

Pipeline Market Data Adapter Test
Sprint44
"""


from market_regime_v2.pipeline_market_data_adapter import (
    PipelineMarketDataAdapter
)



print()

print("=" * 70)

print("PIPELINE MARKET DATA ADAPTER TEST")

print("=" * 70)



adapter = PipelineMarketDataAdapter()



# -------------------------------------
# Simulated Scanner Output
# -------------------------------------

ranking = [

    {
        "symbol": "TEST_A",
        "score": 92
    },

    {
        "symbol": "TEST_B",
        "score": 78
    },

    {
        "symbol": "TEST_C",
        "score": 45
    },

    {
        "symbol": "TEST_D",
        "score": 30
    }

]



# -------------------------------------
# Convert
# -------------------------------------

market_data = adapter.convert(

    ranking

)



print()

print("=" * 70)

print("ADAPTER OUTPUT")

print("=" * 70)



print()

print("Price :", market_data["price"])

print("EMA20 :", market_data["ema20"])

print("EMA50 :", market_data["ema50"])

print("EMA100:", market_data["ema100"])


print()

print("Positive :", market_data["positive"])

print("Negative :", market_data["negative"])

print("Unchanged:", market_data["unchanged"])


print()

print("Money Flow :", market_data["money_flow"])

print("Volatility :", market_data["market_volatility"])




# -------------------------------------
# Status
# -------------------------------------

status = adapter.status()



print()

print("=" * 70)

print("ADAPTER STATUS")

print("=" * 70)


print()

print("Module :", status["module"])

print("Active :", status["active"])




print()

print("=" * 70)

print("ADAPTER TEST FINISHED")

print("=" * 70)