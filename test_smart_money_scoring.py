"""
Iran AI Trader Professional
Smart Money Scoring Test
Sprint31-C
"""


from smart_money_scoring import SmartMoneyScoring



def main():


    engine = SmartMoneyScoring()



    technical_score = 94.9


    smart_money_score = 100



    final_score = engine.calculate(

        technical_score,

        smart_money_score

    )



    status = engine.status(

        smart_money_score

    )



    print()

    print("=" * 60)

    print("SMART MONEY SCORING TEST")

    print("=" * 60)



    print()

    print(

        "Technical Score:",

        technical_score

    )


    print(

        "Smart Money Score:",

        smart_money_score

    )


    print(

        "Final AI Score:",

        final_score

    )


    print(

        "Smart Money Status:",

        status

    )



if __name__ == "__main__":


    main()