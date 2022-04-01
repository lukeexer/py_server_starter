# pylint: disable=C0415
'''Unit test for SValidate library.'''
import unittest
import os

from pathlib import Path

from slib.log import SLog
from slib.log import SLogLevel

class TestSLog(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''

        self.log_file_name = 'test.log'

    def tearDown(self):
        '''Tear down function.'''

        from slib.log import SLOG_LOGGER

        handlers = SLOG_LOGGER.handlers[:]

        for handler in handlers:
            handler.close()
            SLOG_LOGGER.removeHandler(handler)

        os.remove(self.log_file_name)

    def test_log_debug(self):
        '''Make sure the message has been written into the log file.'''

        SLog.init(level=SLogLevel.DEBUG, file=self.log_file_name)

        msg = 'test debug log message.'
        SLog.debug(msg)

        log_content = Path(self.log_file_name).read_text(encoding='utf-8')

        self.assertIn(msg, log_content)

    def test_log_info(self):
        '''Make sure the message has been written into the log file.'''

        SLog.init(level=SLogLevel.INFO, file=self.log_file_name)

        msg = 'test info log message.'
        SLog.info(msg)

        log_content = Path(self.log_file_name).read_text(encoding='utf-8')

        self.assertIn(msg, log_content)

    def test_log_warning(self):
        '''Make sure the message has been written into the log file.'''

        SLog.init(level=SLogLevel.WARNING, file=self.log_file_name)

        msg = 'test warning log message.'
        SLog.warning(msg)

        log_content = Path(self.log_file_name).read_text(encoding='utf-8')

        self.assertIn(msg, log_content)

    def test_log_error(self):
        '''Make sure the message has been written into the log file.'''

        SLog.init(level=SLogLevel.ERROR, file=self.log_file_name)

        msg = 'test error log message.'
        SLog.error(msg)

        log_content = Path(self.log_file_name).read_text(encoding='utf-8')

        self.assertIn(msg, log_content)
