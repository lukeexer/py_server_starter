from flask import Flask

from slib.config import SConfig

from server.example.views import example

class SServer():
    '''Logging with default settings.'''

    @staticmethod
    def init(debug=False):
        '''Intialize flask server.'''

        host = SConfig.get_str_conf('http_server_host')
        port = SConfig.get_str_conf('http_server_port')

        app = Flask(__name__)
        app.env = 'development'

        # Register your server endpoint module here.
        app.register_blueprint(example)

        app.run(host=host, port=port, debug=debug)
