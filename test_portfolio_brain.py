"""
Iran AI Trader Professional
Portfolio Brain Test
Sprint34
"""


from portfolio_brain import PortfolioBrain

from portfolio_brain_report import PortfolioBrainReport



def main():


    print()

    print("=" * 70)

    print(

        "AI PORTFOLIO BRAIN TEST"

    )

    print("=" * 70)



    stock_data = {


        "symbol": "چکارن",


        "technical_score": 94.9,


        "smart_money_score": 100,


        "portfolio_score": 90,


        "risk_score": 80


    }



    brain = PortfolioBrain()



    result = brain.analyze(

        stock_data

    )



    report = PortfolioBrainReport()



    report.show(

        result

    )



if __name__ == "__main__":

    main()