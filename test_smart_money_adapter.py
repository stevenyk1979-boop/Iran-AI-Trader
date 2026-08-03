"""
Iran AI Trader Professional
Smart Money Adapter Test
Sprint31-B
"""


from smart_money_adapter import SmartMoneyAdapter



def main():


    item = {


        "symbol": "چکارن",


        "score": 94.9,


        "volume_ratio": 2.2,


        "buyer_power": 2.5


    }



    adapter = SmartMoneyAdapter()


    result = adapter.apply(

        item

    )


    print()

    print("=" * 60)

    print("SMART MONEY ADAPTER TEST")

    print("=" * 60)


    print()

    print(

        result

    )



if __name__ == "__main__":

    main()