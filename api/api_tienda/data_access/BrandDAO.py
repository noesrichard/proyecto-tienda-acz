from .DAO import DAO


class BrandDAO(DAO):

    def __init__(self, brand=None):
        super().__init__(entity_name='brand')
        self.__brand = brand

    def save(self):
        super()._save(f"null,'{self.__brand.get_name()}','{self.__brand.get_description()}'")

    def update(self):
        super()._update(sql_params=f"nam_bra='{self.__brand.get_name()}', des_bra='{self.__brand.get_description()}'"
                                   f"WHERE id_bra={self.__brand.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_bra={self.__brand.get_id()}")

    def get_one_by_id(self):
        return super()._get_one_by(condition=f"WHERE id_bra={self.__brand.get_id}")
