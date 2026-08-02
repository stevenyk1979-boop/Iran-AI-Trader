"""
Iran AI Trader Professional
Decision Result
"""

from dataclasses import dataclass, field


@dataclass
class DecisionResult:

    symbol: str = ""

    score: float = 0.0

    confidence: float = 0.0

    risk: float = 0.0

    signal: str = "HOLD"

    reasons: list = field(default_factory=list)

    detail: dict = field(default_factory=dict)

    def summary(self):

        return {

            "symbol": self.symbol,

            "score": round(self.score, 2),

            "confidence": round(self.confidence, 2),

            "risk": round(self.risk, 2),

            "signal": self.signal,

            "reasons": self.reasons

        }