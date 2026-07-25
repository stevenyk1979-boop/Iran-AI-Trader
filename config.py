"""
Iran AI Trader V2.0
Global Configuration
"""

from pathlib import Path


# ---------------------------------------------------
# Project Information
# ---------------------------------------------------

PROJECT_NAME = "Iran AI Trader"
VERSION = "2.0 Alpha"

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
DOC_DIR = BASE_DIR / "docs"
TEST_DIR = BASE_DIR / "tests"

# ---------------------------------------------------
# Database
# ---------------------------------------------------

DATABASE_NAME = "iran_ai_trader.db"

DATABASE_PATH = DATA_DIR / DATABASE_NAME

# ---------------------------------------------------
# Market Settings
# ---------------------------------------------------

MARKET_NAME = "Iran Stock Market"

DEFAULT_TIMEFRAME = "Daily"

# ---------------------------------------------------
# Create Required Folders
# ---------------------------------------------------

for folder in [
    DATA_DIR,
    LOG_DIR,
    DOC_DIR,
    TEST_DIR,
]:
    folder.mkdir(exist_ok=True)