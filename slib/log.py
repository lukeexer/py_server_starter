# pylint: disable=W0603
'''Logging share library.'''
import logging
from logging.handlers import TimedRotatingFileHandler
from enum import Enum

SLOG_LOGGER = None
SLOG_AMOUNT_OF_KEEPED_LOG_FILE = 7

SLOG_FILE_PATH = 'log/'
SLOG_FILE_NAME = 'system.log'

class SLogLevel(Enum):
    '''Define logging level Enumerations.'''

    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4

class SLog():
    '''Logging with default settings.'''

    @staticmethod
    def init(level = SLogLevel.INFO):
        '''intialize the logging system.'''

        global SLOG_LOGGER

        # format the log record
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        full_path = SLOG_FILE_PATH + SLOG_FILE_NAME
        handler = TimedRotatingFileHandler(full_path,
                                            when='midnight',
                                            backupCount=SLOG_AMOUNT_OF_KEEPED_LOG_FILE)
        handler.setFormatter(formatter)

        SLOG_LOGGER = logging.getLogger(__name__)
        SLOG_LOGGER.addHandler(handler)

        # The default logging level is INFO
        SLog.set_level(level)

    @staticmethod
    def set_level(level = SLogLevel.INFO):
        '''Set logging level.'''

        if level == SLogLevel.ERROR:
            SLOG_LOGGER.setLevel(logging.ERROR)
        elif level == SLogLevel.WARNING:
            SLOG_LOGGER.setLevel(logging.WARNING)
        elif level == SLogLevel.INFO:
            SLOG_LOGGER.setLevel(logging.INFO)
        else:
            SLOG_LOGGER.setLevel(logging.DEBUG)

    @staticmethod
    def debug(msg):
        '''Log debug level message.'''
        SLOG_LOGGER.debug(msg)

    @staticmethod
    def info(msg):
        '''Log info level message.'''
        SLOG_LOGGER.info(msg)

    @staticmethod
    def warning(msg):
        '''Log warning level message.'''
        SLOG_LOGGER.warning(msg)

    @staticmethod
    def error(msg):
        '''Log error level message.'''
        SLOG_LOGGER.error(msg)
    