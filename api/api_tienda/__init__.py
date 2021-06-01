from flask import Flask
from flask_cors import CORS, cross_origin
from .DbConnection import DBConnection
from .config import BDConfig, ClearDBConfig

app = Flask(__name__)
app.config.from_object(ClearDBConfig)
db = DBConnection(app)
CORS(app)


def create_app():
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    from .catalog.urls import catalog

    app.register_blueprint(catalog)

    return app
