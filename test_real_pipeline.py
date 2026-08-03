"""
Iran AI Trader Professional
Real Pipeline Test
Sprint29-D
"""

from scanner import Scanner
from entry_validator import EntryValidator
from real_pipeline import RealPipeline


def main():

    scanner = Scanner()

    validator = EntryValidator()

    pipeline = RealPipeline(

        scanner,

        validator

    )

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


if __name__ == "__main__":
    main()