import json
from util.util import hash_password
from application_configuration.app import db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    balance = db.Column(db.Numeric)

    def __init__(self, email, password, starting_balance=0):
        self.email = email
        self.password = hash_password(password)
        self.balance = starting_balance

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "balance": float(self.balance)
        }

    def to_json(self):
        return json.dumps(self.to_dict())
