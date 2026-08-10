"""
Iran AI Trader Professional

Scanner V2

Sprint44-16

Scanner Core Config Integrated
"""

from scanner_v2.market_loader import MarketLoader
from scanner_v2.history_loader import HistoryLoader
from scanner_v2.validator import Validator
from scanner_v2.ranking_engine import RankingEngine
from scanner_v2.config import ScannerConfig


class Scanner:

    def __init__(self):

        self.config = ScannerConfig()

        self.market_loader = MarketLoader()

        self.history_loader = HistoryLoader()

        self.validator = Validator()

        self.ranking_engine = RankingEngine()

        self.results = []

    def scan(self):

        self.results = []

        symbols = self.market_loader.load_symbols()

        print(
            "DEBUG SYMBOL COUNT:",
            len(symbols)
        )

        print(
            "DEBUG SYMBOLS:",
            symbols
        )

        for symbol in symbols:

            result = self.scan_symbol(symbol)

            if result is not None:

                self.results.append(result)

        return self.results

    def scan_symbol(
        self,
        symbol
    ):

        try:

            print(
                "Scanning:",
                symbol
            )

            history = self.history_loader.load(symbol)

            if history is None:

                print(
                    "No history:",
                    symbol
                )

                return None

            valid = self.validator.validate_history(
                history,
                symbol
            )

            if not valid:

                print(
                    "Validation failed:",
                    symbol
                )

                return None

            result = self.ranking_engine.analyze(
                history,
                symbol
            )

            print(
                "Ranking result:",
                result
            )

            if not self.validator.validate_score(
                result.get("score")
            ):

                print(
                    "Invalid score:",
                    symbol
                )

                return None

            return result

        except Exception as error:

            print(
                "Scanner error:",
                symbol,
                error
            )

            return None

    def statistics(self):

        return {
            "symbols_scanned": len(self.results),
            "watch": len(
                [
                    r for r in self.results
                    if r["decision"] == "WATCH"
                ]
            ),
            "strong_watch": len(
                [
                    r for r in self.results
                    if r["decision"] == "STRONG WATCH"
                ]
            )
        }