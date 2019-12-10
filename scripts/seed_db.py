import requests
from util.password_generator import get_bad_password, get_good_password
from faker import Faker
from random import randint, random

'''
requests.post(url="http://127.0.0.1:8888/register", json={"email": "email@email.com",
                                                         "password": "a_password"})
'''


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
