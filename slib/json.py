# pylint: disable=R0903
'''SServer JSON Library.'''
from flask import jsonify

class SJson():
    '''SServer JSON Utility Functions.'''

    @staticmethod
    def make_error_json(error_code, error_msg):
        '''Generate API error message in JSON format.'''

        json = {}
        json['code'] = error_code.value
        json['msg'] = error_msg.value

        return jsonify(json)
