"""
Iran AI Trader Professional
Real Pipeline
Sprint29-D
"""

from pipeline import TradingPipeline


class RealPipeline:

    def __init__(self, scanner, validator):

        self.scanner = scanner
        self.validator = validator

    # ---------------------------------

    def run(self):

        print("=" * 60)
        print("REAL PIPELINE")
        print("=" * 60)

        # اجرای اسکن واقعی
        ranking = self.scanner.scan()

        # اگر WatchList کلاس متد all() داشته باشد از آن استفاده می‌کنیم،
        # در غیر این صورت از ranking استفاده می‌کنیم.
        if hasattr(self.scanner.watchlist, "all"):

            watchlist = self.scanner.watchlist.all()

        else:

            watchlist = ranking

        print(f"WatchList Loaded : {len(watchlist)}")

        pipeline = TradingPipeline(self.validator)

        result = pipeline.run(

            watchlist,

            total_symbols=len(ranking)

        )

        print("Pipeline Finished")

        return result