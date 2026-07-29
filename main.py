"""
Iran AI Trader V2.0 Beta
Main Application
"""

from pathlib import Path
from datetime import datetime

from config import PROJECT_NAME, VERSION

from database import DatabaseManager
from market import MarketManager

from portfolio import PortfolioManager
from position_manager import PositionManager

from scanner import Scanner
from scanner_report import ScannerReport

from csv_loader import CSVLoader

from technical_analysis import TechnicalAnalysis
from score_engine import ScoreEngine

from risk_manager import RiskManager

from download_manager import DownloadManager


# ----------------------------------------------------------
# Create folders
# ----------------------------------------------------------

def create_folders():

    folders = [

        "data",
        "logs",
        "docs",
        "tests"

    ]

    for folder in folders:

        Path(folder).mkdir(exist_ok=True)


# ----------------------------------------------------------
# Banner
# ----------------------------------------------------------

def banner():

    print("=" * 60)
    print(PROJECT_NAME)
    print(VERSION)
    print("=" * 60)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    banner()

    create_folders()

    # -------------------------
    # Database
    # -------------------------

    db = DatabaseManager()

    db.initialize()

    # -------------------------
    # Market
    # -------------------------

    market = MarketManager()

    market.status()

    market.update()

    # -------------------------
    # Portfolio
    # -------------------------

    portfolio = PortfolioManager()

    portfolio.list_assets()

    # -------------------------
    # Scanner
    # -------------------------

    scanner = Scanner()

    ranking = scanner.scan()

    report = ScannerReport()

    report.show(ranking)

    # -------------------------
    # Historical Data
    # -------------------------

    loader = CSVLoader()

    history = loader.load("historical_data.csv")

    prices = history.close_prices()

    print()

    print("=" * 40)

    print("Historical Data")

    print("=" * 40)

    print("Candles :", history.count())

    # -------------------------
    # Technical Analysis
    # -------------------------

    ta = TechnicalAnalysis()

    bands = ta.bollinger(prices)

    print()

    print("=" * 40)

    print("Technical Analysis")

    print("=" * 40)

    print("SMA(10)  :", ta.sma(prices, 10))
    print("EMA(10)  :", ta.ema(prices, 10))
    print("RSI(14)  :", ta.rsi(prices))
    print("MACD     :", ta.macd(prices))
    print("Bollinger:", bands)

    # -------------------------
    # Score Engine
    # -------------------------

    engine = ScoreEngine()

    score = engine.total_score(

        ta.rsi(prices),

        ta.macd(prices),

        bands,

        prices[-1]

    )

    print()

    print("=" * 40)

    print("Score Engine")

    print("=" * 40)

    print("Score :", score)
    print("Signal:", engine.recommendation(score))

    # -------------------------
    # Risk Manager
    # -------------------------

    risk = RiskManager()

    capital = 10_000_000

    entry = prices[-1]

    print()

    print("=" * 60)

    print("Risk Manager")

    print("=" * 60)

    print("Capital        :", capital)
    print("Position Size  :", risk.position_size(capital))
    print("Entry Price    :", entry)
    print("Stop Loss      :", risk.stop_loss_price(entry))
    print("Take Profit    :", risk.take_profit_price(entry))

    # -------------------------
    # Position Manager
    # -------------------------

    pm = PositionManager()

    pm.open_position(

        "وبملت",

        1000,

        entry

    )

    print()

    print("=" * 60)

    print("Position Manager")

    print("=" * 60)

    print("Open Positions :", pm.count())

    print(pm.list_positions())

    # -------------------------
    # Download Manager
    # -------------------------

    downloader = DownloadManager()

    downloader.connect()

    prices = downloader.download_history("وبملت")

    cached = downloader.get_cached_history("وبملت")

    print()

    print("=" * 60)

    print("Download Manager")

    print("=" * 60)

    print("Downloaded Candles :", len(prices))
    print("Cached Candles     :", len(cached))

    # -------------------------
    # Finish
    # -------------------------

    print()

    print("Project initialized successfully.")

    print("Ready for development...")


# ----------------------------------------------------------

if __name__ == "__main__":

    main()