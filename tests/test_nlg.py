import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
from natural_language import NaturalLanguageGenerator
from decision_result import DecisionResult

d = DecisionResult(
    symbol="فملی",
    score=92,
    confidence=100,
    risk=15,
    signal="STRONG BUY",
    reasons=[]
)

print(
    NaturalLanguageGenerator().generate(d)
)