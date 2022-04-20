"Example API module."
from flask import Blueprint
from flask import jsonify, abort

from slib.log import SLog

from server.example.service import ExampleService
from server.example.repository import ExampleRepo

example = Blueprint('example', __name__)

@example.route('/', methods=['GET'])
@example.route('/hello', methods=['GET'])
def hello_world():
    '''Hello demo endpoint.'''

    msg = 'Hello to the world of Falsk!'

    SLog.info(msg)

    return msg

@example.route('/show/<key>', methods=['GET'])
def get_message(key):
    '''Get message demo endpoint.'''

    repo = ExampleRepo()
    service = ExampleService(repo)

    msg = None
    msg = service.get_message(key)

    return msg or f'{key} not found!'

@example.route('/json/get', methods=['GET'])
def get_example_json():
    '''Return example data in JSON format.'''

    ret_data = {}
    ret_data['key1'] = 'val1'
    ret_data['key2'] = 'val2'
    ret_data['arr1'] = ['ele1', 'ele2', 'ele3']
    ret_data['dict1'] = {'dkey1': 'dval1', 'dkey2': 'dval2'}

    return jsonify(ret_data), 200

@example.route('/post/example', methods=['POST'])
def post_example_for_method_not_allowed_test():
    '''Post example for method not allowed test.'''

    return jsonify('post data'), 200

@example.route('/error', methods=['GET'])
def entry_point_for_internal_server_error_test():
    '''Entry point for internal server error test.'''

    abort(500)

@example.route('/error/exception', methods=['GET'])
def entry_point_for_unknown_runtime_exception_test():
    '''Entry point for unknown exception test.'''

    abort(409)
