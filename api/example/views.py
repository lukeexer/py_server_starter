"Example API module."
from flask import Blueprint

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
