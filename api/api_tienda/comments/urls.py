from flask import Blueprint, jsonify, request
from api_tienda.catalog.models import Product
from .dao import CommentsDataAccessObject
from .models import Comment
from api_tienda import auth

comments = Blueprint('comments', __name__)


@comments.route('/catalog/products/<int:product_id>/comments', methods=['GET'])
def get_product_comments(product_id):
    comment = Comment(product_id=product_id)
    product_comments = CommentsDataAccessObject().get_comments_by_product(comment)
    return jsonify(product_comments)


@comments.route('/catalog/products/<int:product_id>/comments', methods=['POST'])
@auth.login_required
def create_comment(product_id):
    response = {}
    data = request.get_json()
    comment = Comment(product_id=product_id, user=auth.current_user().get_username(), **data)
    if data.get('comment_description') != "":
        CommentsDataAccessObject().save(comment)
        response['message'] = 'Se agrego tu comentario correctamente!'
        return jsonify(response)
    response['error_description'] = 'La descripcion de tu comentario no puede estar vacia!'
    return jsonify(response)


@comments.route('/catalog/products/comments/<int:comment_id>', methods=['DELETE'])
@auth.login_required
def delete_comment(comment_id):
    response = {}
    comment = Comment(comment_id=comment_id, user=auth.current_user().get_username())
    exists = CommentsDataAccessObject().exists(comment)
    if exists:
        CommentsDataAccessObject().delete(comment)
        response['message'] = 'Se ha eliminado el comentario!'
        return jsonify(response)
    response['error_comment'] = 'No existe el comentario!'
    return jsonify(response)