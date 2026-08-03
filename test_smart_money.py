"""
Iran AI Trader Professional
Smart Money Test
Sprint31-A
"""


from smart_money_engine import SmartMoneyEngine
from smart_money_report import SmartMoneyReport



def main():


    data = {


        "symbol": "چکارن",


        "volume_ratio": 2.2,


        "buyer_power": 2.5


    }



    engine = SmartMoneyEngine()


    result = engine.analyze(

        data

    )



    report = SmartMoneyReport()


    report.show(

        result

    )



if __name__ == "__main__":

    main()