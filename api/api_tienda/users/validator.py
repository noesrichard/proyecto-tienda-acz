import re


def validate_username(user):
    if re.match("^[a-zA-Z0-9_.-]+$", user.get_username()):
        return True
    return False


def validate_password(user):
    if re.match("^[a-zA-Z0-9_.-]+$", user.get_password()):
        return True
    return False


def validate_user(user):
    response = {}
    if validate_username(user) and validate_password(user):
        return response
    response['error_username_password'] = 'Usuario o contraseña no valido!'
    return response
