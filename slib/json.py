# pylint: disable=R0903
'''SServer JSON Library.'''

class SJson():
    '''SServer JSON Utility Functions.'''

    @staticmethod
    def make_error_json(error_code, error_msg):
        '''Generate API error message in JSON format.'''

        ret_json = {}
        ret_json['code'] = error_code.value
        ret_json['msg'] = error_msg.value

        return ret_json
