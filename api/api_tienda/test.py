import unittest
from users.models import User
from users import validator

#Comentario
class Test(unittest.TestCase):

    def test_valid_username(self):
        user = User(username="ric.-r")
        result = validator.validate_username(user)
        self.assertTrue(result)

    def test_valid_password(self):
        user = User(password="12qwe.reu_12")
        result = validator.validate_password(user)
        self.assertTrue(result)

    def test_invalid_username(self):
        user = User(username="ric .-r")
        result = validator.validate_username(user)
        self.assertFalse(result)

    def test_invalid_password(self):
        user = User(password="12qwe .reu_12")
        result = validator.validate_password(user)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
