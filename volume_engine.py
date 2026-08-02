"""
Iran AI Trader Professional
Volume Engine
"""


class VolumeEngine:

    MAX_SCORE = 25


    def average_volume(

        self,

        volumes,

        period=20

    ):

        if len(volumes) < period:

            return None


        return sum(

            volumes[-period:]

        ) / period



    # --------------------------------


    def volume_ratio(

        self,

        volumes,

        period=20

    ):

        avg = self.average_volume(

            volumes,

            period

        )


        if avg is None:

            return 1


        if avg == 0:

            return 1


        return volumes[-1] / avg



    # --------------------------------


    def score(

        self,

        volumes

    ):

        ratio = self.volume_ratio(volumes)

        score = 0

        reason = []


        if ratio >= 3:

            score = 25

            reason.append(

                "Extreme Volume Increase"

            )


        elif ratio >= 2:

            score = 20

            reason.append(

                "Strong Volume Increase"

            )


        elif ratio >= 1.5:

            score = 15

            reason.append(

                "Good Volume"

            )


        elif ratio >= 1.2:

            score = 10

            reason.append(

                "Volume Improving"

            )


        else:

            reason.append(

                "Weak Volume"

            )


        return {

            "score": score,

            "max_score": self.MAX_SCORE,

            "ratio": round(

                ratio,

                2

            ),

            "reason": reason

        }