from .DAO import DAO

class CartDAO(DAO):

    def __init__(self, user=None):
        super().__init__(entity_name='users_product')
        self.__user = user

    def get_cart(self):
        return super()._get_all_by(condition= f"INNER JOIN product ON users_product.id_pro_car=product.id_pro "
                                   f"WHERE ema_user_car='{self.__user.get_email()}'")