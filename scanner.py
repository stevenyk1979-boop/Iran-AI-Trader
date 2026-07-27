"""
Iran AI Trader V2.0
Scanner Engine
"""

from csv_loader import CSVLoader
from technical_analysis import TechnicalAnalysis
from score_engine import ScoreEngine


class Scanner:

    def scan(self):

        loader = CSVLoader()

        history = loader.load("historical_data.csv")

        prices = history.close_prices()

        ta = TechnicalAnalysis()

        engine = ScoreEngine()

        rsi = ta.rsi(prices)

        macd = ta.macd(prices)

        bands = ta.bollinger(prices)

        score = engine.total_score(
            rsi,
            macd,
            bands,
            prices[-1]
        )

        print()

        print("=" * 50)

        print("Scanner Report")

        print("=" * 50)

        print("Symbol :", history.last().symbol)

        print("Last Price :", prices[-1])

        print()

        print("RSI :", rsi)

        print("MACD :", macd)

        print("Bollinger :", bands)

        print()

        print("Score :", score)

        print("Signal :", engine.recommendation(score))