'''Unit test for SHttp library.'''
import unittest
from http import HTTPStatus

import httpretty
from slib.http import SHttp, HttpRequestFail, InvalidJsonFormat, InvalidHttpResponseType

class TestSHttp(unittest.TestCase):
    '''Test case class.'''

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_get(self):
        '''Test dict_from_json_get function.'''

        expected_dict = {'data1': '127.0.0.1', 'data2': 0}

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.GET,
            url,
            adding_headers={'Content-Type': 'application/json'},
            body=json_body
        )

        actual_dict = SHttp.dict_from_json_get(url)

        self.assertEqual(expected_dict, actual_dict)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_get_with_status_500(self):
        '''Test dict_from_json_get function with status code 500.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.GET,
            url,
            adding_headers={'Content-Type': 'application/json'},
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
            body=json_body
        )

        with self.assertRaises(HttpRequestFail):
            SHttp.dict_from_json_get(url)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_get_with_invalid_json_format(self):
        '''Test dict_from_json_get function with invalid JSON format.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0'''

        httpretty.register_uri(
            httpretty.GET,
            url,
            adding_headers={'Content-Type': 'application/json'},
            body=json_body
        )

        with self.assertRaises(InvalidJsonFormat):
            SHttp.dict_from_json_get(url)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_get_with_invalid_content_type(self):
        '''Test dict_from_json_get function with invalid content type.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.GET,
            url,
            adding_headers={'Content-Type': 'text/html'},
            body=json_body
        )

        with self.assertRaises(InvalidHttpResponseType):
            SHttp.dict_from_json_get(url)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_post(self):
        '''Test dict_from_json_post function.'''

        expected_dict = {'data1': '127.0.0.1', 'data2': 0}

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.POST,
            url,
            adding_headers={'Content-Type': 'application/json'},
            body=json_body
        )

        value_1 = 'value_1'
        value_2 = 'value_2'

        req_body = {}
        req_body['key_1'] = value_1
        req_body['key_2'] = value_2

        actual_dict = SHttp.dict_from_json_post(url, req_body)

        self.assertTrue(value_1 in httpretty.last_request().body.decode('utf-8'))
        self.assertTrue(value_2 in httpretty.last_request().body.decode('utf-8'))

        self.assertEqual(expected_dict, actual_dict)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_post_with_status_500(self):
        '''Test dict_from_json_post function with status code 500.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.POST,
            url,
            adding_headers={'Content-Type': 'application/json'},
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
            body=json_body
        )

        with self.assertRaises(HttpRequestFail):
            SHttp.dict_from_json_post(url)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_post_with_invalid_json_format(self):
        '''Test dict_from_json_post function with invalid JSON format.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0'''

        httpretty.register_uri(
            httpretty.POST,
            url,
            adding_headers={'Content-Type': 'application/json'},
            body=json_body
        )

        with self.assertRaises(InvalidJsonFormat):
            SHttp.dict_from_json_post(url)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_dict_from_json_post_with_invalid_content_type(self):
        '''Test dict_from_json_get function with invalid content type.'''

        url = 'http://test.org/path'
        json_body = '''{"data1": "127.0.0.1", "data2": 0}'''

        httpretty.register_uri(
            httpretty.POST,
            url,
            adding_headers={'Content-Type': 'text/html'},
            body=json_body
        )

        with self.assertRaises(InvalidHttpResponseType):
            SHttp.dict_from_json_post(url)
