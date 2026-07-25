from pathlib import Path

from config import PROJECT_NAME, VERSION
from database import DatabaseManager
from market import MarketManager


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

    print("Project initialized successfully.")
    print("Ready for development...")


if __name__ == "__main__":
    main()