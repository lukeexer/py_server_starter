'''Input validation utilities.'''
from slib.log import SLog

class InvalidInput(Exception):
    '''Rised when input validation fails.'''

class SCheck():
    '''Input validation utilities.'''

    @staticmethod
    def check_str(lebel, string, min_length, max_length):
        '''Check string input.'''

        string = string.strip()

        if len(string) > max_length:
            err_msg = f'[{lebel}]: String length is greater than expectation.'
            SLog.warning(err_msg)
            raise InvalidInput(err_msg)

        if len(string) < min_length:
            err_msg = f'[{lebel}]: String length is less than expectation.'
            SLog.warning(err_msg)
            raise InvalidInput(err_msg)

        return string

    @staticmethod
    def check_int(lebel, string, min_val, max_val):
        '''Check string input.'''

        int_val = 0

        try:
            int_val = int(string)
        except ValueError:
            err_msg = f'[{lebel}]: String can not be converted to integer.'
            SLog.warning(err_msg)
            raise InvalidInput(err_msg) from ValueError

        if int_val > max_val:
            err_msg = f'[{lebel}]: Integer value is greater than expectation.'
            SLog.warning(err_msg)
            raise InvalidInput(err_msg)

        if int_val < min_val:
            err_msg = f'[{lebel}]: Integer value is less than expectation.'
            SLog.warning(err_msg)
            raise InvalidInput(err_msg)

        return int_val
