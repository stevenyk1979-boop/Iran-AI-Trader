"""
Iran AI Trader Professional
Smart Capital Engine Test
Sprint32-D
"""

from smart_capital_engine import SmartCapitalEngine


def main():

    engine = SmartCapitalEngine()

    candidate = {

        "symbol": "چکارن",

        "final_score": 96.43,

        "price": 25400

    }

    regime = {

        "regime": "BULL"

    }

    result = engine.allocate(

        candidate,

        regime

    )

    print()

    print("=" * 60)
    print("SMART CAPITAL ENGINE")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    main()