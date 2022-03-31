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

        ret_val = SCheck.check_str('str_field', str_to_be_tested, 1, 3)

        self.assertEqual(str_to_be_tested, ret_val)

    def test_str_length_greater_than_max_limitation(self):
        '''Test invalid string with the string length greater than min limitation.'''

        str_to_be_tested = 'abcd'

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_field', str_to_be_tested, 1, 3)

    def test_str_length_less_than_min_limitation(self):
        '''Test invalid string with the string length less than min limitation.'''

        str_to_be_tested = 'ab'

        with self.assertRaises(InvalidInput):
            SCheck.check_str('str_field', str_to_be_tested, 3, 3)

    def test_check_int_with_valid_value(self):
        '''Test valid integer.'''

        int_to_be_tested = 10

        ret_val = SCheck.check_int('int_field', int_to_be_tested, 0, 10)

        self.assertEqual(int_to_be_tested, ret_val)

    def test_check_int_value_greater_than_max_limitation(self):
        '''Test invalid integer with the value greater than max limitation.'''

        int_to_be_tested = 11

        with self.assertRaises(InvalidInput):
            SCheck.check_int('int_field', int_to_be_tested, 0, 10)

    def test_check_int_value_less_than_min_limitation(self):
        '''Test invalid integer with the value less than min limitation.'''

        int_to_be_tested = -1

        with self.assertRaises(InvalidInput):
            SCheck.check_int('int_field', int_to_be_tested, 0, 10)

    def test_check_int_with_invalid_string(self):
        '''Test check integer with invalid string value.'''

        int_to_be_tested = 'abc'

        with self.assertRaises(InvalidInput):
            SCheck.check_int('int_field', int_to_be_tested, 0, 10)
