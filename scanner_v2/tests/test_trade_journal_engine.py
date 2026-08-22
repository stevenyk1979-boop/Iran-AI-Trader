from scanner_v2.trade_journal_engine import (
    TradeJournalEngine
)


def test_trade_journal_engine():

    engine = TradeJournalEngine()

    trades = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "current_price": 1750,
            "quantity": 20000,
            "status": "CLOSED",
            "exit_reason": "TAKE PROFIT"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "current_price": 1800,
            "quantity": 10000,
            "status": "CLOSED",
            "exit_reason": "STOP LOSS"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "current_price": 1000,
            "quantity": 5000,
            "status": "CLOSED",
            "exit_reason": "MANUAL"
        }

    ]

    records = engine.record(
        trades
    )

    assert len(records) == 3

    assert records[0]["result"] == "WIN"
    assert records[1]["result"] == "LOSS"
    assert records[2]["result"] == "BREAKEVEN"

    assert records[0]["pnl"] == 15_000_000
    assert records[1]["pnl"] == -2_000_000
    assert records[2]["pnl"] == 0

    assert engine.total_pnl() == 13_000_000

    assert engine.total_profit() == 15_000_000

    assert engine.total_loss() == -2_000_000

    assert engine.win_rate() == 33.33

    assert engine.average_win() == 15_000_000

    assert engine.average_loss() == -2_000_000

    assert engine.profit_factor() == 7.5

    stats = engine.statistics()

    assert stats["total_trades"] == 3
    assert stats["winning_trades"] == 1
    assert stats["losing_trades"] == 1
    assert stats["breakeven_trades"] == 1
    assert stats["net_pnl"] == 13_000_000

    print()
    print("=" * 60)
    print("TRADE JOURNAL + PERFORMANCE ENGINE")
    print("=" * 60)

    for trade in records:

        print(
            trade["symbol"],
            "| Entry:",
            trade["entry_price"],
            "| Exit:",
            trade["exit_price"],
            "| P/L:",
            trade["pnl"],
            "| Result:",
            trade["result"]
        )

    print("-" * 60)

    print(
        "Total:",
        stats["total_trades"]
    )

    print(
        "Wins:",
        stats["winning_trades"]
    )

    print(
        "Losses:",
        stats["losing_trades"]
    )

    print(
        "Win Rate:",
        stats["win_rate_percent"],
        "%"
    )

    print(
        "Net P/L:",
        stats["net_pnl"]
    )

    print(
        "Profit Factor:",
        stats["profit_factor"]
    )

    print("=" * 60)