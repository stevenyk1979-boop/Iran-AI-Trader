from pathlib import Path

from config import PROJECT_NAME, VERSION
from database import DatabaseManager
from market import MarketManager
from portfolio import PortfolioManager
from scanner import Scanner

from technical_analysis import TechnicalAnalysis
from score_engine import ScoreEngine

from csv_loader import CSVLoader


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

    loader = CSVLoader()

    history = loader.load("historical_data.csv")

    print()
    print("=" * 40)
    print("Historical Data")
    print("=" * 40)

    print("Candles :", history.count())

    prices = history.close_prices()

    ta = TechnicalAnalysis()

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

    engine = ScoreEngine()
    scanner = Scanner()
    scanner.scan()
    score = engine.total_score(
        ta.rsi(prices),
        ta.macd(prices),
        bands,
        prices[-1],
    )

    print()
    print("=" * 40)
    print("Score Engine")
    print("=" * 40)

    print("Score :", score)
    print("Signal:", engine.recommendation(score))

    print()
    print("Project initialized successfully.")
    print("Ready for development...")


if __name__ == "__main__":
    main()