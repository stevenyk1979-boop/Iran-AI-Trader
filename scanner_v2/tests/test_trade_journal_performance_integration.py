"""
Iran AI Trader Professional

Scanner V2

Sprint46

Trade Journal + Performance Integration Test

Pipeline:

Closed Positions
        ↓
Trade Journal
        ↓
Performance Analytics

IMPORTANT:
No broker connection.
No real order execution.
"""

from scanner_v2.trade_journal_engine import (
    TradeJournalEngine
)

from scanner_v2.performance_analytics_engine import (
    PerformanceAnalyticsEngine
)


def test_trade_journal_performance_integration():

    journal_engine = (
        TradeJournalEngine()
    )

    # -------------------------------------------------
    # CLOSED POSITIONS
    # -------------------------------------------------

    closed_positions = [

        {
            "symbol": "TEST1",

            "entry_price": 1000,

            "current_price": 1750,

            "quantity": 20_000,

            "status": "CLOSED",

            "exit_reason": "TAKE PROFIT"

        },

        {

            "symbol": "TEST2",

            "entry_price": 2000,

            "current_price": 1800,

            "quantity": 10_000,

            "status": "CLOSED",

            "exit_reason": "STOP LOSS"

        },

        {

            "symbol": "TEST3",

            "entry_price": 1000,

            "current_price": 1000,

            "quantity": 5_000,

            "status": "CLOSED",

            "exit_reason": "MANUAL"

        }

    ]

    # -------------------------------------------------
    # STEP 1
    # JOURNAL
    # -------------------------------------------------

    journal_records = (
        journal_engine.record(
            closed_positions
        )
    )

    assert len(
        journal_records
    ) == 3

    # -------------------------------------------------
    # JOURNAL VALIDATION
    # -------------------------------------------------

    assert (
        journal_records[0][
            "symbol"
        ]
        == "TEST1"
    )

    assert (
        journal_records[0][
            "result"
        ]
        == "WIN"
    )

    assert (
        journal_records[0][
            "pnl"
        ]
        == 15_000_000
    )

    assert (
        journal_records[1][
            "result"
        ]
        == "LOSS"
    )

    assert (
        journal_records[1][
            "pnl"
        ]
        == -2_000_000
    )

    assert (
        journal_records[2][
            "result"
        ]
        == "BREAKEVEN"
    )

    assert (
        journal_records[2][
            "pnl"
        ]
        == 0
    )

    # -------------------------------------------------
    # STEP 2
    # PERFORMANCE ANALYTICS
    # -------------------------------------------------

    analytics_engine = (
        PerformanceAnalyticsEngine(
            journal_records
        )
    )

    # -------------------------------------------------
    # PERFORMANCE CHECKS
    # -------------------------------------------------

    assert (
        analytics_engine.total_pnl()
        == 13_000_000
    )

    assert (
        analytics_engine.total_profit()
        == 15_000_000
    )

    assert (
        analytics_engine.total_loss()
        == -2_000_000
    )

    assert (
        analytics_engine.win_rate()
        == 33.33
    )

    assert (
        analytics_engine.expectancy()
        == 4_333_333.33
    )

    assert (
        analytics_engine.profit_factor()
        == 7.5
    )

    assert (
        analytics_engine.return_percent(
            100_000_000
        )
        == 13.0
    )

    assert (
        analytics_engine.performance_status()
        == "STRONG"
    )

    # -------------------------------------------------
    # STEP 3
    # STATISTICS
    # -------------------------------------------------

    stats = (
        analytics_engine.statistics(
            100_000_000
        )
    )

    assert (
        stats["total_trades"]
        == 3
    )

    assert (
        stats["wins"]
        == 1
    )

    assert (
        stats["losses"]
        == 1
    )

    assert (
        stats["net_pnl"]
        == 13_000_000
    )

    assert (
        stats["performance_status"]
        == "STRONG"
    )

    # -------------------------------------------------
    # OUTPUT
    # -------------------------------------------------

    print()

    print("=" * 60)

    print(
        "TRADE JOURNAL + PERFORMANCE INTEGRATION"
    )

    print("=" * 60)

    for trade in journal_records:

        print(

            trade["symbol"],

            "| P/L:",

            trade["pnl"],

            "| Result:",

            trade["result"]

        )

    print("-" * 60)

    print(
        "Trades:",
        stats[
            "total_trades"
        ]
    )

    print(
        "Win Rate:",
        stats[
            "win_rate_percent"
        ],
        "%"
    )

    print(
        "Net P/L:",
        stats[
            "net_pnl"
        ]
    )

    print(
        "Expectancy:",
        stats[
            "expectancy"
        ]
    )

    print(
        "Profit Factor:",
        stats[
            "profit_factor"
        ]
    )

    print(
        "Performance:",
        stats[
            "performance_status"
        ]
    )

    print("=" * 60)