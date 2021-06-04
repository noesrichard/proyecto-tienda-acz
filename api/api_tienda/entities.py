class Brand:
    def __init__(self, **kwargs):
        self.__id = kwargs.get('brand_id')
        self.__name = kwargs.get('brand_name')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Category:

    def __init__(self, **kwargs):
        self.__id = kwargs.get('category_id')
        self.__name = kwargs.get('category_name')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Product:

    def __init__(self, **kwargs):
        self.__id = kwargs.get('product_id')
        self.__name = kwargs.get('product_name')
        self.__description = kwargs.get('product_description')
        self.__price = kwargs.get('product_price')
        self.__quantity = kwargs.get('product_quantity_available')
        self.__category = kwargs.get('category_id')
        self.__brand = kwargs.get('brand_id')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_category(self):
        return self.__category

    def get_brand(self):
        return self.__brand

    def is_price_valid(self):
        pass


class User:
    def __init__(self, **kwargs):
        self.__email = kwargs.get('ema_user')
        self.__pas_user = kwargs.get('pas_user')
        self.__name = kwargs.get('nam_user')
        self.__ape = kwargs.get('ape_user')
        self.__is_verified = kwargs.get('is_ver_user')

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__pas_user

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__ape

    def is_verified(self):
        return self.__is_verified


class Cart:
    def __init__(self, **kwargs):
        self.__id_car = kwargs.get('id_car')
        self.__user = kwargs.get('ema_user')
        self.__product = kwargs.get('id_pro_car')
        self.__quantity = kwargs.get('qua_pro_car')

    def get_id(self):
        return self.__id_car

    def get_user(self):
        return self.__user

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity
