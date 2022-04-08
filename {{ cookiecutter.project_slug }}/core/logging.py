import logging
import os
import time
from typing import Optional

import dis_snek.client.const as dis_snek_const


class CustomLogger:
    """Log all errors to a file, and log all logging events to console"""

    def __init__(self):
        self.formatter = logging.Formatter(
            "%(asctime)s UTC || %(levelname)s || %(message)s"
        )
        self.formatter.converter = time.gmtime

    def make_logger(self, log_name: str):
        logger = logging.getLogger(log_name)

        # log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(logging.DEBUG)

        # log to file
        file_handler = MakeFileHandler(
            filename=f"./logs/{log_name}.log",
            encoding="utf-8",
        )
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(logging.ERROR)

        # add bother handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)


class MakeFileHandler(logging.FileHandler):
    """Subclass of logging.FileHandler which makes sure the folder is created"""

    def __init__(
        self,
        filename: str,
        mode: str = "a",
        encoding: Optional[str] = None,
        delay: bool = False,
    ):
        # create the folder if it does not exist already
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)


def init_logging():
    # Initialize formatter
    logger = CustomLogger()

    # Initialize logging for exceptions
    logger_name = os.getenv("LOGGER_NAME")
    logger.make_logger(logger_name)

    # tell dis-snek to log with this logger
    dis_snek_const.logger_name = logger_name
