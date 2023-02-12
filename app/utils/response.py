
def success_response(message='Successfully retrieve data', data=None):
    return {'status': 'Success', 'message': message, 'data': data}, 200


def bad_request_response(reason=None, data=None):
    return {'status': 'Bad Request', 'reason': reason, 'data': data}, 400


def unauthorized_response(reason=None, data=None):
    return {'status': 'Unauthorized', 'reason': reason, 'data': data}, 401


def forbidden_response(reason=None, data=None):
    return {'status': 'Forbidden', 'reason': reason, 'data': data}, 403


def page_not_found_response(reason=None, data=None):
    return {'status': 'Page Not Found', 'reason': reason, 'data': data}, 404


def error_response(reason='Unknown Error', data=None):
    return {'status': 'Internal Server Error', 'reason': reason, 'data': data}, 500
