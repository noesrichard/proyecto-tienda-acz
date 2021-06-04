

class Validator:
    def __init__(self, entity=None):
        self._entity = entity

    def validate(self):
        pass


class UserValidator(Validator):

    def __init__(self, user=None):
        super().__init__(user)

    def validate(self):
        if self._entity.get_username() == "":
            return False
        if self._entity.get_password() == "":
            return False
        if self._entity.get_name() == "":
            return False
        if self._entity.get_last_name() == "":
            return False
        return True
