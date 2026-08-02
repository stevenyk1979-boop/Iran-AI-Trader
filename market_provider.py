"""
Iran AI Trader Professional
Market Provider Interface
"""

from abc import ABC
from abc import abstractmethod


class MarketProvider(ABC):

    @abstractmethod
    def get_symbols(self):
        """
        Return market symbols.

        Example:

        [
            {
                "symbol": "...",
                "file": "..."
            }
        ]
        """
        pass

    @abstractmethod
    def get_history(self, symbol):
        """
        Return historical candles.
        """
        pass

    @abstractmethod
    def is_available(self):
        """
        Check provider status.
        """
        pass