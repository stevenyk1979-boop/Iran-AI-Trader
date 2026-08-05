"""
Iran AI Trader Professional
Pipeline Regime Configuration
Sprint37
"""


# -------------------------------------
# Enable / Disable Market Regime V2
# -------------------------------------

ENABLE_MARKET_REGIME_V2 = True



# -------------------------------------
# Integration Mode
# -------------------------------------

# TEST:
# فقط بررسی و گزارش

# SHADOW:
# اجرای V2 در کنار Pipeline قدیمی بدون تاثیر روی تصمیم

# PRODUCTION:
# استفاده واقعی از خروجی V2

REGIME_MODE = "SHADOW"



# -------------------------------------
# Fallback Settings
# -------------------------------------

ENABLE_FALLBACK = True


DEFAULT_REGIME = "UNKNOWN"



# -------------------------------------
# Risk Control
# -------------------------------------

ALLOW_BULL_TRADING = True

ALLOW_SIDEWAYS_TRADING = False

ALLOW_BEAR_TRADING = False



# -------------------------------------
# Logging
# -------------------------------------

ENABLE_REGIME_LOG = True


LOG_COMPARISON = True



# -------------------------------------
# Score Thresholds
# -------------------------------------

MIN_BUY_REGIME_SCORE = 75


MIN_WATCH_SCORE = 60