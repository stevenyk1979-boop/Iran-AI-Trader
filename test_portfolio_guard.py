"""
Iran AI Trader Professional
Portfolio Guard Test
Sprint32-C
"""

from portfolio_guard import PortfolioGuard


def main():

    guard = PortfolioGuard()

    portfolio = [

        "چکارن",

        "پتایر"

    ]

    result = guard.allow(

        portfolio,

        "فایرا",

        10

    )

    print()

    print("=" * 60)
    print("PORTFOLIO GUARD TEST")
    print("=" * 60)

    print()

    print(

        "Allowed :",

        result

    )


if __name__ == "__main__":

    main()