"""
Iran AI Trader Professional
AI Score Engine
"""

from trend_strength import TrendStrength
from momentum_engine import MomentumEngine
from volume_engine import VolumeEngine
from risk_engine import RiskEngine
from decision_engine import DecisionEngine


class AIScoreEngine:

    def __init__(self):

        self.trend = TrendStrength()

        self.momentum = MomentumEngine()

        self.volume = VolumeEngine()

        self.risk = RiskEngine()

        self.decision = DecisionEngine()


    # ---------------------------------

    def score(

        self,

        history,

        analysis,

        symbol=None

    ):

        """
        Run AI scoring pipeline
        """


        engines = {}


        # ---------------------------------
        # Trend
        # ---------------------------------

        engines["trend"] = self.trend.score(

            analysis

        )


        # ---------------------------------
        # Momentum
        # ---------------------------------

        engines["momentum"] = self.momentum.score(

            analysis

        )


        # ---------------------------------
        # Volume
        # ---------------------------------

        volumes = history.volumes()


        engines["volume"] = self.volume.score(

            volumes

        )


        # ---------------------------------
        # Risk
        # ---------------------------------

        risk_result = self.risk.calculate(

            history

        )


        # ---------------------------------
        # Final Decision
        # ---------------------------------

        result = self.decision.decide(

            symbol,

            engines,

            risk_result

        )


        return result