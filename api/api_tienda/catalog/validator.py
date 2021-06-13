import re


def validate_category(category):
    response = {}
    if re.match("^[a-zA-Z0-9]+$", category.get_name()):
        return response
    response['error_name'] = 'Nombre no valido'
    return response
