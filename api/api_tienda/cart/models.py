class Cart:
    def __init__(self, **kwargs):
        self.__cart_id = kwargs.get('cart_id')
        self.__user = kwargs.get('user')
        self.__product = kwargs.get('product')
        self.__quantity = kwargs.get('quantity')

    def get_id(self):
        return self.__cart_id

    def get_user(self):
        return self.__user

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity
