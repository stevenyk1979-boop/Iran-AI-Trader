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

    scanner = Scanner()

    ranking = scanner.scan()
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


   


    print()

    print(

        "Project initialized successfully."

    )

    print(

        "Ready for development..."

    )




if __name__ == "__main__":

    main()