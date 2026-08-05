"""
Iran AI Trader Professional
Pipeline Regime Config Test
Sprint37
"""


import pipeline_regime_config as config



print()

print("=" * 70)

print("PIPELINE REGIME CONFIG TEST")

print("=" * 70)



print()


print("Market Regime V2 Enabled :",

      config.ENABLE_MARKET_REGIME_V2)



print("Integration Mode        :",

      config.REGIME_MODE)



print("Fallback Enabled        :",

      config.ENABLE_FALLBACK)



print("Default Regime           :",

      config.DEFAULT_REGIME)



print()


print("Risk Control")

print("-" * 40)


print("Bull Trading Allowed    :",

      config.ALLOW_BULL_TRADING)



print("Sideways Trading       :",

      config.ALLOW_SIDEWAYS_TRADING)



print("Bear Trading           :",

      config.ALLOW_BEAR_TRADING)



print()


print("Score Thresholds")

print("-" * 40)


print("Minimum Buy Score       :",

      config.MIN_BUY_REGIME_SCORE)



print("Minimum Watch Score     :",

      config.MIN_WATCH_SCORE)



print()


print("=" * 70)

print("CONFIG TEST FINISHED")

print("=" * 70)