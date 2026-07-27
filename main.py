from pathlib import Path

from config import PROJECT_NAME, VERSION
from database import DatabaseManager
from market import MarketManager
from portfolio import PortfolioManager
from scanner import Scanner
from technical_analysis import TechnicalAnalysis


def create_folders():

    folders = [
        "data",
        "logs",
        "docs",
        "tests",
    ]

    for folder in folders:
        Path(folder).mkdir(exist_ok=True)


def banner():

    print("=" * 60)
    print(PROJECT_NAME)
    print(VERSION)
    print("=" * 60)


def main():

    banner()

    create_folders()

    db = DatabaseManager()
    db.initialize()

    market = MarketManager()
    market.status()
    market.update()

    portfolio = PortfolioManager()
    portfolio.list_assets()

    scanner = Scanner()
    scanner.scan()

    ta = TechnicalAnalysis()

    prices = ta.sample_data()

    print()
    print("=" * 40)
    print("Technical Analysis")
    print("=" * 40)

    print("SMA(10)  :", ta.sma(prices, 10))
    print("EMA(10)  :", ta.ema(prices, 10))
    print("RSI(14)  :", ta.rsi(prices))
    print("MACD     :", ta.macd(prices))
    bands = ta.bollinger(prices)
    print("Bollinger:", bands)
    print()
    print("Project initialized successfully.")
    print("Ready for development...")


if __name__ == "__main__":
    main()