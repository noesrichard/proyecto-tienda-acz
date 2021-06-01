from api_tienda.data_access.BrandDAO import BrandDAO
from api_tienda.data_access.ProductDAO import ProductDAO
from api_tienda.models.Brand import Brand
from api_tienda.models.Category import Category
from api_tienda.models.Product import Product
from api_tienda.data_access.CategoryDAO import CategoryDAO
from .utils import response
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


@catalog.route('/catalog/categories/<int:id_cat>', methods=['PUT', 'DELETE', 'GET'])
def categories(id_cat):
    if request.method == 'PUT':
        data = request.get_json()
        category = CategoryDAO(category=Category(id_cat=id_cat, **data))
    else:
        category = CategoryDAO(category=Category(id_cat=id_cat))
    return response(method=request.method, entity=category)


@catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDAO().get_all())


@catalog.route('/catalog/products', methods=['POST'])
def create_products():
    data = request.get_json()
    ProductDAO(product=Product(**data)).save()
    return "200 OK POST"


@catalog.route('/catalog/products/<int:id_pro>', methods=['GET', 'PUT', 'DELETE'])
def products(id_pro):
    if request.method == 'PUT':
        data = request.get_json()
        product = ProductDAO(product=Product(id_pro=id_pro, **data))
    else:
        product = ProductDAO(product=Product(id_pro=id_pro))
    return response(method=request.method, entity=product)


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


@catalog.route('/catalog/brands/<int:id_bra>', methods=['GET', 'DELETE', 'PUT'])
def update_brand(id_bra):
    if request.method == 'PUT':
        data = request.get_json()
        brand = BrandDAO(brand=Brand(id_bra = id_bra, **data))
    else:
        brand = BrandDAO(brand=Brand(id_bra=id_bra))
    return response(method=request.method, entity=brand)

