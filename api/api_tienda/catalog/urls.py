from api_tienda.data_access.BrandDAO import BrandDAO
from api_tienda.data_access.ProductDAO import ProductDAO
from api_tienda.models.Brand import Brand
from api_tienda.models.Category import Category
from api_tienda.models.Product import Product
from api_tienda.data_access.CategoryDAO import CategoryDAO
from flask import jsonify, Blueprint, request

catalog = Blueprint('api_catalog', __name__)


@catalog.route('/catalog/categories', methods=['GET'])
def get_categories():
    return jsonify(CategoryDAO().get_all())


@catalog.route('/catalog/create-category', methods=['POST'])
def create_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).save()
    return "Done"


@catalog.route('/catalog/update-category', methods=['PUT'])
def update_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).update()
    return "Done"


@catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDAO().get_all())


@catalog.route('/catalog/products/category/<int:category>', methods=['GET'])
def get_products_by_category(category):
    return jsonify(ProductDAO().get_all_by_category(category))


@catalog.route('/catalog/products/brand/<int:brand>', methods=['GET'])
def get_products_by_brand(brand):
    return jsonify(ProductDAO().get_all_by_brand(brand))


@catalog.route('/catalog/product/<int:id_pro>', methods=['GET'])
def get_product(id_pro):
    return jsonify(ProductDAO().get_one_by_id(id_pro))


@catalog.route('/catalog/create-product', methods=['POST'])
def create_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).save()
    return "Done"


@catalog.route('/catalog/update-product', methods=['PUT'])
def update_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).update()
    return "Done"


@catalog.route('/catalog/create-brand', methods=['POST'])
def create_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).save()
    return "Done"


@catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDAO().get_all())


@catalog.route('/catalog/update-brand', methods=['PUT'])
def update_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).update()
    return "Done"


@catalog.route('/catalog/delete-brand', methods=['DELETE'])
def delete_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).delete()
    return "Done"


@catalog.route('/catalog/delete-product', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    ProductDAO(product=Product(**data)).delete()
    return "Done"


@catalog.route('/catalog/delete-category', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).delete()
    return "Done"