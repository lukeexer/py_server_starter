'''Unit test for SJson library.'''
from datetime import datetime
from unittest.mock import patch
from dataclasses import dataclass

import unittest

from enum import Enum
from slib.json import SJson, InvalidJsonFormat

class ErrCode(Enum):
    '''Server error code enumeration definition.'''
    UNKNOWN_ERROR = 'S00001'

class ErrMsg(Enum):
    '''Server error message enumeration definition.'''
    UNKNOWN_ERROR = 'unknown error'

@dataclass
class MockDataClass:
    '''data class mock for testing.'''
    data1: int
    data2: str

class TestSJson(unittest.TestCase):
    '''Test case class.'''

    def test_make_error_json(self):
        '''Test make_error_json function.'''

        expected_dict = {}
        expected_dict['code'] = ErrCode.UNKNOWN_ERROR.value
        expected_dict['msg'] = ErrMsg.UNKNOWN_ERROR.value

        actual_dict = SJson.make_error_dict(ErrCode.UNKNOWN_ERROR, ErrMsg.UNKNOWN_ERROR)

        self.assertEqual(expected_dict, actual_dict)

    def test_make_json(self):
        '''Test make_json function.'''

        expected_json = '''{"key1": "value1", "key2": "value2"}'''

        test_dict = {}
        test_dict['key1'] = 'value1'
        test_dict['key2'] = 'value2'

        actual_json = SJson.make_json(test_dict)

        self.assertEqual(expected_json, actual_json)

    def test_make_json_with_invalid_json_format(self):
        '''Test make_json function with invalid json format.'''

        test_dict = {}
        test_dict['key1'] = 'value1'
        test_dict['key2'] = datetime.now()

        with self.assertRaises(InvalidJsonFormat):
            SJson.make_json(test_dict)


    def test_parse_json(self):
        '''Test parse_json function.'''

        test_json = '''{"key1": "value1", "key2": "value2"}'''

        expected_dict = {}
        expected_dict['key1'] = 'value1'
        expected_dict['key2'] = 'value2'

        actual_dict = SJson.parse_json(test_json)

        self.assertEqual(expected_dict, actual_dict)

    def test_parse_json_with_invalid_json_format(self):
        '''Test parse_json function with invalid json format.'''

        test_json = '''{"key1": "value1",'''

        with self.assertRaises(InvalidJsonFormat):
            SJson.parse_json(test_json)

    def test_make_json_with_vo(self):
        '''Test make_json_with_vo function.'''

        expected_json = '''{"data1": 1, "data2": "test"}'''

        data_class = MockDataClass(1, 'test')
        actual_json = SJson.make_json_with_vo(data_class)

        self.assertEqual(expected_json, actual_json)

    @patch('json.dumps')
    def test_make_json_with_non_dataclass(self, mock_json_dumps):
        '''Test make_json_with_vo function with non-dataclass.'''

        mock_json_dumps.side_effect = InvalidJsonFormat('Invalid JSON format mock')

        non_dataclass = 1

        with self.assertRaises(InvalidJsonFormat):
            SJson.make_json_with_vo(non_dataclass)
