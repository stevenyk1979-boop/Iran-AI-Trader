"""
Iran AI Trader Professional
Portfolio Optimizer Test
Sprint33-A
"""


from portfolio_optimizer import PortfolioOptimizer
from portfolio_report import PortfolioReport



def main():


    decisions = [


        {

            "symbol": "چکارن",

            "score": 96.43,

            "signal": "BUY"

        },


        {

            "symbol": "ولملت",

            "score": 91,

            "signal": "BUY"

        },


        {

            "symbol": "دزاگرس",

            "score": 75,

            "signal": "HOLD"

        }

    ]



    optimizer = PortfolioOptimizer()


    result = optimizer.optimize(

        decisions

    )


    report = PortfolioReport()


    report.show(

        result

    )



if __name__ == "__main__":

    main()