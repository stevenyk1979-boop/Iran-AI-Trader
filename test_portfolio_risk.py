"""
Iran AI Trader Professional
Portfolio Risk Test
Sprint33-D
"""


from portfolio_risk_engine import PortfolioRiskEngine

from portfolio_risk_report import PortfolioRiskReport



def main():


    print()

    print("=" * 70)

    print(

        "PORTFOLIO RISK ENGINE TEST"

    )

    print("=" * 70)



    prices = [

        10000,

        10500,

        11000,

        10800,

        10200,

        9800

    ]



    engine = PortfolioRiskEngine()



    result = engine.analyze(

        prices

    )



    report = PortfolioRiskReport()



    report.show(

        result

    )



if __name__ == "__main__":

    main()