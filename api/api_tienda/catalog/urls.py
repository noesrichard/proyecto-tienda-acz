from .data_access_object.BrandDAO import BrandDAO
from .data_access_object.ProductDAO import ProductDAO
from .model.Brand import Brand
from .model.Category import Category
from .model.Product import Product
from .data_access_object.CategoryDAO import CategoryDAO
from flask import jsonify, Blueprint, request

api_catalog = Blueprint('api_catalog', __name__)


@api_catalog.route('/catalog/categories', methods=['GET'])
def get_categories():
    return jsonify(CategoryDAO().get_all())


@api_catalog.route('/catalog/create-category', methods=['POST'])
def create_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).save()
    return "Done"


@api_catalog.route('/catalog/update-category', methods=['PUT'])
def update_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).update()
    return "Done"


@api_catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDAO().get_all())


@api_catalog.route('/catalog/products/category/<int:category>', methods=['GET'])
def get_products_by_category(category):
    return jsonify(ProductDAO().get_all_by_category(category))


@api_catalog.route('/catalog/products/brand/<int:brand>', methods=['GET'])
def get_products_by_brand(brand):
    return jsonify(ProductDAO().get_all_by_brand(brand))


@api_catalog.route('/catalog/product/<int:id_pro>', methods=['GET'])
def get_product(id_pro):
    return jsonify(ProductDAO().get_one_by_id(id_pro))


@api_catalog.route('/catalog/create-product', methods=['POST'])
def create_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).save()
    return "Done"


@api_catalog.route('/catalog/update-product', methods=['PUT'])
def update_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).update()
    return "Done"


@api_catalog.route('/catalog/create-brand', methods=['POST'])
def create_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).save()
    return "Done"


@api_catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDAO().get_all())


@api_catalog.route('/catalog/update-brand', methods=['PUT'])
def update_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).update()
    return "Done"


@api_catalog.route('/catalog/delete-brand', methods=['DELETE'])
def delete_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).delete()
    return "Done"


@api_catalog.route('/catalog/delete-product', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).delete()
    return "Done"


@api_catalog.route('/catalog/delete-category', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).delete()
    return "Done"