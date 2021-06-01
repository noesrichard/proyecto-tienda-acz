
from .DAO import DAO

class CategoryDAO(DAO):

    def __init__(self, category=None):
        super().__init__(entity_name='category')
        self.__category = category

    def save(self):
        super()._save(f"null,'{self.__category.get_name()}','{self.__category.get_description()}'")

    def update(self):
        super()._update(sql_params=f"nam_cat='{self.__category.get_name()}', des_cat='{self.__category.get_description()}' "
                                   f"WHERE id_cat={self.__category.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_cat={self.__category.get_id()}")