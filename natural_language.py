"""
Iran AI Trader Professional
Natural Language Generator
"""


class NaturalLanguageGenerator:


    def generate(

        self,

        decision

    ):


        text = []


        if decision.signal == "STRONG BUY":

            text.append(

                "Very strong buying opportunity."

            )


        elif decision.signal == "BUY":

            text.append(

                "Buying opportunity detected."

            )


        elif decision.signal == "HOLD":

            text.append(

                "Wait for better confirmation."

            )


        else:

            text.append(

                "Avoid buying at current conditions."

            )


        if decision.risk < 20:

            text.append(

                "Risk is low."

            )


        elif decision.risk < 40:

            text.append(

                "Risk is moderate."

            )


        else:

            text.append(

                "Risk is high."

            )


        if decision.confidence > 90:

            text.append(

                "AI confidence is very high."

            )


        elif decision.confidence > 70:

            text.append(

                "AI confidence is acceptable."

            )


        else:

            text.append(

                "AI confidence is weak."

            )


        return " ".join(text)