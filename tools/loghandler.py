import logging
from pathlib import Path


class LoggerHandler:
    def __init__(self, level, logname: str, config: dict):
        self.config = config
        self.level = getattr(logging, level)
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(self.level)
        ch = logging.StreamHandler()
        ch.setLevel(self.level)
        Path(__file__).parents[1]

        formatter_console = logging.Formatter(
            '[%(asctime)s] - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        ch.setFormatter(formatter_console)
        self.logger.addHandler(ch)

    def logging(self):
        return self.logger
