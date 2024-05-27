import logging

logger = logging.getLogger()

class LoggingFormatter(logging.Formatter):
    info_fmt  = "%(levelname)s %(asctime)s: %(message)s"
    err_fmt = "%(levelname)s %(asctime)s: %(module)s %(funcName)s %(message)s"

    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        original_fmt = self._style._fmt
        if record.levelno <= logging.WARNING:
            self._style._fmt = LoggingFormatter.info_fmt
        else:
            self._style._fmt = LoggingFormatter.err_fmt
        result = logging.Formatter.format(self, record)
        self._style._fmt = original_fmt
        return result