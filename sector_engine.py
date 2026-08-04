"""
Iran AI Trader Professional
Sector Engine
Sprint33-B
"""


from collections import defaultdict

from sector_config import MAX_SECTOR_EXPOSURE



class SectorEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def analyze_sector_distribution(

        self,

        decisions

    ):

        """

        Calculate sector allocation

        """

        sectors = defaultdict(int)



        total_score = 0



        for item in decisions:


            score = item.get(

                "score",

                0

            )


            sector = item.get(

                "sector",

                "Unknown"

            )


            sectors[sector] += score


            total_score += score



        distribution = {}



        for sector, value in sectors.items():


            if total_score > 0:

                distribution[sector] = round(

                    (

                        value /

                        total_score

                    ) * 100,

                    2

                )

            else:

                distribution[sector] = 0



        return distribution



    # -------------------------------------

    def check_concentration(

        self,

        distribution

    ):


        warnings = []



        for sector, percent in distribution.items():


            if percent > MAX_SECTOR_EXPOSURE:


                warnings.append(

                    f"{sector} concentration too high"

                )



        return warnings



    # -------------------------------------

    def analyze(

        self,

        decisions

    ):


        distribution = self.analyze_sector_distribution(

            decisions

        )


        warnings = self.check_concentration(

            distribution

        )



        status = "HEALTHY"


        if warnings:

            status = "WARNING"



        return {


            "distribution": distribution,


            "warnings": warnings,


            "status": status


        }