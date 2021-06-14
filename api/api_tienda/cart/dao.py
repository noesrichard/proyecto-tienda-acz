from api_tienda.data_access_object import DataAccessObject


class CartDataAccessObject(DataAccessObject):
    def __init__(self, cart=None):
        super().__init__(entity_name='cart')

    def save(self, cart):
        super()._save(f"null,'{cart.get_user()}', '{cart.get_product()}', '{cart.get_quantity()}'")

    def get_all(self, cart):
        return super()._get_all_as_dict(columns="cart.id_car as cart_id, product.nam_pro as product_name, "
                                                "product.pri_pro as product_price, "
                                                "cart.qua_pro_car as product_quantity",
                                        condition="INNER JOIN product ON cart.id_pro_car = product.id_pro "
                                                  f"WHERE cart.user_car = '{cart.get_user()}'")

    def delete(self, cart):
        super()._delete(f"WHERE id_car={cart.get_id()}")
