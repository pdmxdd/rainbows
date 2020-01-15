import json
import os
import hashlib
from flask import make_response
import requests
from faker import Faker
from random import randint, random
from util.password_generator import get_bad_password, get_good_password


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def check_password(password, password_hash):
    # return the comparison of a hashed version of password to user.password_hash
    return hashlib.sha256(password.encode("utf-8")).hexdigest() == password_hash


def make_json_response(the_dict, status_code):
    response = make_response(json.dumps(the_dict), status_code)
    response.headers.add('Access-Control-Allow-Origin', f'{os.environ.get("FRONT_END")}')
    response.headers.add('Content-Type', 'application/json')
    '''response.headers.add('Access-Control-Allow-Headers',
                         "Origin, X-Requested-With, Content-Type, Accept, x-auth")
    '''
    return response


def seed_db_with_users():
    fake = Faker()

    for i in range(100):
        if randint(0, 1) == 1:
            password = get_good_password()
        else:
            password = get_bad_password()

        random_balance = randint(25, 25000) * random()

        requests.post(url="http://127.0.0.1:8888/register",
                      json={"email": fake.ascii_free_email(), "password": password, "starting_balance": random_balance})
