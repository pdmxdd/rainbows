from flask import Blueprint
from models.user import User
from util.util import make_json_response, hash_password

hacker_bp = Blueprint(name="hacker_bp", import_name=__name__, url_prefix="/hacker")


@hacker_bp.route("/breach-database", methods=["POST"])
def breach_database():
    users = User.query.all()

    return make_json_response({
        "users": [user.to_dict() for user in users]
    }, 200)


@hacker_bp.route("/rainbow", methods=["GET"])
def get_rainbow_table():
    passwords = {}
    with open("bad-passwords.txt", 'r') as f:
        temp = f.read()
    for line in temp.split("\n"):
        if hash_password(line) not in list(passwords.keys()):
            passwords[hash_password(line)] = line
    return make_json_response(passwords, 200)


@hacker_bp.route("/rainbow-table", methods=["GET"])
def get_scan_rainbow_table():
    passwords = {}

    with open("bad-passwords.txt", 'r') as f:
        temp = f.read()

    for line in temp.split("\n"):
        if hash_password(line) not in list(passwords.keys()):
            passwords[hash_password(line)] = line

    users = User.query.all()

    hits = {}

    for user in users:
        if user.password in list(passwords.keys()):
            hits[user.email] = passwords[user.password]

    return make_json_response(hits, 200)