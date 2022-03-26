"Example API module."
from flask import Blueprint
from flask import jsonify

from api.example.modules import MESSAGES

example = Blueprint('example', __name__)

@example.route('/')
@example.route('/hello')
def hello_world():
    '''Hello demo endpoint.'''

    return MESSAGES['default']

@example.route('/show/<key>')
def get_message(key):
    '''Get message demo endpoint.'''

    return MESSAGES.get(key) or f'{key} not found!'

@example.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    '''Update demo endpoint.'''

    MESSAGES[key] = message
    return f'{key} Added/Updated'

@example.route('/get/json')
def get_example_json():
    '''Return example data in JSON format.'''
    ret_data = {}
    ret_data['key1'] = 'val1'
    ret_data['key2'] = 'val2'
    ret_data['arr1'] = ['ele1', 'ele2', 'ele3']
    ret_data['dict1'] = {'dkey1': 'dval1', 'dkey2': 'dval2'}

    return jsonify(ret_data)
