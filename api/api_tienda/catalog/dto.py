from .dao import CategoryDataAccessObject
from .dao import BrandDataAccessObject
from .dao import ProductDataAccessObject


class CatalogDataTransferObject:

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
