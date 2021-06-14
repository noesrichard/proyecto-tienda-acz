from flask import Blueprint, request, jsonify
from .dao import UserDataAccessObject
from api_tienda.models import User
from api_tienda import auth
from api_tienda.users import validator
user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    new_user = User(username=data.get('username'), password=data.get('password'))
    repeated_password = data.get('repeated_password')
    response = validator.validate_user(new_user)
    if repeated_password != new_user.get_password():
        response['error_password'] = 'Las contraseñas no coinciden'
    if UserDataAccessObject().exists_username(new_user):
        response['error_user'] = "Nombre de usuario no disponible"
    if 'error_username_password' not in response and 'error_user' not in response and 'error_password' not in response:
        UserDataAccessObject().save(new_user)
        response['message'] = 'Usuario creado exitosamente!'
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
