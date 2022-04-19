"Example API module."
from flask import Blueprint
from flask import jsonify

from slib.log import SLog

from server.example.service import ExampleService
from server.example.repository import ExampleRepo

example = Blueprint('example', __name__)

@example.route('/', methods=['GET'])
@example.route('/hello', methods=['GET'])
def hello_world():
    '''Hello demo endpoint.'''

    repo = ExampleRepo()
    service = ExampleService(repo)

    msg = service.get_message('default')

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

@example.route('/get/json', methods=['GET'])
def get_example_json():
    '''Return example data in JSON format.'''
    ret_data = {}
    ret_data['key1'] = 'val1'
    ret_data['key2'] = 'val2'
    ret_data['arr1'] = ['ele1', 'ele2', 'ele3']
    ret_data['dict1'] = {'dkey1': 'dval1', 'dkey2': 'dval2'}

    return jsonify(ret_data)
