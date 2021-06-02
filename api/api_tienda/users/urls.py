from flask import Blueprint, request
from utils import verify_registration_data
from api_tienda.DAO import UserDAO
from api_tienda.entities import User

user = Blueprint('user', __name__)


@user.route('/user/registration', methods=['POST'])
def user_registration():
    data = request.get_json()
    if verify_registration_data(data) != "":
        return verify_registration_data(data)
    UserDAO(user=User(**data)).save()
    return "200 OK POST"
