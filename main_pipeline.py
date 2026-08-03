"""
Iran AI Trader Professional
Main Pipeline
Sprint29-C
"""

from pipeline import TradingPipeline
from daily_report import DailyReport


class MainPipeline:

    def __init__(

        self,

        validator,

        scanner

    ):

        self.validator = validator
        self.scanner = scanner

    # -----------------------------

    def run(self):

        watchlist = self.scanner.watchlist()

        pipeline = TradingPipeline(

            self.validator

        )

        result = pipeline.run(

            watchlist,

            total_symbols=len(

                watchlist

            )

        )

        return result