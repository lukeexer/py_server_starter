# pylint: disable=W0703
"""Server entry point."""
import traceback

from flask import Flask

from slib.init import SInit
from slib.log import SLog
from slib.sqlite import SSqlite
from slib.config import SConfig

from server.error.handler import handler
from server.example.api import example

def create_db():
    '''Create database.'''
    pass

# Create app instance here for GUnicorn execution.
app = Flask(__name__)

try:
    SInit.init(log_all_conf=False)

    create_db()

    # Intialize flask server.
    host = SConfig.get_str_conf('http_server_host')
    port = SConfig.get_str_conf('http_server_port')

    app.env = 'development'

    app.register_blueprint(handler)

    # Register your server endpoint module here.
    app.register_blueprint(example)

    if __name__ == "__main__":
        app.run(host=host, port=port, debug=False)

except Exception as e:
    SLog.error(e)
    SLog.error(traceback.format_exc())

    print(e)
    print(traceback.format_exc())
