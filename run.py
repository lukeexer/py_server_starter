# pylint: disable=W0703
"""Server entry point."""
import traceback

from flask import Flask

from slib.init import SInit
from slib.log import SLog

from api.example.views import example

if __name__ == "__main__":
    try:
        SInit.init()

        app = Flask(__name__)
        app.env="development"

        app.register_blueprint(example)

        app.run(debug=False)

    except Exception as e:
        SLog.error(e)
        SLog.error(traceback.format_exc())

        print(e)
        print(traceback.format_exc())
