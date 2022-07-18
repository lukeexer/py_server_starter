'''Unit test for SValidate library.'''
import unittest

from slib.validate import SCheck
from slib.log import SLog

from slib.validate import InvalidInput

class TestSCeck(unittest.TestCase):
    '''Test case class.'''

    def setUp(self):
        '''Set up function.'''
        SLog.init()

    def test_check_str_with_valid_value(self):
        '''Test valid string.'''

        str_to_be_tested = 'abc'

        ret_val = SCheck.check_str('str_api', 'str_field', str_to_be_tested, 1, 3)

        self.assertEqual(str_to_be_tested, ret_val)

    def test_str_length_greater_than_max_limitation(self):
        '''Test invalid string with the string length greater than min limitation.'''

        str_to_be_tested = 'abcd'

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_api', 'str_field', str_to_be_tested, 1, 3)

    def test_str_length_less_than_min_limitation(self):
        '''Test invalid string with the string length less than min limitation.'''

        str_to_be_tested = 'ab'

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_api', 'str_field', str_to_be_tested, 3, 3)

    def test_check_int_with_valid_value(self):
        '''Test valid integer.'''

        expected_int_val = 10
        int_to_be_tested = '10'

        ret_val = SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10)

        self.assertEqual(expected_int_val, ret_val)

    def test_check_int_value_greater_than_max_limitation(self):
        '''Test invalid integer with the value greater than max limitation.'''

        int_to_be_tested = '11'

        with self.assertRaises(InvalidInput):
            SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10)

    def test_check_int_value_less_than_min_limitation(self):
        '''Test invalid integer with the value less than min limitation.'''

        int_to_be_tested = '-1'

        with self.assertRaises(InvalidInput):
            SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10)

    def test_check_int_with_invalid_string(self):
        '''Test check integer with invalid string value.'''

        int_to_be_tested = 'abc'

        with self.assertRaises(InvalidInput):
            SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10)

    def test_check_int_with_none(self):
        '''Test check integer with none value.'''

        int_to_be_tested = None

        with self.assertRaises(InvalidInput):
            SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10)

    def test_check_str_with_none(self):
        '''Test check string with none value.'''

        str_to_be_tested = None

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_api', 'str_field', str_to_be_tested, 0, 10)

    def test_check_int_without_required_input(self):
        '''Test check integer without required input.'''

        int_to_be_tested = ''

        with self.assertRaises(InvalidInput):
            SCheck.check_int('str_api', 'int_field', int_to_be_tested, 0, 10, required=True)

    def test_check_str_with_required_input(self):
        '''Test check string without required input.'''

        str_to_be_tested = ''

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_api', 'str_field', str_to_be_tested, 0, 10, required=True)

    def test_check_str_regex(self):
        '''Test check string regular expression.'''

        str_to_be_tested = 'A01'
        regex_to_be_tested = '[A-Z][0-9][0-9]'

        ret_str = SCheck.check_str_regex('str_api', 'str_field',
                str_to_be_tested, regex_to_be_tested)

        self.assertEqual(str_to_be_tested, ret_str)

    def test_check_str_regex_with_invalid_input(self):
        '''Test check string regular expresstion with invalid input.'''

        str_to_be_tested = '001'
        regex_to_be_tested = '[A-Z][0-9][0-9]'

        with self.assertRaises(InvalidInput):
            SCheck.check_str_regex('str_api', 'str_field', str_to_be_tested, regex_to_be_tested)
