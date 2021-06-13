from flask import Blueprint, request, jsonify
from ..data_access_object import CartDataAccessObject
from ..models import Cart
from api_tienda import auth
from api_tienda.cart import app

cart = Blueprint('cart', __name__)


@cart.route('/cart/products', methods=['POST'])
@auth.login_required
def add_product():
    data = request.get_json()
    new_cart = Cart(product=data.get('product'), user=auth.current_user().get_username(),
                    quantity=data.get('quantity'))
    response = app.add_cart(new_cart)
    return jsonify(response)

@cart.route('/cart/products', methods=['GET'])
@auth.login_required
def get_cart():
    user = auth.current_user()
    cart = Cart(user=user.get_username())
    cartDao = CartDataAccessObject().get_all(cart)
    return jsonify(cartDao)

@cart.route('/cart/products/<int:cart_id>', methods=['DELETE'])
@auth.login_required
def delete_cart_product(cart_id):
    CartDataAccessObject(Cart(cart_id=cart_id)).delete()
    return "200 OK DELETE"

