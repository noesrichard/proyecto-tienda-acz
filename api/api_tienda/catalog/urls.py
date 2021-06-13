from api_tienda.models import Brand, Category, Product
from api_tienda.data_access_object import BrandDataAccessObject, CategoryDataAccessObject, ProductDataAccessObject
from flask import jsonify, Blueprint, request

catalog = Blueprint('api_catalog', __name__)


@catalog.route('/catalog/categories', methods=['GET'])
def get_categories():
    return jsonify(CategoryDataAccessObject().get_all())


'''
JSON:
{
    "category_id": 
    "category_name":
}
'''


@catalog.route('/catalog/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    CategoryDataAccessObject().save(category=Category(**data))
    return "200 OK POST"


@catalog.route('/catalog/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    CategoryDataAccessObject().update(category=Category(category_id=category_id, **data))
    return "200 OK PUT"


@catalog.route('/catalog/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    CategoryDataAccessObject().delete(category=Category(category_id=category_id))
    return "200 OK DELETE"


@catalog.route('/catalog/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return jsonify(CategoryDataAccessObject().get_one_by_id(category=Category(category_id=category_id)))


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
    ProductDataAccessObject().save(product=Product(**data))
    return "200 OK POST"


@catalog.route('/catalog/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify(ProductDataAccessObject().get_one_by_id(product=Product(product_id=product_id)))


@catalog.route('/catalog/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    ProductDataAccessObject().update(product=Product(product_id=product_id, **data))
    return "200 OK PUT"


@catalog.route('/catalog/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    ProductDataAccessObject().delete(product=Product(product_id=product_id))
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
    BrandDataAccessObject().save(brand=Brand(**data))
    return "200 OK POST"


@catalog.route('/catalog/brands', methods=['GET'])
def get_brands():
    return jsonify(BrandDataAccessObject().get_all())


@catalog.route('/catalog/brands/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    return jsonify(BrandDataAccessObject().get_one_by_id(brand=Brand(brand_id=brand_id)))


@catalog.route('/catalog/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    BrandDataAccessObject().delete(brand=Brand(brand_id=brand_id))
    return "200 OK DELETE"


@catalog.route('/catalog/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.get_json()
    BrandDataAccessObject().update(brand=Brand(brand_id=brand_id, **data))
    return "200 OK PUT"
