class User:
    def __init__(self, **kwargs):
        self.__username = kwargs.get('username')
        self.__password = kwargs.get('password')

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

