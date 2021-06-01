from flask import Blueprint, request, jsonify
from api_tienda.data_access.CartDAO import CartDAO
from api_tienda.models.User import User
users = Blueprint('users', __name__)


@users.route('/user/cart', methods=['GET'])
def get_user_cart_products():
    data = request.get_json()
    return jsonify(CartDAO(user=User(**data)).get_cart())
