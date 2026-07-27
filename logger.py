"""
Iran AI Trader V2.0
Logging System
"""

import logging
from pathlib import Path

from config import LOG_DIR


class LoggerManager:

    def __init__(self):

        Path(LOG_DIR).mkdir(exist_ok=True)

        self.log_file = Path(LOG_DIR) / "iran_ai_trader.log"

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

    def info(self, message):
        logging.info(message)
        print("[INFO]", message)

    def warning(self, message):
        logging.warning(message)
        print("[WARNING]", message)

    def error(self, message):
        logging.error(message)
        print("[ERROR]", message)