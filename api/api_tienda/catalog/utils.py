

def response(method='GET', entity=None):
    if method == 'GET':
        return entity.get_one_by_id()
    elif method == 'POST':
        entity.save()
        return "200 OK POST"
    elif method == 'PUT':
        entity.update()
        return "200 OK PUT"
    elif method == 'DELETE':
        entity.delete()
        return "200 OK DELETE"