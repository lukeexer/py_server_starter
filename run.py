"""Server entry point."""
from flask import Flask

from slib.init import SInit

from api.example.views import example

if __name__ == "__main__":
    SInit.init()

    app = Flask(__name__)    
    app.env="development"

    app.register_blueprint(example)

    app.run(debug=False)
