"""
Iran AI Trader Professional
Final AI Score Test
Sprint31-E
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

    print("FINAL AI SCORE TEST")

    print("=" * 60)

    print()

    print("Technical Score :", result["technical_score"])

    print("Smart Money     :", result["smart_money_score"])

    print("Final AI Score  :", result["final_score"])

    print("Status          :", result["smart_money_status"])


if __name__ == "__main__":

    main()