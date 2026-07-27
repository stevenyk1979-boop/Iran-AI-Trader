from pathlib import Path

from config import PROJECT_NAME, VERSION
from database import DatabaseManager
from market import MarketManager
from portfolio import PortfolioManager
from scanner import Scanner


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

    portfolio.add_asset(
        "وبملت",
        1000,
        1675
    )

    portfolio.list_assets()

    scanner = Scanner()
    scanner.scan()

    print()
    print("Project initialized successfully.")
    print("Ready for development...")


if __name__ == "__main__":
    main()