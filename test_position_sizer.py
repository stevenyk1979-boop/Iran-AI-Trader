"""
Iran AI Trader Professional
Position Sizer Test
Sprint32-B
"""

from position_sizer import PositionSizer


def main():

    sizer = PositionSizer()

    result = sizer.calculate(

        capital=10_000_000,

        price=25400

    )

    print()

    print("=" * 60)
    print("POSITION SIZER TEST")
    print("=" * 60)

    print()

    print("Capital :", 10_000_000)

    print("Price   :", 25400)

    print()

    print("Shares  :", result["shares"])

    print("Used    :", result["capital_used"])


if __name__ == "__main__":
    main()