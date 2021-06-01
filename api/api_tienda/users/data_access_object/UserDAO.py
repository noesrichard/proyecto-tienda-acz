from .DAO import DAO

class UserDAO(DAO):

    def __init__(self):
        super().__init__(entity_name='users')

