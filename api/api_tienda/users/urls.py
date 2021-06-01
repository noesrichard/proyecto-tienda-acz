from flask import Blueprint, request, jsonify
from .data_access_object.CartDAO import CartDAO
from .data_access_object.UserDAO import UserDAO
from .model.Cart import Cart
from .model.User import User
users = Blueprint('users', __name__)


@users.route('/user/cart', methods=['GET'])
def get_user_cart_products():
    data = request.get_json()
    return jsonify(CartDAO(user=User(**data)).get_cart())
