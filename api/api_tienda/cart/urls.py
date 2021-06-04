from flask import Blueprint, request, jsonify
from ..DAO import CartDAO
from ..entities import Cart
cart = Blueprint('cart',__name__)

@cart.route('/cart/products/<int:id_pro>', methods=['POST'])
def add_product(id_pro):
    data = request.get_json()
    print(data)
    CartDAO(cart=Cart(id_pro_car=id_pro, **data)).save()
    return "200 OK POST"