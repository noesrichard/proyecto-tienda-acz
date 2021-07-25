
#Comentario
class Comment:
    def __init__(self, **kwargs):
        self.__comment_id = kwargs.get('comment_id')
        self.__product = kwargs.get('product_id')
        self.__user = kwargs.get('user')
        self.__description = kwargs.get('comment_description')
        self.__qualification = kwargs.get('comment_qualification')

    def get_id(self):
        return self.__comment_id

    def get_product(self):
        return self.__product

    def get_user(self):
        return self.__user

    def get_description(self):
        return self.__description

    def get_qualification(self):
        return self.__qualification
