"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Quality + Performance + Risk
Ranking Integration Test
"""


from scanner_v2.performance_risk_analytics_engine import (
    PerformanceRiskAnalyticsEngine
)

from scanner_v2.strategy_quality_ranking_engine import (
    StrategyQualityRankingEngine
)


def test_strategy_quality_performance_risk_ranking_integration():

    trades_a = [

        {
            "symbol": "A",
            "entry_price": 1000,
            "exit_price": 1250,
            "quantity": 10000,
            "pnl": 2500000,
            "result": "WIN"
        },

        {
            "symbol": "A",
            "entry_price": 1000,
            "exit_price": 1100,
            "quantity": 10000,
            "pnl": 1000000,
            "result": "WIN"
        },

        {
            "symbol": "A",
            "entry_price": 1000,
            "exit_price": 950,
            "quantity": 10000,
            "pnl": -500000,
            "result": "LOSS"
        }

    ]

    trades_b = [

        {
            "symbol": "B",
            "entry_price": 1000,
            "exit_price": 1100,
            "quantity": 10000,
            "pnl": 1000000,
            "result": "WIN"
        },

        {
            "symbol": "B",
            "entry_price": 1000,
            "exit_price": 950,
            "quantity": 10000,
            "pnl": -500000,
            "result": "LOSS"
        },

        {
            "symbol": "B",
            "entry_price": 1000,
            "exit_price": 950,
            "quantity": 10000,
            "pnl": -500000,
            "result": "LOSS"
        }

    ]

    performance_a = (
        PerformanceRiskAnalyticsEngine(
            trades=trades_a,
            starting_capital=100000000
        )
    )

    performance_b = (
        PerformanceRiskAnalyticsEngine(
            trades=trades_b,
            starting_capital=100000000
        )
    )

    summary_a = (
        performance_a.refresh()
    )

    summary_b = (
        performance_b.refresh()
    )

    assert (
        summary_a["total_trades"]
        == 3
    )

    assert (
        summary_b["total_trades"]
        == 3
    )

    assert (
        summary_a["net_pnl"]
        == 3000000.0
    )

    assert (
        summary_b["net_pnl"]
        == 0.0
    )

    assert (
        summary_a["profit_factor"]
        > summary_b["profit_factor"]
    )

    quality_engine = (
        StrategyQualityRankingEngine()
    )

    strategies = [

        {
            "symbol": "STRATEGY_A",
            "strategy_quality_score":
                85.0,
            "strategy_quality_status":
                "STRONG",

            "performance":
                summary_a
        },

        {
            "symbol": "STRATEGY_B",
            "strategy_quality_score":
                40.0,
            "strategy_quality_status":
                "WEAK",

            "performance":
                summary_b
        }

    ]

    ranked = (
        quality_engine.rank(
            strategies
        )
    )

    assert (
        len(ranked)
        == 2
    )

    assert (
        ranked[0]["symbol"]
        == "STRATEGY_A"
    )

    assert (
        ranked[0]["rank"]
        == 1
    )

    assert (
        ranked[1]["symbol"]
        == "STRATEGY_B"
    )

    assert (
        ranked[1]["rank"]
        == 2
    )

    assert (
        ranked[0]["performance"][
            "net_pnl"
        ]
        == 3000000.0
    )

    assert (
        ranked[1]["performance"][
            "net_pnl"
        ]
        == 0.0
    )

    print()

    print("=" * 70)

    print(
        "STRATEGY QUALITY + PERFORMANCE + RISK RANKING"
    )

    print("=" * 70)

    for item in ranked:

        performance = (
            item["performance"]
        )

        print(

            f'RANK {item["rank"]}',

            "| Strategy:",
            item["symbol"],

            "| Score:",
            item["score"],

            "| Quality:",
            item["status"],

            "| Net P/L:",
            performance["net_pnl"],

            "| PF:",
            performance["profit_factor"],

            "| Max DD %:",
            performance[
                "max_drawdown_percent"
            ]

        )

    print("=" * 70)