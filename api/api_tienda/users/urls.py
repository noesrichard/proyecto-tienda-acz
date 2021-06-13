from flask import Blueprint, request, jsonify
from api_tienda.data_access_object import UserDataAccessObject
from api_tienda.models import User
from api_tienda import auth
from .validator import UserValidator

user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    new_user = User(**data)
    is_valid = UserValidator(new_user).validate()
    if is_valid:
        UserDataAccessObject(user=User(**data)).save()
        return "200 OK POST"
    return "NO SE REGISTRO"


@auth.verify_password
def verify_password(username, password):
    client_user = UserDataAccessObject(User(username=username, password=password))
    if client_user.exists():
        return client_user.get_user()


@user.route('/user/login', methods=['POST'])
@auth.login_required
def login():
   permission = {'permission': True}
   return jsonify(permission)


@user.route('/user/index', methods=['GET'])
@auth.login_required
def user_data():
    return f"Iniciaste sesion"
