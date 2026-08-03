"""
Iran AI Trader Professional
Real Pipeline
Sprint30-C
"""


from scanner import Scanner

from entry_validator import EntryValidator

from trade_candidate import TradeCandidateEngine

from trade_decision import TradeDecisionEngine

from market_regime import MarketRegimeEngine

from regime_report import RegimeReport



class RealPipeline:


    def __init__(self):


        self.scanner = Scanner()


        self.validator = EntryValidator()


        self.candidate_engine = TradeCandidateEngine()


        self.decision_engine = TradeDecisionEngine()


        # Sprint30-C

        self.regime_engine = MarketRegimeEngine()

        self.regime_report = RegimeReport()



    # -------------------------------------------------

    def run(self):


        print()

        print("=" * 60)

        print("REAL PIPELINE")

        print("=" * 60)



        # ---------------------------------------------
        # Step 1
        # Market Scan
        # ---------------------------------------------


        ranking = self.scanner.scan()



        # ---------------------------------------------
        # Step 2
        # Market Regime
        # ---------------------------------------------


        regime = self.regime_engine.calculate(

            ranking

        )


        self.regime_report.show(

            regime

        )



        # ---------------------------------------------
        # Step 3
        # Load WatchList
        # ---------------------------------------------


        watchlist = self.scanner.watchlist.all()



        print()

        print(

            "WatchList Loaded:",

            len(watchlist)

        )



        # ---------------------------------------------
        # Step 4
        # Candidate Generation
        # ---------------------------------------------


        candidates = self.candidate_engine.generate(

            watchlist,

            self.validator

        )



        # ---------------------------------------------
        # Step 5
        # Decision Engine
        # ---------------------------------------------


        decisions = []


        for candidate in candidates:


            decision = self.decision_engine.decide(

                candidate

            )


            decisions.append(

                decision

            )



        # ---------------------------------------------
        # Final Summary
        # ---------------------------------------------


        print()

        print("=" * 60)

        print(

            "PIPELINE FINISHED"

        )

        print("=" * 60)



        print(

            "Candidates:",

            len(candidates)

        )


        print(

            "Decisions:",

            len(decisions)

        )



        return {


            "regime": regime,


            "candidates": candidates,


            "decisions": decisions


        }



# -------------------------------------------------


if __name__ == "__main__":


    pipeline = RealPipeline()


    result = pipeline.run()