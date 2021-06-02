
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


@catalog.route('/catalog/categories/<int:id_cat>', methods=['PUT'])
def update_category(id_cat):
    data = request.get_json()
    CategoryDAO(category=Category(id_cat=id_cat, **data)).update()
    return "200 OK PUT"


@catalog.route('/catalog/categories/<int:id_cat>', methods=['DELETE'])
def delete_category(id_cat):
    CategoryDAO(category=Category(id_cat=id_cat)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/categories/<int:id_cat>', methods=['GET'])
def get_category(id_cat):
    return jsonify(CategoryDAO(category=Category(id_cat=id_cat)).get_one_by_id())


@catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDAO().get_all())


@catalog.route('/catalog/products', methods=['POST'])
def create_products():
    data = request.get_json()
    ProductDAO(product=Product(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/products/<int:id_pro>', methods=['GET'])
def get_product(id_pro):
    return jsonify(ProductDAO(product=Product(id_pro=id_pro)).get_one_by_id())


@catalog.route('/catalog/products/<int:id_pro>', methods=['PUT'])
def update_product(id_pro):
    data = request.get_json()
    ProductDAO(product=Product(id_pro=id_pro, **data)).update()
    return "200 OK PUT"


@catalog.route('/catalog/products/<int:id_pro>', methods=['DELETE'])
def delete_product(id_pro):
    ProductDAO(product=Product(id_pro=id_pro)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/products/search', methods=['GET'])
def search_products():
    if 'id_cat' in request.args:
        category = request.args.get('id_cat')
        return jsonify(ProductDAO(Product(id_cat_pro=category)).get_all_by_category())
    elif 'id_bra' in request.args:
        brand = request.args.get('id_bra')
        return jsonify(ProductDAO(Product(id_bra_pro=brand)).get_all_by_brand())
    return "404"


@catalog.route('/catalog/brands', methods=['POST'])
def create_brand():
    data = request.get_json()
    BrandDAO(brand=Brand(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDAO().get_all())


@catalog.route('/catalog/brands/<int:id_bra>', methods=['GET'])
def get_brand(id_bra):
    return jsonify(BrandDAO(brand=Brand(id_bra=id_bra)).get_one_by_id())


@catalog.route('/catalog/brands/<int:id_bra>', methods=['DELETE'])
def delete_brand(id_bra):
    BrandDAO(brand=Brand(id_bra=id_bra)).delete()
    return "200 OK DELETE"


@catalog.route('/catalog/brands/<int:id_bra>', methods=['PUT'])
def update_brand(id_bra):
    data = request.get_json()
    BrandDAO(brand=Brand(id_bra=id_bra, **data)).update()
    return "200 OK PUT"
