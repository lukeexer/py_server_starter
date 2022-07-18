# pylint: disable=R0913
'''Input validation utilities.'''
import re

class InvalidInput(Exception):
    '''Raised when input validation fails.'''

class SCheck():
    '''Input validation utilities.'''

    @staticmethod
    def check_str_regex(api_name, field_name, string, regex):
        '''Throw invalid input exception.'''

        matched = re.search(regex, string)

        if matched is None:
            err_msg = f'[{api_name} {field_name}]: Received field input is None.'
            raise InvalidInput(err_msg)

        return string

    @staticmethod
    def check_str(api_name, field_name, string, min_length, max_length, required=True):
        '''Check string input.'''

        if string is None:
            err_msg = f'[{api_name} {field_name}]: Received field input is None.'
            raise InvalidInput(err_msg)

        string = string.strip()

        if required is True:
            if SCheck.check_empty(string) is True:
                err_msg = f'[{api_name} {field_name}]: Input is required.'
                raise InvalidInput(err_msg)

        if len(string) > max_length:
            err_msg = f'[{api_name} {field_name}]: String length is greater than expectation. ' \
                'The input value is: {string}'
            raise InvalidInput(err_msg)

        if len(string) < min_length:
            err_msg = f'[{api_name} {field_name}]: String length is less than expectation.' \
                'The input value is: {string}.'
            raise InvalidInput(err_msg)

        return string

    @staticmethod
    def check_int(api_name, field_name, string, min_val, max_val, required=True):
        '''Check integer input in string format.'''

        if string is None:
            err_msg = f'[{api_name} {field_name}]: Received field input is None.'
            raise InvalidInput(err_msg)

        string = string.strip()

        if required is True:
            if SCheck.check_empty(string) is True:
                err_msg = f'[{api_name} {field_name}]: Input is required.'
                raise InvalidInput(err_msg)

        int_val = 0

        try:
            int_val = int(string)
        except ValueError:
            err_msg = f'[{api_name} {field_name}]: String can not be converted to integer. ' \
                f'The input value is: {string}.'
            raise InvalidInput(err_msg) from ValueError

        if int_val > max_val:
            err_msg = f'[{api_name} {field_name}]: Integer value is greater than expectation. ' \
                f'The input value is: {string}.'
            raise InvalidInput(err_msg)

        if int_val < min_val:
            err_msg = f'[{api_name} {field_name}]: Integer value is less than expectation. ' \
                f'The input value is: {string}.'
            raise InvalidInput(err_msg)

        return int_val

    @staticmethod
    def check_empty(string):
        '''Check empty string.'''
        string = string.strip()

        if len(string) == 0 or string == '':
            return True

        return False
