class Category():

    def __init__(self, **kwargs):
        self.__id = kwargs.get('id_cat')
        self.__name = kwargs.get('nam_cat')
        self.__description = kwargs.get('des_cat')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

