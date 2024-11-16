import logging

# ANSI escape codes for colors
RED = '\033[31m'
RESET = '\033[0m'
YELLOW = '\033[33m'

class CustomFormatter(logging.Formatter):
    """Custom formatter to add colors to log levels."""
    FORMATS = {
        logging.ERROR: RED + '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:%(funcName)s - %(message)s' + RESET,
        logging.WARNING: YELLOW + '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:%(funcName)s - %(message)s' + RESET,
        logging.INFO: '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:%(funcName)s - %(message)s',
        'DEFAULT': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d:%(funcName)s - %(message)s'
    }

    def format(self, record):
        self._style._fmt = self.FORMATS.get(record.levelno, self.FORMATS['DEFAULT'])
        return logging.Formatter.format(self, record)

def setup_logging():
    logger = logging.getLogger('library-logger')
    logger.setLevel(logging.DEBUG)  # Set the minimum level of messages to log
    logger.propagate = False  # Ensure logs do not propagate to the parent logger

    # Clear existing handlers
    logger.handlers = []

    # Create and add new handlers
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = CustomFormatter()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = setup_logging()
