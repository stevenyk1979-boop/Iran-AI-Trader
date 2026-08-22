"""
Iran AI Trader Professional

Scanner V2

Sprint45-08

Portfolio Risk Engine

Controls total portfolio exposure,
single-symbol exposure,
and portfolio risk status.
"""


class PortfolioRiskEngine:

    def __init__(
        self,
        max_portfolio_exposure=0.80,
        max_symbol_exposure=0.20,
        max_high_risk_exposure=0.10
    ):

        self.max_portfolio_exposure = float(
            max_portfolio_exposure
        )

        self.max_symbol_exposure = float(
            max_symbol_exposure
        )

        self.max_high_risk_exposure = float(
            max_high_risk_exposure
        )

    # -------------------------------------------------
    # Evaluate portfolio
    # -------------------------------------------------

    def evaluate(
        self,
        positions,
        total_capital
    ):

        try:

            if positions is None:
                positions = []

            if not isinstance(
                positions,
                list
            ):
                positions = []

            total_capital = float(
                total_capital
            )

            if total_capital <= 0:

                return {
                    "status": "INVALID",
                    "total_capital": total_capital,
                    "invested_capital": 0.0,
                    "portfolio_exposure": 0.0,
                    "available_capital": 0.0,
                    "risk_exposure": 0.0,
                    "positions_count": 0,
                    "symbol_exposures": []
                }

            invested_capital = 0.0
            high_risk_capital = 0.0
            symbol_exposures = []

            for position in positions:

                if not isinstance(
                    position,
                    dict
                ):
                    continue

                value = self._position_value(
                    position
                )

                if value <= 0:
                    continue

                symbol = position.get(
                    "symbol",
                    "UNKNOWN"
                )

                risk_status = position.get(
                    "risk_status",
                    position.get(
                        "risk",
                        "LOW RISK"
                    )
                )

                invested_capital += value

                if risk_status == "HIGH RISK":

                    high_risk_capital += value

                exposure = (
                    value /
                    total_capital
                )

                symbol_exposures.append({

                    "symbol": symbol,

                    "value": round(
                        value,
                        2
                    ),

                    "exposure": round(
                        exposure,
                        4
                    ),

                    "exposure_percent": round(
                        exposure * 100,
                        2
                    ),

                    "risk_status": risk_status

                })

            portfolio_exposure = (
                invested_capital /
                total_capital
            )

            high_risk_exposure = (
                high_risk_capital /
                total_capital
            )

            available_capital = (
                total_capital -
                invested_capital
            )

            status = self._status(
                portfolio_exposure,
                symbol_exposures,
                high_risk_exposure
            )

            return {

                "status": status,

                "total_capital": round(
                    total_capital,
                    2
                ),

                "invested_capital": round(
                    invested_capital,
                    2
                ),

                "available_capital": round(
                    available_capital,
                    2
                ),

                "portfolio_exposure": round(
                    portfolio_exposure,
                    4
                ),

                "portfolio_exposure_percent": round(
                    portfolio_exposure * 100,
                    2
                ),

                "risk_exposure": round(
                    high_risk_exposure,
                    4
                ),

                "risk_exposure_percent": round(
                    high_risk_exposure * 100,
                    2
                ),

                "positions_count": len(
                    symbol_exposures
                ),

                "symbol_exposures":
                    symbol_exposures

            }

        except Exception as error:

            return {

                "status": "INVALID",

                "total_capital": 0.0,

                "invested_capital": 0.0,

                "available_capital": 0.0,

                "portfolio_exposure": 0.0,

                "portfolio_exposure_percent": 0.0,

                "risk_exposure": 0.0,

                "risk_exposure_percent": 0.0,

                "positions_count": 0,

                "symbol_exposures": [],

                "error": str(error)

            }

    # -------------------------------------------------
    # Position value
    # -------------------------------------------------

    def _position_value(
        self,
        position
    ):

        value = position.get(
            "value",
            position.get(
                "capital",
                position.get(
                    "position_value",
                    0
                )
            )
        )

        try:

            return float(
                value
            )

        except Exception:

            quantity = position.get(
                "quantity",
                0
            )

            price = position.get(
                "price",
                position.get(
                    "entry_price",
                    0
                )
            )

            try:

                return (
                    float(quantity) *
                    float(price)
                )

            except Exception:

                return 0.0

    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def _status(
        self,
        portfolio_exposure,
        symbol_exposures,
        high_risk_exposure
    ):

        if (
            portfolio_exposure >
            self.max_portfolio_exposure
        ):

            return "OVEREXPOSED"

        for item in symbol_exposures:

            if (
                item["exposure"] >
                self.max_symbol_exposure
            ):

                return "SYMBOL OVEREXPOSED"

        if (
            high_risk_exposure >
            self.max_high_risk_exposure
        ):

            return "HIGH RISK EXPOSURE"

        return "CONTROLLED"

    # -------------------------------------------------
    # Can open position
    # -------------------------------------------------

    def can_open(
        self,
        position_value,
        total_capital,
        current_invested=0
    ):

        try:

            position_value = float(
                position_value
            )

            total_capital = float(
                total_capital
            )

            current_invested = float(
                current_invested
            )

            if (
                position_value <= 0 or
                total_capital <= 0
            ):

                return False

            projected_exposure = (
                current_invested +
                position_value
            ) / total_capital

            return (
                projected_exposure <=
                self.max_portfolio_exposure
            )

        except Exception:

            return False

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(
        self,
        evaluation
    ):

        if not isinstance(
            evaluation,
            dict
        ):
            return {}

        return {

            "status": evaluation.get(
                "status",
                "INVALID"
            ),

            "positions_count":
                evaluation.get(
                    "positions_count",
                    0
                ),

            "portfolio_exposure_percent":
                evaluation.get(
                    "portfolio_exposure_percent",
                    0.0
                ),

            "risk_exposure_percent":
                evaluation.get(
                    "risk_exposure_percent",
                    0.0
                ),

            "available_capital":
                evaluation.get(
                    "available_capital",
                    0.0
                )

        }