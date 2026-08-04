"""
Iran AI Trader Professional
Sector Engine Test
Sprint33-B
"""


from sector_engine import SectorEngine
from sector_report import SectorReport



def main():


    decisions = [


        {
            "symbol": "چکارن",
            "score": 96.43,
            "sector": "Food"
        },


        {
            "symbol": "ولملت",
            "score": 91,
            "sector": "Leasing"
        },


        {
            "symbol": "دزاگرس",
            "score": 88,
            "sector": "Petro"
        },


        {
            "symbol": "وبملت",
            "score": 85,
            "sector": "Banking"
        }


    ]



    engine = SectorEngine()


    result = engine.analyze(

        decisions

    )


    report = SectorReport()


    report.show(

        result

    )



if __name__ == "__main__":

    main()