from flask import Blueprint, request, jsonify
from ..data_access_object import CartDataAccessObject
from ..models import Cart
from api_tienda import auth

cart = Blueprint('cart', __name__)


@cart.route('/cart/products/<int:product>', methods=['POST'])
@auth.login_required
def add_product(product):
    data = request.get_json()
    CartDataAccessObject(cart=Cart(product=product, user=auth.current_user().get_username(),
                                   quantity=data.get('quantity'))).save()
    return "200 OK POST"

@cart.route('/cart/products', methods=['GET'])
@auth.login_required
def get_cart():
    cart = CartDataAccessObject(Cart(user=auth.current_user().get_username())).get_all()
    return jsonify(cart)