from api_tienda.data_access_object import DataAccessObject


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
