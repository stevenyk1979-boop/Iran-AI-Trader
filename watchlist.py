"""
Iran AI Trader Professional
Watch List Engine
Sprint29-D Professional
"""

import json
import os
from datetime import datetime


class WatchList:

    def __init__(self, filename="watchlist.json"):

        self.filename = filename
        self.items = []

        self.load()

    # ------------------------------------------------

    def load(self):

        if os.path.exists(self.filename):

            try:

                with open(
                    self.filename,
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.items = json.load(f)

            except Exception:

                self.items = []

        else:

            self.items = []

    # ------------------------------------------------

    def save(self):

        with open(
            self.filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.items,
                f,
                ensure_ascii=False,
                indent=4
            )

    # ------------------------------------------------

    def exists(self, symbol):

        return any(
            x["symbol"] == symbol
            for x in self.items
        )

    # ------------------------------------------------

    def determine_status(self, score):

        if score >= 85:

            return "READY TO BUY"

        elif score >= 70:

            return "WATCH"

        else:

            return "REJECT"

    # ------------------------------------------------

    def add(

        self,

        symbol,

        score,

        signal,

        reasons=None

    ):

        if self.exists(symbol):

            return False

        status = self.determine_status(score)

        item = {

            "symbol": symbol,

            "score": round(score, 2),

            "signal": signal,

            "status": status,

            "added_date": str(datetime.now()),

            "reasons": reasons or []

        }

        self.items.append(item)

        self.sort()

        self.save()

        return True

    # ------------------------------------------------

    def update(

        self,

        symbol,

        score,

        signal,

        reasons=None

    ):

        for item in self.items:

            if item["symbol"] == symbol:

                item["score"] = round(score, 2)

                item["signal"] = signal

                item["status"] = self.determine_status(score)

                item["reasons"] = reasons or []

                item["updated_date"] = str(datetime.now())

                self.sort()

                self.save()

                return True

        return self.add(

            symbol,

            score,

            signal,

            reasons

        )

    # ------------------------------------------------

    def remove(self, symbol):

        self.items = [

            x

            for x in self.items

            if x["symbol"] != symbol

        ]

        self.save()

    # ------------------------------------------------

    def sort(self):

        self.items.sort(

            key=lambda x: x["score"],

            reverse=True

        )

    # ------------------------------------------------

    def count(self):

        return len(self.items)

    # ------------------------------------------------

    def top(self, limit=10):

        return self.items[:limit]

    # ------------------------------------------------

    def all(self):

        return self.items

    # ------------------------------------------------

    def ready(self):

        return [

            x

            for x in self.items

            if x["status"] == "READY TO BUY"

        ]

    # ------------------------------------------------

    def watch(self):

        return [

            x

            for x in self.items

            if x["status"] == "WATCH"

        ]

    # ------------------------------------------------

    def rejected(self):

        return [

            x

            for x in self.items

            if x["status"] == "REJECT"

        ]

    # ------------------------------------------------

    def clear(self):

        self.items = []

        self.save()