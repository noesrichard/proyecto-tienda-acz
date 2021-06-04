from flask import Flask
import os
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from .DbConnection import DBConnection
from .config import BDConfig


app = Flask(__name__)
db = DBConnection(app)
CORS(app)
auth = HTTPBasicAuth()

if 'CLEARDB_DATABASE_URL' in os.environ:
    from .config import ClearDBConfig
    app.config.from_object(ClearDBConfig)
else:
    app.config.from_object(BDConfig)


def create_app():
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_SORT_KEYS'] = False

    from .catalog.urls import catalog
    app.register_blueprint(catalog)

    from .users.urls import user
    app.register_blueprint(user)

    from .cart.urls import cart
    app.register_blueprint(cart)

    return app
