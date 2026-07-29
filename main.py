"""
Iran AI Trader V2.0 Alpha
Main Application
"""

from pathlib import Path

from config import PROJECT_NAME, VERSION

from database import DatabaseManager
from market import MarketManager

from portfolio import PortfolioManager
from risk_manager import RiskManager
from position_manager import PositionManager

from scanner import Scanner
from scanner_report import ScannerReport

from technical_analysis import TechnicalAnalysis
from score_engine import ScoreEngine

from csv_loader import CSVLoader

from tsetmc_connector import TSETMCConnector



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


    # Database

    db = DatabaseManager()

    db.initialize()



    # Market Status

    market = MarketManager()

    market.status()

    market.update()



    # Portfolio

    portfolio = PortfolioManager()

    print()

    print("Current Portfolio")

    print("-" * 40)

    portfolio.list_assets()



    # ==========================
    # Market Universe Loading
    # ==========================

    connector = TSETMCConnector()

    connector.connect()


    symbols = connector.get_symbols()


    scanner = Scanner()


    scanner.load_market(symbols)



    # Scan Market

    ranking = scanner.scan()



    report = ScannerReport()

    print()

    print("=" * 60)

    print("Scanner Report")

    print("=" * 60)


    report.show(ranking)



    # ==========================
    # Technical Analysis
    # ==========================


    loader = CSVLoader()


    history = loader.load(

        "historical_data.csv"

    )


    print()

    print("=" * 40)

    print("Historical Data")

    print("=" * 40)


    print(

        "Candles :",

        history.count()

    )


    prices = history.close_prices()



    ta = TechnicalAnalysis()


    print()

    print("=" * 40)

    print("Technical Analysis")

    print("=" * 40)


    print(

        "SMA(10) :",

        ta.sma(prices,10)

    )


    print(

        "EMA(10) :",

        ta.ema(prices,10)

    )


    print(

        "RSI(14) :",

        ta.rsi(prices)

    )


    print(

        "MACD :",

        ta.macd(prices)

    )


    bands = ta.bollinger(prices)


    print(

        "Bollinger:",

        bands

    )



    # Score Engine

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

    print(

        "Signal:",

        engine.recommendation(score)

    )



    # Risk Manager

    print()

    print("=" * 60)

    print("Risk Manager")

    print("=" * 60)


    risk = RiskManager()


    capital = 10_000_000

    entry = prices[-1]


    print(

        "Capital       :",

        capital

    )


    print(

        "Position Size :",

        risk.position_size(capital)

    )


    print(

        "Entry Price   :",

        entry

    )


    print(

        "Stop Loss     :",

        risk.stop_loss_price(entry)

    )


    print(

        "Take Profit   :",

        risk.take_profit_price(entry)

    )



    # Position Manager

    print()

    print("=" * 60)

    print("Position Manager")

    print("=" * 60)


    pm = PositionManager()


    pm.open_position(

        "وبملت",

        1000,

        entry

    )


    print(

        "Open Positions :",

        pm.count()

    )


    print(

        pm.list_positions()

    )


    print()

    print(

        "Project initialized successfully."

    )

    print(

        "Ready for development..."

    )




if __name__ == "__main__":

    main()