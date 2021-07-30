from flask import jsonify, abort


def json_abort(status_code, data=None):
    response = jsonify(data or {'error': 'There was an error'})
    response.status_code = status_code
    abort(response)
