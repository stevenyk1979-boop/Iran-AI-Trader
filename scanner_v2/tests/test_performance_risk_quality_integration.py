"""
Iran AI Trader Professional

Scanner V2

Sprint50

Performance Risk + Strategy Quality Integration Test
"""


from scanner_v2.performance_risk_analytics_engine import (
    PerformanceRiskAnalyticsEngine
)


def test_performance_risk_quality_integration():

    trades = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "exit_price": 1750,
            "quantity": 20000,
            "pnl": 15000000,
            "result": "WIN"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "exit_price": 1800,
            "quantity": 10000,
            "pnl": -2000000,
            "result": "LOSS"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "exit_price": 1000,
            "quantity": 10000,
            "pnl": 0,
            "result": "BREAKEVEN"
        }

    ]

    engine = (
        PerformanceRiskAnalyticsEngine(
            trades=trades,
            starting_capital=100000000
        )
    )

    summary = (
        engine.refresh()
    )

    assert (
        summary["total_trades"]
        == 3
    )

    assert (
        summary["wins"]
        == 1
    )

    assert (
        summary["losses"]
        == 1
    )

    assert (
        summary["net_pnl"]
        == 13000000.0
    )

    assert (
        summary["win_rate_percent"]
        == 33.33
    )

    assert (
        summary["profit_factor"]
        == 7.5
    )

    assert (
        summary["return_percent"]
        == 13.0
    )

    assert (
        "recovery_percent"
        in summary
    )

    assert (
        "strategy_quality_score"
        in summary
    )

    assert (
        "strategy_quality_status"
        in summary
    )

    assert (
        0.0
        <= summary[
            "strategy_quality_score"
        ]
        <= 100.0
    )

    print()

    print("=" * 60)

    print(
        "PERFORMANCE RISK + STRATEGY QUALITY"
    )

    print("=" * 60)

    print(
        "Trades:",
        summary[
            "total_trades"
        ]
    )

    print(
        "Win Rate:",
        summary[
            "win_rate_percent"
        ],
        "%"
    )

    print(
        "Net P/L:",
        summary[
            "net_pnl"
        ]
    )

    print(
        "Profit Factor:",
        summary[
            "profit_factor"
        ]
    )

    print(
        "Return:",
        summary[
            "return_percent"
        ],
        "%"
    )

    print(
        "Max Drawdown:",
        summary[
            "max_drawdown"
        ]
    )

    print(
        "Max Drawdown %:",
        summary[
            "max_drawdown_percent"
        ],
        "%"
    )

    print(
        "Recovery:",
        summary[
            "recovery_percent"
        ],
        "%"
    )

    print(
        "Strategy Quality Score:",
        summary[
            "strategy_quality_score"
        ]
    )

    print(
        "Strategy Quality:",
        summary[
            "strategy_quality_status"
        ]
    )

    print("=" * 60)