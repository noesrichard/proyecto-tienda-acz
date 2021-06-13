from ..data_access_object import UserDataAccessObject
from .validator import validate_user


def create_user(user):
    response = validate_user(user)
    if UserDataAccessObject().exists_username(user):
        response['error_user'] = 'Nombre de usuario no disponible'
    print(response)
    if 'error_username_password' not in response and 'error_user' not in response:
        UserDataAccessObject().save(user)
        response['status'] = 'Usuario creado exitosamente'
        return response
    return response
