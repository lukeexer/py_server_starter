'''Unit test for SJson library.'''
import unittest

from enum import Enum
from slib.json import SJson

class ErrCode(Enum):
    '''Server error code enumeration definition.'''
    UNKNOWN_ERROR = 'S00001'

class ErrMsg(Enum):
    '''Server error message enumeration definition.'''
    UNKNOWN_ERROR = 'unknown error'

class TestSJson(unittest.TestCase):
    '''Test case class.'''

    def test_make_error_json(self):
        '''Test make_error_json function.'''

        expected_dict = {}
        expected_dict['code'] = ErrCode.UNKNOWN_ERROR.value
        expected_dict['msg'] = ErrMsg.UNKNOWN_ERROR.value

        actual_dict = SJson.make_error_json(ErrCode.UNKNOWN_ERROR, ErrMsg.UNKNOWN_ERROR)

        self.assertEqual(expected_dict, actual_dict)
