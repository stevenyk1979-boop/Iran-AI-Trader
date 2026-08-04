"""
Iran AI Trader Professional
Pipeline Intelligence Test
Sprint35
"""


from pipeline_intelligence import PipelineIntelligence

from pipeline_intelligence_report import PipelineIntelligenceReport



def main():


    print()

    print("=" * 70)

    print(

        "PIPELINE INTELLIGENCE TEST"

    )

    print("=" * 70)



    candidates = [



        {

            "symbol": "چکارن",

            "score": 94.9,

            "smart_money_score": 100,

            "portfolio_score": 90,

            "risk_score": 80

        },



        {

            "symbol": "ولملت",

            "score": 91,

            "smart_money_score": 85,

            "portfolio_score": 88,

            "risk_score": 75

        },



        {

            "symbol": "دزاگرس",

            "score": 70,

            "smart_money_score": 40,

            "portfolio_score": 65,

            "risk_score": 50

        }

    ]



    intelligence = PipelineIntelligence()



    results = intelligence.analyze_all(

        candidates

    )



    report = PipelineIntelligenceReport()



    report.show(

        results

    )



if __name__ == "__main__":

    main()