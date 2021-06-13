from flask import Blueprint, request, jsonify
from api_tienda.data_access_object import UserDataAccessObject
from api_tienda.models import User
from api_tienda import auth
from . import app

user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    new_user = User(**data)
    response = app.create_user(new_user)
    return jsonify(response)


@auth.verify_password
def verify_password(username, password):
    client_user = User(username=username, password=password)
    if UserDataAccessObject().exists(client_user):
        return client_user


@user.route('/user/login', methods=['POST'])
@auth.login_required
def login():
    response = {'permission': True}
    return jsonify(response)


@user.route('/user/index', methods=['GET'])
@auth.login_required
def user_data():
    return f"Iniciaste sesion"
