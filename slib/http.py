# pylint: disable=R0903, W0102
'''SServer HTTP Client Library.'''
from http import HTTPStatus
import json
import requests

from slib.log import SLog

class HttpRequestFail(Exception):
    '''Raised when HTTP request fail.'''

class InvalidHttpResponseType(Exception):
    '''Raised when receive invalid HTTP response content type.'''

class InvalidJsonFormat(Exception):
    '''Raised when encountering invalid JSON format.'''

class SHttp():
    '''SServer HTTP Client Utility Functions.'''

    @staticmethod
    def dict_from_json_get(url, param_dict={}, timeout=3):
        '''Get Python dictionary from HTTP GET response JSON.'''

        resp = requests.get(url, params=param_dict, timeout=timeout)

        if resp.status_code != HTTPStatus.OK:
            SLog.error(f'Send request to {url}. and the HTTP response code is not 200.'
                        f' The response code is: {resp.status_code}.')
            raise HttpRequestFail('The HTTP response code is not 200.')

        if 'application/json' not in resp.headers['content-type']:
            SLog.error(f'Send request to {url}. and the HTTP response '
                        f'format is not application/json.')
            raise InvalidHttpResponseType('The HTTP response format is not application/json.')

        ret_dict = {}

        try:
            ret_dict = json.loads(resp.text)
        except Exception:
            SLog.error(f'Send request to {url}, but the replied data '
                        f'can not be converted to dictionary.')
            raise InvalidJsonFormat(
                'Invalid JSON format. Can not be converted to dictionary.') from Exception

        return ret_dict

    @staticmethod
    def dict_from_json_post(url, body_dict={}, timeout=3):
        '''Get Python dictionary from HTTP POST response JSON.'''

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        resp = requests.post(url, data=body_dict, headers=headers, timeout=timeout)

        if resp.status_code != HTTPStatus.OK:
            SLog.error(f'Send request to {url}. and the HTTP response code is not 200.'
                        f' The response code is: {resp.status_code}.')
            raise HttpRequestFail('The HTTP response code is not 200.')

        if 'application/json' not in resp.headers['content-type']:
            SLog.error(f'Send request to {url}. and the HTTP response '
                        f'format is not application/json.')
            raise InvalidHttpResponseType('The HTTP response format is not application/json.')

        ret_dict = {}

        try:
            ret_dict = json.loads(resp.text)
        except Exception:
            SLog.error(f'Send request to {url}, but the replied data '
                        f'can not be converted to dictionary.')
            raise InvalidJsonFormat(
                'Invalid JSON format. Can not be converted to dictionary.') from Exception

        return ret_dict
