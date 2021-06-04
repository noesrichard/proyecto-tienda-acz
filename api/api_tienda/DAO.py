from api_tienda import db


class DAO:

    def __init__(self, entity_name=None):
        self.__db = db
        self.__entity_name = entity_name

    def _all_columns(self, columns):
        result = ""
        values = list(columns.values())
        for i in range(len(values)):
            if i == len(values) - 1:
                result += values[i]
            else:
                result += values[i] + ","
        return result

    def _sql_query(self, sql_query=""):
        cur = self.__db.get_cursor_no_dict()
        cur.execute(sql_query)
        return cur.fetchone()[0]

    def _get_all_as_dict(self, columns="*", condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT {columns} FROM {self.__entity_name} {condition};")
        return cur.fetchall()

    def _get_one_as_dict(self, columns="*", condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT {columns} FROM {self.__entity_name} {condition};")
        return cur.fetchone()

    def _update(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f"UPDATE {self.__entity_name} SET {sql_params};")
        cur.connection.commit()

    def _delete(self, condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"DELETE FROM {self.__entity_name} {condition};")
        cur.connection.commit()

    def _save(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f'''INSERT INTO {self.__entity_name} VALUES({sql_params});''')
        cur.connection.commit()


class BrandDAO(DAO):

    def __init__(self, brand=None):
        super().__init__(entity_name='brand')
        self.__brand = brand
        self.__columns = {
            'id_bra': 'id_bra as brand_id',
            'nam_bra': 'nam_bra as brand_name'
        }

    def __all_columns(self):
        return super()._all_columns(self.__columns)

    def save(self):
        super()._save(f"null,'{self.__brand.get_name()}'")

    def get_all(self):
        return super()._get_all_as_dict(columns=self.__all_columns())

    def update(self):
        super()._update(sql_params=f"nam_bra='{self.__brand.get_name()}' "
                                   f"WHERE id_bra={self.__brand.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_bra={self.__brand.get_id()}")

    def get_one_by_id(self):
        return super()._get_one_as_dict(columns="id_bra as brand_id, nam_bra as brand_name",
                                        condition=f"WHERE id_bra={self.__brand.get_id}")


class CategoryDAO(DAO):

    def __init__(self, category=None):
        super().__init__(entity_name='category')
        self.__category = category
        self.__columns = {
            'id_cat': 'id_cat as category_id',
            'nam_cat': 'nam_cat as category_name'
        }

    def save(self):
        super()._save(f"null,'{self.__category.get_name()}'")

    def __all_columns(self):
        return super()._all_columns(self.__columns)

    def get_all(self):
        return super()._get_all_as_dict(columns=self.__all_columns())

    def update(self):
        super()._update(
            sql_params=f"nam_cat='{self.__category.get_name()}' "
                       f"WHERE id_cat={self.__category.get_id()}")

    def delete(self):
        super()._delete(condition=f"WHERE id_cat={self.__category.get_id()}")

    def get_one_by_id(self):
        return super()._get_one_as_dict(columns="id_cat as category_id, nam_cat as category_name",
                                        condition=f"WHERE id_cat={self.__category.get_id()}")


class ProductDAO(DAO):

    def __init__(self, product=None):
        super().__init__(entity_name='product')
        self.__product = product
        self.__columns = {
            'id': 'product.id_pro as product_id',
            'name': 'product.nam_pro as product_name',
            'des': 'product.des_pro as product_description',
            'price': 'product.pri_pro as product_price',
            'ava': 'product.ava_pro as product_quantity_available',
            'id_cat': 'product.id_cat_pro as category_id',
            'id_bra': 'product.id_bra_pro as brand_id'
        }

    def __all_columns(self):
        return super()._all_columns(self.__columns)

    def save(self):
        super()._save(
            f"null,'{self.__product.get_name()}','{self.__product.get_description()}',{self.__product.get_price()},"
            f"{self.__product.get_quantity()}, {self.__product.get_category()}, {self.__product.get_brand()}")

    def get_all(self):
        return super()._get_all_as_dict(columns=self.__all_columns()+", category.nam_cat as category, brand.nam_bra as brand",
                                        condition="INNER JOIN category ON product.id_cat_pro=category.id_cat "
                                                  "INNER JOIN brand ON product.id_bra_pro=brand.id_bra;")

    def get_one_by_id(self):
        return super()._get_one_as_dict(columns=self.__all_columns(), condition=f"WHERE id_pro = {self.__product.get_id()}")

    def get_all_by_category(self):
        return super()._get_all_as_dict(columns=self.__all_columns(), condition=f"WHERE id_cat_pro={self.__product.get_category()}")

    def get_all_by_brand(self):
        return super()._get_all_as_dict(columns=self.__all_columns(), condition=f"WHERE id_bra_pro={self.__product.get_brand()}")

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

    def get_user(self):
        return self.__user

    def save(self):
        super()._save(f"'{self.__user.get_username()}', '{self.__user.get_password()}', '{self.__user.get_name()}', "
                      f"'{self.__user.get_last_name()}', {self.__user.is_verified()} ")

    def exists(self):
        return super()._sql_query(f"SELECT EXISTS( SELECT * FROM users WHERE id_user='{self.__user.get_username()}' AND"
                                  f" pas_user='{self.__user.get_password()}');")


class CartDAO(DAO):
    def __init__(self, cart=None):
        super().__init__(entity_name='cart')
        self.__cart = cart

    def save(self):
        super()._save(f"null,'{self.__cart.get_user()}', '{self.__cart.get_product()}', '{self.__cart.get_quantity()}'")
