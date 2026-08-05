"""
Iran AI Trader Professional

Scanner Regime Bridge Test
Sprint39.5
"""


from market_regime_v2.scanner_regime_bridge import ScannerRegimeBridge



print()

print("=" * 70)

print("SCANNER REGIME BRIDGE TEST")

print("=" * 70)



engine = ScannerRegimeBridge()



# -------------------------------------
# BULL + Strong Stock
# -------------------------------------

result1 = engine.evaluate(

    regime="BULL",

    market_score=82,

    stock_score=90

)



print()

print("=" * 70)

print("BULL + STRONG STOCK")

print("=" * 70)


print()

print("Allowed :", result1["allowed"])

print("Mode    :", result1["mode"])

print("Action  :", result1["action"])

print("Reason  :", result1["reason"])





# -------------------------------------
# BULL + Medium Stock
# -------------------------------------

result2 = engine.evaluate(

    regime="BULL",

    market_score=82,

    stock_score=75

)



print()

print("=" * 70)

print("BULL + MEDIUM STOCK")

print("=" * 70)


print()

print("Allowed :", result2["allowed"])

print("Mode    :", result2["mode"])

print("Action  :", result2["action"])

print("Reason  :", result2["reason"])





# -------------------------------------
# BEAR Market
# -------------------------------------

result3 = engine.evaluate(

    regime="BEAR",

    market_score=55,

    stock_score=90

)



print()

print("=" * 70)

print("BEAR MARKET + STRONG STOCK")

print("=" * 70)


print()

print("Allowed :", result3["allowed"])

print("Mode    :", result3["mode"])

print("Action  :", result3["action"])

print("Reason  :", result3["reason"])





print()

print("=" * 70)

print("BRIDGE TEST FINISHED")

print("=" * 70)