"""
Iran AI Trader Professional
Watch List Engine
Sprint28-A
"""

import json
import os
from datetime import datetime


class WatchList:

    def __init__(

        self,

        filename="watchlist.json"

    ):

        self.filename = filename

        self.items = []

        self.load()


    # -------------------------------------

    def load(self):

        """
        Load watch list
        """

        if os.path.exists(self.filename):

            try:

                with open(

                    self.filename,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.items = json.load(file)


            except Exception:

                self.items = []


    # -------------------------------------

    def save(self):

        """
        Save watch list
        """

        with open(

            self.filename,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.items,

                file,

                ensure_ascii=False,

                indent=4

            )


    # -------------------------------------

    def add(

        self,

        symbol,

        score,

        signal,

        reasons=None

    ):

        """
        Add symbol to watch list
        """


        item = {

            "symbol": symbol,

            "score": round(score, 2),

            "signal": signal,

            "status": "WATCH",

            "added_date": str(

                datetime.now()

            ),

            "reasons": reasons or []

        }


        self.items.append(item)


        self.save()



    # -------------------------------------

    def remove(

        self,

        symbol

    ):

        """
        Remove symbol
        """


        self.items = [

            x for x in self.items

            if x["symbol"] != symbol

        ]


        self.save()



    # -------------------------------------

    def all(self):

        """
        Return watch list
        """

        return self.items



    # -------------------------------------

    def exists(

        self,

        symbol

    ):

        return any(

            x["symbol"] == symbol

            for x in self.items

        )