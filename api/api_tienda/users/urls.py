from flask import Blueprint, request, jsonify
from .utils import verify_registration_data
from api_tienda.DAO import UserDAO
from api_tienda.entities import User
from api_tienda import auth
from flask_cors import cross_origin

user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    if verify_registration_data(data) != "":
        return verify_registration_data(data)
    UserDAO(user=User(**data)).save()
    return "200 OK POST"


@auth.verify_password
def verify_password(username, password):
    user = UserDAO(User(ema_user=username, pas_user=password))
    if user.is_valid():
        return user.get_user()


@user.route('/user/login', methods=['POST'])
def login():
    permission = {'permission': False}
    data = request.get_json()
    if UserDAO(user=User(**data)).is_valid():
        permission['permission'] = True
    return jsonify(permission)


@user.route('/user/index', methods=['GET'])
@auth.login_required
def user_data():
    return f"Iniciaste sesion"
