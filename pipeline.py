"""
Iran AI Trader Professional
AI Trading Pipeline
Sprint29-B
"""


from trade_candidate import TradeCandidateEngine
from trade_decision import TradeDecisionEngine
from daily_report import DailyReport



class TradingPipeline:


    def __init__(

        self,

        validator

    ):


        self.validator = validator

        self.candidate_engine = TradeCandidateEngine()

        self.decision_engine = TradeDecisionEngine()

        self.report_engine = DailyReport()



    # ---------------------------------


    def run(

        self,

        watchlist,

        total_symbols=0

    ):


        candidates = self.candidate_engine.generate(

            watchlist,

            self.validator

        )


        decisions = []


        for candidate in candidates:


            decision = self.decision_engine.decide(

                candidate

            )


            decisions.append(

                decision

            )


        report = self.report_engine.generate(

            decisions,

            total_symbols,

            len(watchlist)

        )


        return {


            "candidates": candidates,

            "decisions": decisions,

            "report": report

        }