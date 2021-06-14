from .dao import CartDataAccessObject
from api_tienda.models import Cart


def add_cart(new_cart):
    response = {"message": "todo bien"}
    try:
        CartDataAccessObject().save(new_cart)
    except:
        response['message'] = "Hubo un error"
    return response


def get_cart(user_cart):
    return CartDataAccessObject().get_all(user_cart)


def delete_cart(cart):
    response = {'message': 'Todo bien'}
    try:
        CartDataAccessObject().delete(cart)
    except:
        response['message'] = 'Hubo un error'
    return response
