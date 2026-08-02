"""
Iran AI Trader Professional
Risk Engine
"""


class RiskEngine:


    def calculate(

        self,

        history,

        period=20

    ):


        prices = history.close_prices()


        if len(prices) < period + 1:

            return {

                "risk": 70,

                "reason": "Not enough recent data"

            }



        recent = prices[-period:]


        changes = []


        for i in range(1, len(recent)):

            change = (

                abs(

                    recent[i] - recent[i-1]

                )

                /

                recent[i-1]

            ) * 100


            changes.append(change)



        if not changes:

            return {

                "risk": 50,

                "reason": "No movement"

            }



        volatility = sum(changes) / len(changes)



        # تبدیل نوسان به Risk 0-100

        risk = min(

            volatility * 5,

            100

        )



        if risk < 30:

            reason = "Low volatility"


        elif risk < 60:

            reason = "Medium volatility"


        else:

            reason = "High volatility"



        return {

            "risk": round(

                risk,

                2

            ),

            "volatility": round(

                volatility,

                2

            ),

            "reason": reason

        }