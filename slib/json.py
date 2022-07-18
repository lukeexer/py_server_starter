# pylint: disable=R0903
'''SServer JSON Library.'''

import json
import dataclasses

class InvalidJsonFormat(Exception):
    '''Raised when encountering invalid JSON format.'''

class EnhancedJSONEncoder(json.JSONEncoder):
    '''Define value object converting encoder.'''
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

class SJson():
    '''SServer JSON Utility Functions.'''

    @staticmethod
    def make_json(json_dict):
        '''Translate Python dictionary data structure into JSON string.'''

        json_str = ''

        try:
            json_str = json.dumps(json_dict)
        except Exception:
            raise InvalidJsonFormat(
                'Invalid dictionary format. Can not be converted to JSON.') from Exception

        return json_str

    @staticmethod
    def make_json_with_vo(value_object):
        '''Translate value object into JSON string.'''

        json_str = ''

        try:
            json_str = json.dumps(value_object, cls=EnhancedJSONEncoder)
        except Exception:
            raise InvalidJsonFormat(
                'Invalid dataclass format. Can not be converted to JSON.') from Exception

        return json_str

    @staticmethod
    def parse_json(json_str):
        '''Parse JSON string and translates it into Python dictionary data ctructure.'''

        ret_dict = {}

        try:
            ret_dict = json.loads(json_str)
        except Exception:
            raise InvalidJsonFormat(
                'Invalid JSON format. Can not be converted to dictionary.') from Exception

        return ret_dict

    @staticmethod
    def make_error_dict(error_code, error_msg):
        '''Create API error message dictionary for JSON generation.'''

        ret_dict = {}
        ret_dict['code'] = error_code.value
        ret_dict['msg'] = error_msg.value

        return ret_dict

    @staticmethod
    def make_ok_dict(ok_msg):
        '''Create API ok message dictionary for JSON generation.'''

        ret_dict = {}
        ret_dict['msg'] = ok_msg

        return ret_dict
