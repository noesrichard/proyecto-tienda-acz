from flask import Blueprint, request, jsonify
from api_tienda.DAO import UserDAO
from api_tienda.entities import User
from api_tienda import auth
from .validator import  UserValidator

user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    new_user = User(**data)
    is_valid = UserValidator(new_user).validate()
    if is_valid:
        UserDAO(user=User(**data)).save()
        return "200 OK POST"
    return "NO SE REGISTRO"



@auth.verify_password
def verify_password(username, password):
    client_user = UserDAO(User(ema_user=username, pas_user=password))
    if client_user.exists():
        return client_user.get_user()


@user.route('/user/login', methods=['POST'])
def login():
    permission = {'permission': False}
    data = request.get_json()
    if UserDAO(user=User(**data)).exists():
        permission['permission'] = True
    return jsonify(permission)


@user.route('/user/index', methods=['GET'])
@auth.login_required
def user_data():
    return f"Iniciaste sesion"
