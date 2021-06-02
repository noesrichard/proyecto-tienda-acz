from api_tienda import auth

def verify_registration_data(data):
    response = ""
    if 'ema_user' not in data:
        response + "Debe ingresar un email\n"
    if 'pas_user' not in data:
        response + "Debe ingresar una password\n"
    if 'nam_user' not in data:
        response + "Debe ingresar su nombre\n"
    if 'ape_user' not in data:
        response + "Debe ingresar su apellido\n"

    return response



