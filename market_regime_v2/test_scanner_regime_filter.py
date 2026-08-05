"""
Iran AI Trader Professional

Scanner Regime Filter Test
Sprint39
"""


from market_regime_v2.scanner_regime_filter import ScannerRegimeFilter


print()

print("=" * 70)

print("SCANNER REGIME FILTER TEST")

print("=" * 70)



engine = ScannerRegimeFilter()



# -------------------------------------
# BULL TEST
# -------------------------------------

bull = engine.check(

    regime="BULL",

    score=82

)



print()

print("=" * 70)

print("BULL MARKET")

print("=" * 70)


print()

print("Allowed :", bull["allowed"])

print("Mode    :", bull["mode"])

print("Reason  :", bull["reason"])




# -------------------------------------
# SIDEWAYS TEST
# -------------------------------------

sideways = engine.check(

    regime="SIDEWAYS",

    score=72

)



print()

print("=" * 70)

print("SIDEWAYS MARKET")

print("=" * 70)


print()

print("Allowed :", sideways["allowed"])

print("Mode    :", sideways["mode"])

print("Reason  :", sideways["reason"])




# -------------------------------------
# BEAR TEST
# -------------------------------------

bear = engine.check(

    regime="BEAR",

    score=82

)



print()

print("=" * 70)

print("BEAR MARKET")

print("=" * 70)


print()

print("Allowed :", bear["allowed"])

print("Mode    :", bear["mode"])

print("Reason  :", bear["reason"])




print()

print("=" * 70)

print("FILTER TEST FINISHED")

print("=" * 70)