from api_tienda.data_access_object import DataAccessObject


class CommentsDataAccessObject(DataAccessObject):

    def __init__(self):
        super().__init__(entity_name='comments')
        self.__columns = {
            'id_com': 'id_com as comment_id',
            'id_pro_com': 'id_pro_com as product',
            'user_com': 'user_com as username',
            'des_com': 'des_com as description',
            'qua_com': 'qua_com as qualification'
        }

    def get_comments_by_product(self, comment):
        return super()._get_all_as_dict(columns=super()._all_columns(self.__columns),
                                        condition=f"WHERE id_pro_com = {comment.get_product()}")

    def save(self, comment):
        super()._save(f"null,{comment.get_product()}, '{comment.get_user()}', '{comment.get_description()}',"
                      f" {comment.get_qualification()}")
