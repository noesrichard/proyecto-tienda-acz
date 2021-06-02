from api_tienda import db


class DAO:

    def __init__(self, entity_name=None):
        self.__db = db
        self.__entity_name = entity_name

    def get_all(self):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name};")
        return cur.fetchall()

    def _save(self, sql_params):
        cur = self.__db.get_cursor()
        cur.execute(f'''INSERT INTO {self.__entity_name} 
                VALUES({sql_params});''')
        cur.connection.commit()

    def _get_all_by(self, condition):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name} {condition};")
        return cur.fetchall()

    def _get_one_by(self, condition):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name} {condition};")
        return cur.fetchone()

    def _update(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f"UPDATE {self.__entity_name} SET {sql_params};")
        cur.connection.commit()

    def _delete(self, condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"DELETE FROM {self.__entity_name} {condition};")
        cur.connection.commit()


class BrandDAO(DAO):

    def __init__(self, brand=None):
        super().__init__(entity_name='brand')
        self.__brand = brand

    def save(self):
        super()._save(f"null,'{self.__brand.get_name()}'")

    def update(self):
        super()._update(sql_params=f"nam_bra='{self.__brand.get_name()}' "
                                   f"WHERE id_bra={self.__brand.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_bra={self.__brand.get_id()}")

    def get_one_by_id(self):
        return super()._get_one_by(condition=f"WHERE id_bra={self.__brand.get_id}")


class CategoryDAO(DAO):

    def __init__(self, category=None):
        super().__init__(entity_name='category')
        self.__category = category

    def save(self):
        super()._save(f"null,'{self.__category.get_name()}'")

    def update(self):
        super()._update(
            sql_params=f"nam_cat='{self.__category.get_name()}' "
                       f"WHERE id_cat={self.__category.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_cat={self.__category.get_id()}")

    def get_one_by_id(self):
        return super()._get_one_by(f"WHERE id_cat={self.__category.get_id()}")


class ProductDAO(DAO):

    def __init__(self, product=None):
        super().__init__(entity_name='product')
        self.__product = product

    def save(self):
        super()._save(
            f"null,'{self.__product.get_name()}','{self.__product.get_description()}',{self.__product.get_price()},"
            f"{self.__product.get_quantity()}, {self.__product.get_category()}, {self.__product.get_brand()}")

    def get_all(self):
        return super()._get_all_by(condition="INNER JOIN category ON product.id_cat_pro=category.id_cat "
                                             "INNER JOIN brand ON product.id_bra_pro=brand.id_bra;")

    def get_one_by_id(self):
        return super()._get_one_by(f"WHERE id_pro = {self.__product.get_id()}")

    def get_all_by_category(self):
        return super()._get_all_by(f"WHERE id_cat_pro={self.__product.get_category()}")

    def get_all_by_brand(self):
        return super()._get_all_by(f"WHERE id_bra_pro={self.__product.get_brand()}")

    def update(self):
        super()._update(
            sql_params=f"nam_pro='{self.__product.get_name()}', des_pro='{self.__product.get_description()}', "
                       f"pri_pro={self.__product.get_price()}, qua_pro={self.__product.get_quantity()}, "
                       f"id_cat_pro={self.__product.get_category()}, "
                       f"id_bra_pro={self.__product.get_brand()} WHERE id_pro={self.__product.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_pro={self.__product.get_id()}")


class UserDAO(DAO):

    def __init__(self, user=None):
        super().__init__(entity_name='users')
        self.__user = user

    def save(self):
        super()._save(sql_params=f"null,'{self.__user.get_email()}', '{self.__user.get_name()}', "
                                 f"'{self.__user.get_password()}' "
                                 f"'{self.__user.get_name()}', '{self.__user.get_last_name()}', false ")
