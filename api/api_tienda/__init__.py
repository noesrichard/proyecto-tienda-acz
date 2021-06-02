from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from .DbConnection import DBConnection
from .config import BDConfig, ClearDBConfig


app = Flask(__name__)
db = DBConnection(app)
CORS(app)
auth = HTTPBasicAuth()

app.config.from_object(ClearDBConfig)


def create_app():
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_SORT_KEYS'] = False

    from .catalog.urls import catalog
    app.register_blueprint(catalog)

    from .users.urls import user
    app.register_blueprint(user)

    return app
