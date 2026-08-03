"""
Iran AI Trader Professional
Smart Money Integration Test
Sprint31-D
"""

from smart_money_integration import SmartMoneyIntegration


def main():

    item = {

        "symbol": "چکارن",

        "score": 94.9,

        "volume_ratio": 2.2,

        "buyer_power": 2.5

    }


    integration = SmartMoneyIntegration()

    result = integration.integrate(item)


    print()

    print("=" * 60)

    print("SMART MONEY INTEGRATION TEST")

    print("=" * 60)

    print()

    print("Symbol:", result["symbol"])

    print("Technical:", result["technical_score"])

    print("Smart Money:", result["smart_money_score"])

    print("Final:", result["final_score"])

    print("Status:", result["smart_money_status"])

    print()

    print("Signals")

    print("-" * 40)

    for signal in result["smart_money_signals"]:

        print("✓", signal)


if __name__ == "__main__":

    main()