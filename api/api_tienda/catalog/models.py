from .dao import CategoryDataAccessObject
from .dao import BrandDataAccessObject
from .dao import ProductDataAccessObject


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


class Catalog:

    def __init__(self):
        self.__products = ProductDataAccessObject().get_all()
        self.__categories = CategoryDataAccessObject().get_all()
        self.__brands = BrandDataAccessObject().get_all()

    def get_catalog(self):
        data = {
            'products': self.__products,
            'categories': self.__categories,
            'brands': self.__brands
        }
        return data
