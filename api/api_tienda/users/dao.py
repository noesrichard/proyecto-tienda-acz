from api_tienda.data_access_object import DataAccessObject

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
