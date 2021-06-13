from api_tienda.data_access_object import CartDataAccessObject
from api_tienda.models import Cart


def add_cart(new_cart):
    response = {"message": "todo bien"}
    try:
        CartDataAccessObject().save(new_cart)
    except:
        response['message'] = "Hubo un error"
    return response
