from .models import Brand, Category, Product
from .dao import BrandDataAccessObject, CategoryDataAccessObject, ProductDataAccessObject
from .models import Catalog
from flask import jsonify, Blueprint, request
from api_tienda.catalog import validator

catalog = Blueprint('api_catalog', __name__)

'''
JSON:
{
    "category_id": 
    "category_name":
}
'''


@catalog.route('/catalog', methods=['GET'])
def get_catalog():
    data = Catalog().get_catalog()
    return jsonify(data)


@catalog.route('/catalog/categories', methods=['GET'])
def get_categories():
    data = CategoryDataAccessObject().get_all()
    return jsonify(data)


@catalog.route('/catalog/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = Category(**data)
    response = validator.validate_category(category)
    if CategoryDataAccessObject().exists(category):
        response['error_exists'] = "Ya existe una categoria con ese nombre!"
    if 'error_exists' not in response and 'error_name' not in response:
        CategoryDataAccessObject().save(category)
        response['message'] = 'Categoria creada exitosamente!'
    return jsonify(response)


@catalog.route('/catalog/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    category = Category(category_id=category_id, **data)
    CategoryDataAccessObject().update(category)
    return "200 OK PUT"


@catalog.route('/catalog/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    response = {'message': 'Categoria eliminada exitosamente'}
    category = Category(category_id=category_id)
    CategoryDataAccessObject().delete(category)
    return jsonify(response)


@catalog.route('/catalog/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category(category_id=category_id)
    return jsonify(CategoryDataAccessObject().get_one_by_id(category))


'''
JSON:
{
    "product_id": , 
    "product_name": , 
    "product_description": , 
    "product_price": , 
    "product_quantity_available": , 
    "category_id": , 
    "brand_id": , 
}
'''


@catalog.route('/catalog/products', methods=['GET'])
def get_products():
    return jsonify(ProductDataAccessObject().get_all())


@catalog.route('/catalog/products', methods=['POST'])
def create_products():
    data = request.get_json()
    product = Product(**data)
    ProductDataAccessObject().save(product)
    return "200 OK POST"


@catalog.route('/catalog/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product(product_id=product_id)
    return jsonify(ProductDataAccessObject().get_one_by_id(product))


@catalog.route('/catalog/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product(product_id, **data)
    ProductDataAccessObject().update(product)
    return "200 OK PUT"


@catalog.route('/catalog/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product(product_id=product_id)
    ProductDataAccessObject().delete(product)
    return "200 OK DELETE"


@catalog.route('/catalog/products/search', methods=['GET'])
def search_products():
    if 'category_id' in request.args:
        category = request.args.get('category_id')
        return jsonify(ProductDataAccessObject().get_all_by_category(Product(category_id=category)))
    elif 'brand_id' in request.args:
        brand = request.args.get('brand_id')
        return jsonify(ProductDataAccessObject().get_all_by_brand(Product(brand_id=brand)))
    return "404"


'''
JSON
{
    "brand_id": ,  
    "brand_name": 
}
'''


@catalog.route('/catalog/brands', methods=['POST'])
def create_brand():
    data = request.get_json()
    brand = Brand(**data)
    BrandDataAccessObject().save(brand)
    return "200 OK POST"


@catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDataAccessObject().get_all())


@catalog.route('/catalog/brands/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = Brand(brand_id=brand_id)
    return jsonify(BrandDataAccessObject().get_one_by_id(brand))


@catalog.route('/catalog/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    brand = Brand(brand_id=brand_id)
    BrandDataAccessObject().delete(brand)
    return "200 OK DELETE"


@catalog.route('/catalog/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.get_json()
    brand = Brand(brand_id=brand_id, **data)
    BrandDataAccessObject().update(brand)
    return "200 OK PUT"
