
"""
Iran AI Trader Professional

Scanner V2

Sprint46-07

Final Risk Gate Engine

Final safety gate before an order can become
an approved executable order.

No broker connection.
No real order execution.
"""


class FinalRiskGateEngine:

    # -------------------------------------------------
    # Constructor
    # -------------------------------------------------

    def __init__(self):

        self.approved = []
        self.warning = []
        self.blocked = []

    # -------------------------------------------------
    # Safe number
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
    # Evaluate one plan
    # -------------------------------------------------

    def evaluate(
        self,
        trade_plan,
        portfolio_risk=None,
        risk_decision=None
    ):

        if not isinstance(
            trade_plan,
            dict
        ):

            return {

                "symbol": "UNKNOWN",

                "decision": "BLOCK",

                "reason":
                    "INVALID_TRADE_PLAN"

            }

        symbol = trade_plan.get(
            "symbol",
            "UNKNOWN"
        )

        # -------------------------------------------------
        # Trade plan status
        # -------------------------------------------------

        plan_status = trade_plan.get(
            "final_status",
            trade_plan.get(
                "status",
                "UNKNOWN"
            )
        )

        if plan_status != "READY":

            return {

                "symbol": symbol,

                "decision": "BLOCK",

                "reason":
                    "TRADE_PLAN_NOT_READY"

            }

        # -------------------------------------------------
        # Portfolio risk
        # -------------------------------------------------

        if isinstance(
            portfolio_risk,
            dict
        ):

            portfolio_status = (
                portfolio_risk.get(
                    "status",
                    "INVALID"
                )
            )

            if portfolio_status not in (
                "CONTROLLED",
            ):

                return {

                    "symbol": symbol,

                    "decision": "BLOCK",

                    "reason":
                        "PORTFOLIO_RISK_" +
                        str(
                            portfolio_status
                        )

                }

        # -------------------------------------------------
        # Risk decision
        # -------------------------------------------------

        if isinstance(
            risk_decision,
            dict
        ):

            decision = risk_decision.get(
                "decision",
                "BLOCK"
            )

            reason = risk_decision.get(
                "reason",
                "UNKNOWN_RISK_DECISION"
            )

            if decision == "BLOCK":

                return {

                    "symbol": symbol,

                    "decision": "BLOCK",

                    "reason": reason

                }

            if decision == "ALLOW_WITH_WARNING":

                return {

                    "symbol": symbol,

                    "decision":
                        "ALLOW_WITH_WARNING",

                    "reason": reason

                }

        # -------------------------------------------------
        # Quantity
        # -------------------------------------------------

        quantity = int(
            self._number(
                trade_plan.get(
                    "quantity",
                    0
                )
            )
        )

        if quantity <= 0:

            return {

                "symbol": symbol,

                "decision": "BLOCK",

                "reason":
                    "INVALID_QUANTITY"

            }

        # -------------------------------------------------
        # Order value
        # -------------------------------------------------

        order_value = self._number(
            trade_plan.get(
                "order_value",
                0
            )
        )

        if order_value <= 0:

            return {

                "symbol": symbol,

                "decision": "BLOCK",

                "reason":
                    "INVALID_ORDER_VALUE"

            }

        # -------------------------------------------------
        # Approved
        # -------------------------------------------------

        return {

            "symbol": symbol,

            "decision": "ALLOW",

            "reason":
                "ALL_RISK_CHECKS_PASSED"

        }

    # -------------------------------------------------
    # Evaluate all
    # -------------------------------------------------

    def evaluate_all(
        self,
        trade_plans,
        portfolio_risk=None,
        risk_decisions=None
    ):

        self.approved = []
        self.warning = []
        self.blocked = []

        if not isinstance(
            trade_plans,
            list
        ):

            return []

        if not isinstance(
            risk_decisions,
            list
        ):

            risk_decisions = []

        decisions = []

        for index, plan in enumerate(
            trade_plans
        ):

            risk_decision = None

            if index < len(
                risk_decisions
            ):

                risk_decision = (
                    risk_decisions[index]
                )

            result = self.evaluate(
                plan,
                portfolio_risk,
                risk_decision
            )

            decisions.append(
                result
            )

            decision = result.get(
                "decision"
            )

            if decision == "ALLOW":

                self.approved.append(
                    result
                )

            elif decision == "ALLOW_WITH_WARNING":

                self.warning.append(
                    result
                )

            else:

                self.blocked.append(
                    result
                )

        return decisions

    # -------------------------------------------------
    # Get approved
    # -------------------------------------------------

    def get_approved(self):

        return list(
            self.approved
        )

    # -------------------------------------------------
    # Get warnings
    # -------------------------------------------------

    def get_warning(self):

        return list(
            self.warning
        )

    # -------------------------------------------------
    # Get blocked
    # -------------------------------------------------

    def get_blocked(self):

        return list(
            self.blocked
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {

            "approved":
                len(
                    self.approved
                ),

            "warning":
                len(
                    self.warning
                ),

            "blocked":
                len(
                    self.blocked
                ),

            "total":
                (
                    len(self.approved)
                    +
                    len(self.warning)
                    +
                    len(self.blocked)
                )

        }

