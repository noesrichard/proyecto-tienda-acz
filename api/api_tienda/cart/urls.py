from flask import Blueprint, request, jsonify
from ..data_access_object import CartDataAccessObject
from ..models import Cart
cart = Blueprint('cart', __name__)

@cart.route('/cart/products/<int:id_pro>', methods=['POST'])
def add_product(id_pro):
    data = request.get_json()
    print(data)
    CartDataAccessObject(cart=Cart(id_pro_car=id_pro, **data)).save()
    return "200 OK POST"