
class User:
    def __init__(self, **kwargs):
        self.__email = kwargs.get('ema_user')
        self.__name = kwargs.get('nam_user')

    def get_email(self):
        return self.__email

    def get_name(self):
        return self.__name
