import hashlib
from flask import make_response


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def check_password(password, password_hash):
    # return the comparison of a hashed version of password to user.password_hash
    return hashlib.sha256(password.encode("utf-8")).hexdigest() == password_hash


def make_json_response(the_json, status_code):
    response = make_response(the_json, status_code)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
    '''response.headers.add('Access-Control-Allow-Headers',
                         "Origin, X-Requested-With, Content-Type, Accept, x-auth")
    '''
    return response
