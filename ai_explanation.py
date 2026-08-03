"""
Iran AI Trader Professional
AI Explanation Engine
"""

from natural_language import NaturalLanguageGenerator


class AIExplanation:

    def __init__(self):
        self.nlg = NaturalLanguageGenerator()

    def explain(self, decision):

        return {
            "symbol": decision.symbol,
            "signal": decision.signal,
            "score": decision.score,
            "confidence": decision.confidence,
            "risk": decision.risk,
            "summary": self.nlg.generate(decision),
            "reasons": decision.reasons
        }