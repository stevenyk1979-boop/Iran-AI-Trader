import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from ai_explanation import AIExplanation
from decision_result import DecisionResult


def main():

    decision = DecisionResult(

        symbol="فملی",

        score=92.5,

        confidence=100,

        risk=15,

        signal="STRONG BUY",

        reasons=[

            "Strong Trend",

            "Strong Momentum",

            "High Volume"

        ]

    )

    explanation = AIExplanation()

    result = explanation.explain(decision)

    print("=" * 60)
    print("AI Explanation Test")
    print("=" * 60)

    for key, value in result.items():
        print(f"{key:<12}: {value}")


if __name__ == "__main__":
    main()