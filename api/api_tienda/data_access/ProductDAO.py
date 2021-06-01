from .DAO import DAO


class ProductDAO(DAO):

    def __init__(self, product=None):
        super().__init__(entity_name='product')
        self.__product = product

    def save(self):
        super()._save(
            f"null,'{self.__product.get_name()}','{self.__product.get_description()}',{self.__product.get_price()},{self.__product.get_category()}, {self.__product.get_brand()}")

    def get_all(self):
        return super()._get_all_by(condition="INNER JOIN category ON product.id_cat_pro=category.id_cat "
                                             "INNER JOIN brand ON product.id_bra_pro=brand.id_bra;")

    def get_one_by_id(self, id_pro):
        return super()._get_one_by(f"WHERE id_pro = {id_pro}")

    def get_all_by_category(self, id_cat):
        return super()._get_all_by(f"WHERE id_cat_pro={id_cat}")

    def get_all_by_brand(self, id_bra):
        return super()._get_all_by(f"WHERE id_bra_pro={id_bra}")

    def update(self):
        super()._update(sql_params=f"nam_pro='{self.__product.get_name()}', des_pro='{self.__product.get_description()}', "
                                   f"pri_pro={self.__product.get_price()}, id_cat_pro={self.__product.get_category()}, "
                                   f"id_bra_pro={self.__product.get_brand()} WHERE id_pro={self.__product.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_pro={self.__product.get_id()}")