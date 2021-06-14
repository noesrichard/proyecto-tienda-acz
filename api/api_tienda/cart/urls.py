from flask import Blueprint, request, jsonify
from .models import Cart
from .dao import CartDataAccessObject
from api_tienda import auth

cart = Blueprint('cart', __name__)


@cart.route('/cart/products', methods=['POST'])
@auth.login_required
def add_product():
    response = {'message': 'Todo bien'}
    data = request.get_json()
    new_cart = Cart(product=data.get('product'), user=auth.current_user().get_username(),
                    quantity=data.get('quantity'))
    CartDataAccessObject().save(new_cart)
    return jsonify(response)


@cart.route('/cart/products', methods=['GET'])
@auth.login_required
def get_cart():
    user = auth.current_user()
    user_cart = Cart(user=user.get_username())
    response = CartDataAccessObject().get_all(user_cart)
    return jsonify(response)


@cart.route('/cart/products/<int:cart_id>', methods=['DELETE'])
@auth.login_required
def delete_cart_product(cart_id):
    response = {'message': 'Todo bien'}
    cart_obj = Cart(cart_id=cart_id)
    CartDataAccessObject().delete(cart_obj)
    return jsonify(response)
