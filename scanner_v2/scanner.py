"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Scanner Core
Market Regime Integrated
Regime-Aware Ranking
Regime-Aware Decision
"""

from scanner_v2.market_loader import MarketLoader
from scanner_v2.history_loader import HistoryLoader
from scanner_v2.validator import Validator
from scanner_v2.ranking_engine import RankingEngine
from scanner_v2.market_regime_adapter import MarketRegimeAdapter
from scanner_v2.regime_aware_ranker import RegimeAwareRanker
from scanner_v2.regime_aware_decision import RegimeAwareDecision
from scanner_v2.config import ScannerConfig


class Scanner:

    def __init__(self, config=None):

        self.config = (
            config
            or ScannerConfig()
        )

        # ---------------------------------------------
        # Core engines
        # ---------------------------------------------

        self.market_loader = MarketLoader(
            config=self.config
        )

        self.history_loader = HistoryLoader(
            config=self.config
        )

        self.validator = Validator(
            config=self.config
        )

        self.ranking_engine = RankingEngine(
            config=self.config
        )

        # ---------------------------------------------
        # Market Regime
        # ---------------------------------------------

        self.market_regime_adapter = (
            MarketRegimeAdapter()
        )

        self.market_regime = {
            "regime": "UNKNOWN",
            "score": 0
        }

        # ---------------------------------------------
        # Regime-Aware Ranking
        # ---------------------------------------------

        self.regime_aware_ranker = (
            RegimeAwareRanker()
        )

        # ---------------------------------------------
        # Regime-Aware Decision
        # ---------------------------------------------

        self.regime_aware_decision = (
            RegimeAwareDecision()
        )

        # ---------------------------------------------
        # Final results
        # ---------------------------------------------

        self.results = []


    # =================================================
    # SCAN
    # =================================================

    def scan(
        self,
        market_regime_data=None
    ):

        self.results = []

        # ---------------------------------------------
        # Market Regime
        # ---------------------------------------------

        if market_regime_data is not None:

            self.market_regime = (
                self.market_regime_adapter.analyze(
                    market_regime_data
                )
            )

        else:

            self.market_regime = {
                "regime": "UNKNOWN",
                "score": 0
            }

        # ---------------------------------------------
        # Market Regime Output
        # ---------------------------------------------

        print()

        print("=" * 60)

        print("MARKET REGIME")

        print("=" * 60)

        print(
            "Regime:",
            self.market_regime.get(
                "regime",
                "UNKNOWN"
            )
        )

        print(
            "Score:",
            self.market_regime.get(
                "score",
                0
            )
        )

        # ---------------------------------------------
        # Load Symbols
        # ---------------------------------------------

        symbols = (
            self.market_loader.load_symbols()
        )

        print()

        print(
            "DEBUG SYMBOL COUNT:",
            len(symbols)
        )

        print(
            "DEBUG SYMBOLS:",
            symbols
        )

        # ---------------------------------------------
        # Scan Symbols
        # ---------------------------------------------

        for symbol in symbols:

            result = (
                self.scan_symbol(symbol)
            )

            if result is not None:

                # -------------------------------------
                # Attach Market Regime
                # -------------------------------------

                result["market_regime"] = (
                    self.market_regime.get(
                        "regime",
                        "UNKNOWN"
                    )
                )

                result["market_regime_score"] = (
                    self.market_regime.get(
                        "score",
                        0
                    )
                )

                self.results.append(
                    result
                )

        # ---------------------------------------------
        # Regime-Aware Ranking
        # ---------------------------------------------

        self.results = (
            self.regime_aware_ranker.rank(
                self.results
            )
        )

        # ---------------------------------------------
        # Regime-Aware Final Decision
        # ---------------------------------------------

        for item in self.results:

            adjusted_score = item.get(
                "regime_adjusted_score",
                item.get(
                    "score",
                    0
                )
            )

            decision_result = (
                self.regime_aware_decision.decide(
                    adjusted_score,
                    self.market_regime.get(
                        "regime",
                        "UNKNOWN"
                    )
                )
            )

            # Keep original decision
            # for diagnostics and analysis.

            item["original_decision"] = (
                item.get(
                    "decision",
                    "IGNORE"
                )
            )

            # Final regime-aware decision

            item["decision"] = (
                decision_result[
                    "decision"
                ]
            )

            # Store thresholds

            item["decision_thresholds"] = {

                "strong_watch": (
                    decision_result[
                        "strong_watch_threshold"
                    ]
                ),

                "watch": (
                    decision_result[
                        "watch_threshold"
                    ]
                )
            }

        # ---------------------------------------------
        # Final Ranking Output
        # ---------------------------------------------

        print()

        print("=" * 60)

        print("REGIME-AWARE FINAL RANKING")

        print("=" * 60)

        for item in self.results:

            print(
                item.get(
                    "rank",
                    0
                ),

                item.get(
                    "symbol",
                    "UNKNOWN"
                ),

                "| Base:",

                item.get(
                    "score",
                    0
                ),

                "| Adjusted:",

                item.get(
                    "regime_adjusted_score",
                    0
                ),

                "| Decision:",

                item.get(
                    "decision",
                    "IGNORE"
                )
            )

        return self.results


    # =================================================
    # SCAN SYMBOL
    # =================================================

    def scan_symbol(
        self,
        symbol
    ):

        try:

            print()

            print(
                "Scanning:",
                symbol
            )

            # -----------------------------------------
            # Load History
            # -----------------------------------------

            history = (
                self.history_loader.load(
                    symbol
                )
            )

            if history is None:

                print(
                    "No history:",
                    symbol
                )

                return None

            # -----------------------------------------
            # Validate History
            # -----------------------------------------

            valid = (
                self.validator.validate_history(
                    history,
                    symbol
                )
            )

            if not valid:

                print(
                    "Validation failed:",
                    symbol
                )

                return None

            # -----------------------------------------
            # Base Ranking
            # -----------------------------------------

            result = (
                self.ranking_engine.analyze(
                    history,
                    symbol
                )
            )

            print()

            print(
                "Ranking result:",
                result
            )

            # -----------------------------------------
            # Validate Score
            # -----------------------------------------

            if not self.validator.validate_score(
                result.get(
                    "score"
                )
            ):

                print(
                    "Invalid score:",
                    symbol
                )

                return None

            return result

        except Exception as error:

            print()

            print(
                "Scanner error:",
                symbol,
                error
            )

            return None


    # =================================================
    # STATISTICS
    # =================================================

    def statistics(self):

        return {

            "symbols_scanned": len(
                self.results
            ),

            "watch": len(
                [
                    r
                    for r in self.results
                    if r.get(
                        "decision"
                    ) == "WATCH"
                ]
            ),

            "strong_watch": len(
                [
                    r
                    for r in self.results
                    if r.get(
                        "decision"
                    ) == "STRONG WATCH"
                ]
            ),

            "ignore": len(
                [
                    r
                    for r in self.results
                    if r.get(
                        "decision"
                    ) == "IGNORE"
                ]
            ),

            "market_regime": (
                self.market_regime.get(
                    "regime",
                    "UNKNOWN"
                )
            ),

            "market_regime_score": (
                self.market_regime.get(
                    "score",
                    0
                )
            )
        }