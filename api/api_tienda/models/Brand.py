class Brand:
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id_bra')
        self.__name = kwargs.get('nam_bra')
        self.__description = kwargs.get('des_bra')

    def get_entity_name(self):
        return self.__entity_name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

