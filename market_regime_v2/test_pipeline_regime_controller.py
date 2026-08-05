"""
Iran AI Trader Professional
Pipeline Regime Controller Test
Sprint38
"""


from pipeline_regime_controller import PipelineRegimeController



print()

print("=" * 70)

print("PIPELINE REGIME CONTROLLER TEST")

print("=" * 70)



# -------------------------------------
# Sample Market Data
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
# Controller
# -------------------------------------

controller = PipelineRegimeController()



result = controller.evaluate(

    market_data

)



summary = controller.summary(

    result

)



# -------------------------------------
# Report
# -------------------------------------

print()

print("=" * 70)

print("CONTROLLER REPORT")

print("=" * 70)



print()


print(

    "Active :",

    result["active"]

)


print(

    "Mode   :",

    result["mode"]

)



print()


print(

    "Regime :",

    summary["regime"]

)


print(

    "Trade Allowed :",

    summary["trade_allowed"]

)



print()

print("=" * 70)

print("CONTROLLER TEST FINISHED")

print("=" * 70)