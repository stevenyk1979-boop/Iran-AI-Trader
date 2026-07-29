"""
Iran AI Trader Professional
Global Settings
"""

# -------------------------------------------------
# Project
# -------------------------------------------------

PROJECT_NAME = "Iran AI Trader Professional"

VERSION = "2.1 Beta"

# -------------------------------------------------
# Scanner
# -------------------------------------------------

MAX_SYMBOLS = 1000

TOP_RESULTS = 10

# -------------------------------------------------
# Technical Analysis
# -------------------------------------------------

SMA_PERIOD = 10

EMA_PERIOD = 10

RSI_PERIOD = 14

MACD_FAST = 12

MACD_SLOW = 26

MACD_SIGNAL = 9

BOLLINGER_PERIOD = 20

BOLLINGER_STD = 2

# -------------------------------------------------
# Risk Management
# -------------------------------------------------

DEFAULT_CAPITAL = 10_000_000

RISK_PER_TRADE = 0.02

STOP_LOSS_PERCENT = 0.03

TAKE_PROFIT_PERCENT = 0.08

# -------------------------------------------------
# Downloader
# -------------------------------------------------

DOWNLOAD_TIMEOUT = 10

DOWNLOAD_RETRY = 3

CACHE_ENABLED = True

# -------------------------------------------------
# Market
# -------------------------------------------------

DATA_SOURCE = "TSETMC"

DEFAULT_HISTORY_FILE = "historical_data.csv"

# -------------------------------------------------
# Logging
# -------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FILE = "logs/iran_ai_trader.log"