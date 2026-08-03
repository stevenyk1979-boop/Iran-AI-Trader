"""
Iran AI Trader Professional
Market Regime Test
Sprint30-B
"""


from market_regime import MarketRegimeEngine
from regime_report import RegimeReport



def main():


    print()

    print("=" * 60)

    print("MARKET REGIME TEST")

    print("=" * 60)



    # -----------------------------
    # Fake Ranking Data
    # مشابه خروجی Ranking Engine
    # -----------------------------

    ranking = [


        {

            "symbol": "چکارن",

            "score": 94.9

        },


        {

            "symbol": "محتشم",

            "score": 94.11

        },


        {

            "symbol": "پتایر",

            "score": 80

        },


        {

            "symbol": "کلوند",

            "score": 79.81

        },


        {

            "symbol": "واتی",

            "score": 71.69

        }


    ]



    # -----------------------------
    # Calculate Market Regime
    # -----------------------------


    engine = MarketRegimeEngine()


    regime = engine.calculate(

        ranking

    )



    print()

    print("RAW RESULT")

    print("-" * 40)

    print(regime)



    # -----------------------------
    # Professional Report
    # -----------------------------


    report = RegimeReport()


    report.show(

        regime

    )



if __name__ == "__main__":


    main()