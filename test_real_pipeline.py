"""
Iran AI Trader Professional
Real Pipeline Test
Sprint31
"""

from real_pipeline import RealPipeline


def main():

    pipeline = RealPipeline()

    result = pipeline.run()

    print()

    print("=" * 60)
    print("REAL PIPELINE FINISHED")
    print("=" * 60)

    print(
        "Candidates :",
        len(result["candidates"])
    )

    print(
        "Decisions :",
        len(result["decisions"])
    )

    print(
        "Market Regime :",
        result["regime"]["regime"]
    )


if __name__ == "__main__":
    main()