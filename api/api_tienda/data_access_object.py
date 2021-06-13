from api_tienda import db


class DataAccessObject:

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


class BrandDataAccessObject(DataAccessObject):

    def __init__(self, brand=None):
        super().__init__(entity_name='brand')
        self.__columns = {
            'id_bra': 'id_bra as brand_id',
            'nam_bra': 'nam_bra as brand_name'
        }

    def __all_columns(self):
        return super()._all_columns(self.__columns)

    def save(self, brand):
        super()._save(f"null,'{brand.get_name()}'")

    def get_all(self):
        return super()._get_all_as_dict(columns=self.__all_columns())

    def update(self, brand):
        super()._update(sql_params=f"nam_bra='{brand.get_name()}' "
                                   f"WHERE id_bra={brand.get_id()}")

    def delete(self, brand):
        super()._delete(condition=f"WHERE id_bra={brand.get_id()}")

    def get_one_by_id(self, brand):
        return super()._get_one_as_dict(columns="id_bra as brand_id, nam_bra as brand_name",
                                        condition=f"WHERE id_bra={brand.get_id}")


class CategoryDataAccessObject(DataAccessObject):

    def __init__(self, category=None):
        super().__init__(entity_name='category')
        self.__columns = {
            'id_cat': 'id_cat as category_id',
            'nam_cat': 'nam_cat as category_name'
        }

    def save(self, category):
        super()._save(f"null,'{category.get_name()}'")

    def __all_columns(self):
        return super()._all_columns(self.__columns)

    def get_all(self):
        return super()._get_all_as_dict(columns=self.__all_columns())

    def update(self, category):
        super()._update(
            sql_params=f"nam_cat='{category.get_name()}' "
                       f"WHERE id_cat={category.get_id()}")

    def delete(self, category):
        super()._delete(condition=f"WHERE id_cat={category.get_id()}")

    def get_one_by_id(self, category):
        return super()._get_one_as_dict(columns="id_cat as category_id, nam_cat as category_name",
                                        condition=f"WHERE id_cat={category.get_id()}")

    def exists(self, category):
        return super()._sql_query(f"SELECT EXISTS( SELECT * FROM category WHERE nam_cat='{category.get_name()}');")


class ProductDataAccessObject(DataAccessObject):

    def __init__(self, product=None):
        super().__init__(entity_name='product')
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

    def save(self, product):
        super()._save(
            f"null,'{product.get_name()}','{product.get_description()}',{product.get_price()},"
            f"{product.get_quantity()}, {product.get_category()}, {product.get_brand()}")

    def get_all(self):
        return super()._get_all_as_dict(
            columns=self.__all_columns() + ", category.nam_cat as category, brand.nam_bra as brand",
            condition="INNER JOIN category ON product.id_cat_pro=category.id_cat "
                      "INNER JOIN brand ON product.id_bra_pro=brand.id_bra;")

    def get_one_by_id(self, product):
        return super()._get_one_as_dict(columns=self.__all_columns(),
                                        condition=f"WHERE id_pro = {product.get_id()}")

    def get_all_by_category(self, product):
        return super()._get_all_as_dict(columns=self.__all_columns(),
                                        condition=f"WHERE id_cat_pro={product.get_category()}")

    def get_all_by_brand(self, product):
        return super()._get_all_as_dict(columns=self.__all_columns(),
                                        condition=f"WHERE id_bra_pro={product.get_brand()}")

    def update(self, product):
        super()._update(
            sql_params=f"nam_pro='{product.get_name()}', des_pro='{product.get_description()}', "
                       f"pri_pro={product.get_price()}, qua_pro={product.get_quantity()}, "
                       f"id_cat_pro={product.get_category()}, "
                       f"id_bra_pro={product.get_brand()} WHERE id_pro={product.get_id()}")

    def delete(self, product):
        super()._delete(condition=f"WHERE id_pro={product.get_id()}")


class UserDataAccessObject(DataAccessObject):

    def __init__(self, user=None):
        super().__init__(entity_name='users')

    def save(self, user):
        super()._save(f"'{user.get_username()}', '{user.get_password()}'")

    def exists(self, user):
        return super()._sql_query(f"SELECT EXISTS( SELECT * FROM users WHERE username='{user.get_username()}' AND"
                                  f" passwd='{user.get_password()}');")

    def exists_username(self, user):
        return super()._sql_query(f"SELECT EXISTS( SELECT * FROM users WHERE username='{user.get_username()}')")


class CartDataAccessObject(DataAccessObject):
    def __init__(self, cart=None):
        super().__init__(entity_name='cart')

    def save(self, cart):
        super()._save(f"null,'{cart.get_user()}', '{cart.get_product()}', '{cart.get_quantity()}'")

    def get_all(self, cart):
        return super()._get_all_as_dict(columns="cart.id_car as cart_id, product.nam_pro as product_name, "
                                                "product.pri_pro as product_price, "
                                                "cart.qua_pro_car as product_quantity",
                                        condition="INNER JOIN product ON cart.id_pro_car = product.id_pro "
                                                  f"WHERE cart.user_car = '{cart.get_user()}'")

    def delete(self, cart):
        super()._delete(f"WHERE id_car={cart.get_id()}")
