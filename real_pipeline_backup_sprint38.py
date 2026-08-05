"""
Iran AI Trader Professional
Real Pipeline
Sprint36
"""


from scanner import Scanner

from entry_validator import EntryValidator

from trade_candidate import TradeCandidateEngine

from trade_decision import TradeDecisionEngine

from market_regime import MarketRegimeEngine

from regime_report import RegimeReport


# Sprint35 Intelligence

from pipeline_intelligence import PipelineIntelligence

from pipeline_intelligence_report import PipelineIntelligenceReport




class RealPipeline:


    def __init__(self):


        self.scanner = Scanner()


        self.validator = EntryValidator()


        self.candidate_engine = TradeCandidateEngine()


        self.decision_engine = TradeDecisionEngine()



        # Market Regime

        self.regime_engine = MarketRegimeEngine()

        self.regime_report = RegimeReport()



        # Sprint36

        self.pipeline_intelligence = PipelineIntelligence()

        self.intelligence_report = PipelineIntelligenceReport()




    # -------------------------------------------------

    def run(self):


        print()

        print("=" * 70)

        print(

            "REAL PIPELINE SPRINT36"

        )

        print("=" * 70)




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
        # WatchList
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
        # Trade Decision Engine
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
        # Step 6
        # Sprint36 AI Intelligence Layer
        # ---------------------------------------------


        intelligence_results = self.pipeline_intelligence.analyze_all(

            candidates

        )




        approved = self.pipeline_intelligence.approved_only(

            intelligence_results

        )




        # ---------------------------------------------
        # Final Intelligence Report
        # ---------------------------------------------


        self.intelligence_report.show(

            intelligence_results

        )




        print()

        print("=" * 70)

        print(

            "PIPELINE FINISHED"

        )

        print("=" * 70)



        print(

            "Candidates:",

            len(candidates)

        )


        print(

            "Decisions:",

            len(decisions)

        )


        print(

            "AI Approved:",

            len(approved)

        )




        return {


            "regime": regime,


            "candidates": candidates,


            "decisions": decisions,


            "intelligence": intelligence_results,


            "approved": approved

        }




# -------------------------------------------------


if __name__ == "__main__":


    pipeline = RealPipeline()


    result = pipeline.run()