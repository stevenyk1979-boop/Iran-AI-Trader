"""
Iran AI Trader Professional
Score Normalizer
"""


class ScoreNormalizer:

    @staticmethod
    def normalize(value, maximum):

        if maximum <= 0:
            return 0

        value = max(0, value)

        value = min(value, maximum)

        return round(
            value / maximum * 100,
            2
        )