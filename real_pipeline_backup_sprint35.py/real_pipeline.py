"""
Iran AI Trader Professional
Real Pipeline
Sprint32-E
"""

from scanner import Scanner
from entry_validator import EntryValidator
from trade_candidate import TradeCandidateEngine
from trade_decision import TradeDecisionEngine

from market_regime import MarketRegimeEngine
from regime_report import RegimeReport

from smart_capital_engine import SmartCapitalEngine


class RealPipeline:

    def __init__(self):

        self.scanner = Scanner()

        self.validator = EntryValidator()

        self.candidate_engine = TradeCandidateEngine()

        self.decision_engine = TradeDecisionEngine()

        self.regime_engine = MarketRegimeEngine()

        self.regime_report = RegimeReport()

        self.smart_capital = SmartCapitalEngine()

    # -------------------------------------------------

    def run(self):

        print()
        print("=" * 60)
        print("REAL PIPELINE")
        print("=" * 60)

        # -----------------------------------------
        # STEP 1
        # Scanner
        # -----------------------------------------

        ranking = self.scanner.scan()

        # -----------------------------------------
        # STEP 2
        # Market Regime
        # -----------------------------------------

        regime = self.regime_engine.calculate(
            ranking
        )

        self.regime_report.show(
            regime
        )

        # -----------------------------------------
        # STEP 3
        # Watch List
        # -----------------------------------------

        watchlist = self.scanner.watchlist.all()

        print()
        print(
            "WatchList Loaded:",
            len(watchlist)
        )

        # -----------------------------------------
        # STEP 4
        # Candidate Engine
        # -----------------------------------------

        candidates = self.candidate_engine.generate(
            watchlist,
            self.validator
        )

        # -----------------------------------------
        # STEP 5
        # Decision + Smart Capital
        # -----------------------------------------

        portfolio = []

        decisions = []

        for candidate in candidates:

            decision = self.decision_engine.decide(
                candidate
            )

            capital = self.smart_capital.allocate(
                candidate,
                regime,
                portfolio
            )

            decision["capital"] = capital

            decisions.append(
                decision
            )

            if capital.get(
                "allowed",
                False
            ):
                portfolio.append(
                    candidate["symbol"]
                )

        # -----------------------------------------
        # FINAL REPORT
        # -----------------------------------------

        print()
        print("=" * 60)
        print("PIPELINE FINISHED")
        print("=" * 60)

        print(
            "Candidates:",
            len(candidates)
        )

        print(
            "Decisions:",
            len(decisions)
        )

        print(
            "Market Regime:",
            regime["regime"]
        )

        return {

            "regime": regime,

            "candidates": candidates,

            "decisions": decisions

        }


# -------------------------------------------------

if __name__ == "__main__":

    pipeline = RealPipeline()

    pipeline.run()