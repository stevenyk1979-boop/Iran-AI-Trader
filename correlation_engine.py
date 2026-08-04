"""
Iran AI Trader Professional
Correlation Engine
Sprint33-C
"""


import math

from correlation_config import (
    HIGH_CORRELATION_THRESHOLD,
    MIN_HISTORY_LENGTH
)



class CorrelationEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def calculate_correlation(

        self,

        series_a,

        series_b

    ):

        """
        Calculate Pearson correlation
        """


        if (

            len(series_a) < MIN_HISTORY_LENGTH

            or

            len(series_b) < MIN_HISTORY_LENGTH

        ):

            return 0



        n = min(

            len(series_a),

            len(series_b)

        )


        a = series_a[:n]

        b = series_b[:n]



        avg_a = sum(a) / n

        avg_b = sum(b) / n



        numerator = sum(

            (

                a[i] - avg_a

            )

            *

            (

                b[i] - avg_b

            )

            for i in range(n)

        )



        denominator_a = math.sqrt(

            sum(

                (

                    x - avg_a

                ) ** 2

                for x in a

            )

        )


        denominator_b = math.sqrt(

            sum(

                (

                    x - avg_b

                ) ** 2

                for x in b

            )

        )



        denominator = (

            denominator_a *

            denominator_b

        )



        if denominator == 0:

            return 0



        return round(

            numerator / denominator,

            2

        )



    # -------------------------------------

    def classify(

        self,

        correlation

    ):

        """

        Risk classification

        """


        if correlation >= HIGH_CORRELATION_THRESHOLD:

            return "HIGH CORRELATION"


        elif correlation >= 0.50:

            return "MODERATE"



        else:

            return "DIVERSIFIED"



    # -------------------------------------

    def analyze(

        self,

        price_history

    ):

        """

        Analyze all symbol pairs

        """


        symbols = list(

            price_history.keys()

        )


        results = []



        for i in range(

            len(symbols)

        ):


            for j in range(

                i + 1,

                len(symbols)

            ):


                symbol_a = symbols[i]

                symbol_b = symbols[j]



                correlation = self.calculate_correlation(

                    price_history[symbol_a],

                    price_history[symbol_b]

                )



                results.append(

                    {

                        "symbol_a": symbol_a,

                        "symbol_b": symbol_b,

                        "correlation": correlation,

                        "status": self.classify(

                            correlation

                        )

                    }

                )



        warnings = [

            item

            for item in results

            if item["status"]

            ==

            "HIGH CORRELATION"

        ]



        return {


            "pairs_checked": len(results),


            "pairs": results,


            "warnings": warnings


        }