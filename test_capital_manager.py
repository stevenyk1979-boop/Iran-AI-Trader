"""
Iran AI Trader Professional
Capital Manager Test
Sprint32-A
"""

from capital_manager import CapitalManager


def main():

    manager = CapitalManager(

        capital=100_000_000,

        risk_percent=1

    )

    candidate = {

        "symbol": "چکارن",

        "final_score": 96.43

    }

    result = manager.allocate(

        candidate

    )

    print()

    print("=" * 60)

    print("CAPITAL MANAGER TEST")

    print("=" * 60)

    print()

    print(

        "Capital :",

        manager.capital

    )

    print(

        "Max Risk :",

        manager.max_risk_amount()

    )

    print()

    print(

        "Allocation :",

        result["allocation_percent"],

        "%"

    )

    print(

        "Capital Used :",

        result["capital"]

    )


if __name__ == "__main__":

    main()