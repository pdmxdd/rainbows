from util.util import hash_password
from application_configuration.app import db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    balance = db.Column(db.Numeric)

    def __init__(self, email, password):
        self.email = email
        self.password = hash_password(password)
        self.balance = 0
