
from api_tienda.entities import  Brand, Category, Product
from api_tienda.DAO import BrandDAO, CategoryDAO, ProductDAO
from flask import jsonify, Blueprint, request

catalog = Blueprint('api_catalog', __name__)


@catalog.route('/catalog/categories', methods=['GET'])
def get_categories():
    return jsonify(CategoryDAO().get_all())


@catalog.route('/catalog/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    CategoryDAO(category=Category(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    CategoryDAO(category=Category(category_id=category_id, **data)).update()
    return "200 OK PUT"


@catalog.route('/catalog/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    CategoryDAO(category=Category(category_id=category_id)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return jsonify(CategoryDAO(category=Category(category_id=category_id)).get_one_by_id())


@catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDAO().get_all())


@catalog.route('/catalog/products', methods=['POST'])
def create_products():
    data = request.get_json()
    ProductDAO(product=Product(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify(ProductDAO(product=Product(product_id=product_id)).get_one_by_id())


@catalog.route('/catalog/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    ProductDAO(product=Product(product_id=product_id, **data)).update()
    return "200 OK PUT"


@catalog.route('/catalog/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    ProductDAO(product=Product(product_id=product_id)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/products/search', methods=['GET'])
def search_products():
    if 'category_id' in request.args:
        category = request.args.get('category_id')
        return jsonify(ProductDAO(Product(category_id=category)).get_all_by_category())
    elif 'brand_id' in request.args:
        brand = request.args.get('brand_id')
        return jsonify(ProductDAO(Product(brand_id=brand)).get_all_by_brand())
    return "404"


@catalog.route('/catalog/brands', methods=['POST'])
def create_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDAO().get_all())


@catalog.route('/catalog/brands/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    return jsonify(BrandDAO(brand=Brand(brand_id=brand_id)).get_one_by_id())


@catalog.route('/catalog/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    BrandDAO(brand=Brand(brand_id=brand_id)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.get_json()
    BrandDAO(brand=Brand(brand_id=brand_id, **data)).update()
    return "200 OK PUT"
