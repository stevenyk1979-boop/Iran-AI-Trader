from decision_engine import DecisionEngine


engine = DecisionEngine()


engines = {

    "trend": {

        "score": 20,

        "max_score": 20,

        "reason": [

            "Strong Trend"

        ]

    },


    "momentum": {

        "score": 20,

        "max_score": 20,

        "reason": [

            "Strong Momentum"

        ]

    },


    "volume": {

        "score": 25,

        "max_score": 25,

        "reason": [

            "High Volume"

        ]

    }

}


risk = {

    "risk": 15

}


result = engine.decide(

    "فملی",

    engines,

    risk

)


print(result.summary())