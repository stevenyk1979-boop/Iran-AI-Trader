"""
Iran AI Trader Professional
Portfolio Risk Configuration
Sprint33-D
"""


# -------------------------------------
# Drawdown Limits
# -------------------------------------


# افت بیشتر از این مقدار هشدار محسوب می‌شود

MAX_ACCEPTABLE_DRAWDOWN = 15



# افت شدید

CRITICAL_DRAWDOWN = 25



# -------------------------------------
# Risk Score Thresholds
# -------------------------------------


# امتیاز بالاتر = ریسک کمتر


LOW_RISK_SCORE = 70


MEDIUM_RISK_SCORE = 40



# -------------------------------------
# Portfolio Exposure
# -------------------------------------


# حداکثر وزن یک موقعیت در سبد

MAX_POSITION_EXPOSURE = 20



# -------------------------------------
# Market Protection
# -------------------------------------


# در بازار نزولی، سخت‌گیری بیشتر شود

BEAR_MARKET_RISK_FACTOR = 0.7