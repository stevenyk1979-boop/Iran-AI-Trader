"""
Iran AI Trader Professional
Pipeline Intelligence
Sprint35
"""


from pipeline_brain_adapter import PipelineBrainAdapter

from portfolio_brain import PortfolioBrain



class PipelineIntelligence:


    def __init__(self):


        self.adapter = PipelineBrainAdapter()


        self.brain = PortfolioBrain()



    # -------------------------------------

    def analyze_candidate(

        self,

        candidate

    ):

        """
        Analyze single candidate
        """


        data = self.adapter.adapt(

            candidate

        )


        return self.brain.analyze(

            data

        )



    # -------------------------------------

    def analyze_all(

        self,

        candidates

    ):

        """
        Analyze all pipeline candidates
        """


        results = []



        for candidate in candidates:


            result = self.analyze_candidate(

                candidate

            )


            results.append(

                result

            )



        results.sort(

            key=lambda x: x.get(

                "final_ai_score",

                0

            ),

            reverse=True

        )



        return results



    # -------------------------------------

    def approved_only(

        self,

        results

    ):

        """
        Return approved opportunities
        """


        return [

            item

            for item in results

            if item.get(

                "decision"

            )

            ==

            "APPROVED BUY"

        ]