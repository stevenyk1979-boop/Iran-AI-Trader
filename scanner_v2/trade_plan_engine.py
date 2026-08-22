"""
Iran AI Trader Professional

Scanner V2

Sprint45-10

Trade Plan Engine

Builds a standardized trade plan from the
outputs of the Scanner V2 decision pipeline.

Portfolio Risk Integrated
"""


class TradePlanEngine:

    def __init__(
        self,
        portfolio_risk_engine=None,
        total_capital=0
    ):

        self.plans = []

        self.portfolio_risk_engine = (
            portfolio_risk_engine
        )

        self.total_capital = self._number(
            total_capital
        )

        self.current_invested = 0.0

    # -------------------------------------------------
    # Safe numeric conversion
    # -------------------------------------------------

    def _number(
        self,
        value,
        default=0.0
    ):

        try:

            return float(value)

        except Exception:

            return float(default)

    # -------------------------------------------------
    # Configure portfolio risk
    # -------------------------------------------------

    def configure_portfolio_risk(
        self,
        portfolio_risk_engine,
        total_capital,
        current_invested=0
    ):

        self.portfolio_risk_engine = (
            portfolio_risk_engine
        )

        self.total_capital = self._number(
            total_capital
        )

        self.current_invested = self._number(
            current_invested
        )

    # -------------------------------------------------
    # Portfolio risk check
    # -------------------------------------------------

    def _portfolio_risk_check(
        self,
        order_value,
        result=None
    ):

        # Risk engine is optional.
        # Existing behavior remains unchanged
        # when no engine is supplied.

        if self.portfolio_risk_engine is None:

            return {
                "allowed": True,
                "status": "NOT CHECKED",
                "reason": None
            }

        if order_value <= 0:

            return {
                "allowed": False,
                "status": "REJECTED",
                "reason": "INVALID ORDER VALUE"
            }

        if self.total_capital <= 0:

            return {
                "allowed": False,
                "status": "REJECTED",
                "reason": "INVALID TOTAL CAPITAL"
            }

        try:

            allowed = (
                self.portfolio_risk_engine.can_open(
                    order_value,
                    self.total_capital,
                    self.current_invested
                )
            )

            if allowed:

                return {
                    "allowed": True,
                    "status": "CONTROLLED",
                    "reason": None
                }

            return {
                "allowed": False,
                "status": "REJECTED",
                "reason": "PORTFOLIO RISK LIMIT"
            }

        except Exception as error:

            return {
                "allowed": False,
                "status": "REJECTED",
                "reason": (
                    "PORTFOLIO RISK ERROR: "
                    + str(error)
                )
            }

    # -------------------------------------------------
    # Build one trade plan
    # -------------------------------------------------

    def build_plan(
        self,
        result
    ):

        if not isinstance(
            result,
            dict
        ):

            return None

        symbol = result.get(
            "symbol"
        )

        if symbol is None:

            return None

        base_score = self._number(
            result.get(
                "base_score",
                result.get(
                    "score",
                    0
                )
            )
        )

        adjusted_score = self._number(
            result.get(
                "regime_adjusted_score",
                result.get(
                    "score",
                    base_score
                )
            )
        )

        candidate_score = self._number(
            result.get(
                "candidate_score",
                result.get(
                    "candidate",
                    0
                )
            )
        )

        risk_score = self._number(
            result.get(
                "risk_score",
                0
            )
        )

        risk_reward = self._number(
            result.get(
                "risk_reward",
                result.get(
                    "risk_reward_ratio",
                    0
                )
            )
        )

        allocation = self._number(
            result.get(
                "allocation",
                result.get(
                    "allocation_percent",
                    0
                )
            )
        )

        capital = self._number(
            result.get(
                "capital",
                result.get(
                    "allocated_capital",
                    0
                )
            )
        )

        price = self._number(
            result.get(
                "price",
                result.get(
                    "entry_price",
                    0
                )
            )
        )

        quantity = self._number(
            result.get(
                "quantity",
                0
            )
        )

        order_value = self._number(
            result.get(
                "order_value",
                quantity * price
            )
        )

        regime = result.get(
            "market_regime",
            result.get(
                "regime",
                "UNKNOWN"
            )
        )

        regime_score = self._number(
            result.get(
                "market_regime_score",
                result.get(
                    "regime_score",
                    0
                )
            )
        )

        signal = result.get(
            "signal",
            "IGNORE"
        )

        risk_status = result.get(
            "risk_status",
            result.get(
                "risk",
                "UNKNOWN"
            )
        )

        validation = result.get(
            "validation_status",
            result.get(
                "validation",
                "UNKNOWN"
            )
        )

        decision = result.get(
            "decision",
            "IGNORE"
        )

        # -------------------------------------------------
        # Portfolio Risk
        # -------------------------------------------------

        portfolio_risk = (
            self._portfolio_risk_check(
                order_value,
                result
            )
        )

        # -------------------------------------------------
        # Final status
        # -------------------------------------------------

        final_status = self._determine_status(

            signal=signal,

            decision=decision,

            risk_status=risk_status,

            validation=validation,

            quantity=quantity,

            order_value=order_value,

            portfolio_risk_allowed=(
                portfolio_risk[
                    "allowed"
                ]
            )

        )

        plan = {

            "symbol": symbol,

            "market_regime": regime,

            "market_regime_score": round(
                regime_score,
                2
            ),

            "base_score": round(
                base_score,
                2
            ),

            "regime_adjusted_score": round(
                adjusted_score,
                2
            ),

            "candidate_score": round(
                candidate_score,
                2
            ),

            "signal": signal,

            "decision": decision,

            "risk_status": risk_status,

            "risk_score": round(
                risk_score,
                2
            ),

            "risk_reward": round(
                risk_reward,
                2
            ),

            "allocation_percent": round(
                allocation,
                2
            ),

            "capital": round(
                capital,
                2
            ),

            "entry_price": round(
                price,
                2
            ),

            "quantity": int(
                quantity
            ),

            "order_value": round(
                order_value,
                2
            ),

            "validation_status": validation,

            "portfolio_risk_status": (
                portfolio_risk[
                    "status"
                ]
            ),

            "portfolio_risk_reason": (
                portfolio_risk[
                    "reason"
                ]
            ),

            "final_status": final_status

        }

        return plan

    # -------------------------------------------------
    # Determine final status
    # -------------------------------------------------

    def _determine_status(
        self,
        signal,
        decision,
        risk_status,
        validation,
        quantity,
        order_value,
        portfolio_risk_allowed=True
    ):

        if validation not in (
            "READY",
            "VALID",
            "PASSED"
        ):

            return "REJECTED"

        if risk_status in (
            "HIGH RISK",
            "EXTREME RISK"
        ):

            return "REJECTED"

        if not portfolio_risk_allowed:

            return "REJECTED"

        if signal not in (
            "BUY",
            "STRONG BUY"
        ):

            return "NOT ACTIONABLE"

        if decision not in (
            "WATCH",
            "STRONG WATCH"
        ):

            return "NOT ACTIONABLE"

        if quantity <= 0:

            return "REJECTED"

        if order_value <= 0:

            return "REJECTED"

        return "READY"

    # -------------------------------------------------
    # Build multiple plans
    # -------------------------------------------------

    def build(
        self,
        results,
        current_invested=None
    ):

        self.plans = []

        if not isinstance(
            results,
            list
        ):

            return []

        if current_invested is not None:

            self.current_invested = (
                self._number(
                    current_invested
                )
            )

        for result in results:

            plan = self.build_plan(
                result
            )

            if plan is not None:

                self.plans.append(
                    plan
                )

        return list(
            self.plans
        )

    # -------------------------------------------------
    # Get plans
    # -------------------------------------------------

    def get_plans(self):

        return list(
            self.plans
        )

    # -------------------------------------------------
    # Get ready plans
    # -------------------------------------------------

    def get_ready_plans(self):

        return [

            plan

            for plan in self.plans

            if plan.get(
                "final_status"
            ) == "READY"

        ]

    # -------------------------------------------------
    # Get rejected plans
    # -------------------------------------------------

    def get_rejected_plans(self):

        return [

            plan

            for plan in self.plans

            if plan.get(
                "final_status"
            ) == "REJECTED"

        ]

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        ready = len(
            self.get_ready_plans()
        )

        rejected = len(
            self.get_rejected_plans()
        )

        not_actionable = len(
            [
                plan
                for plan in self.plans
                if plan.get(
                    "final_status"
                ) == "NOT ACTIONABLE"
            ]
        )

        return {

            "total_plans": len(
                self.plans
            ),

            "ready": ready,

            "rejected": rejected,

            "not_actionable": (
                not_actionable
            )

        }