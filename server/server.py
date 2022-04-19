# pylint: disable=R0903
'''SLib Flask server.'''
from flask import Flask

from slib.config import SConfig

from server.error.handler import handler
from server.example.api import example

class SServer():
    '''Logging with default settings.'''

    @staticmethod
    def init(debug=False):
        '''Intialize flask server.'''

        host = SConfig.get_str_conf('http_server_host')
        port = SConfig.get_str_conf('http_server_port')

        app = Flask(__name__)
        app.env = 'development'

        app.register_blueprint(handler)

        # Register your server endpoint module here.
        app.register_blueprint(example)

        app.run(host=host, port=port, debug=debug)
