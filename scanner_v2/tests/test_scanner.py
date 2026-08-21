from scanner_v2.scanner import Scanner


def test_scanner_v2():

    scanner = Scanner()

    results = scanner.scan()

    print()
    print("=" * 60)
    print("SCANNER V2 TEST")
    print("=" * 60)

    print()
    print("TOTAL RESULTS:", len(results))

    for result in results:
        print(
            result["symbol"],
            "|",
            result["score"],
            "|",
            result["decision"]
        )

    assert results is not None
    assert len(results) > 0

    for result in results:

        assert "symbol" in result
        assert "score" in result
        assert "decision" in result

        assert 0 <= result["score"] <= 100

        assert result["decision"] in [
            "STRONG WATCH",
            "WATCH",
            "IGNORE",
            "FAILED"
        ]