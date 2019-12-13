import json
from application_configuration.app import app, db
from flask import request
from util.util import make_json_response, hash_password, check_password, seed_db_with_users
from models.user import User


@app.route("/login", methods=["POST"])
def post_login():
    user = User.query.filter_by(email=request.json["email"]).first()

    if not check_password(request.json["password"], user.password):
        return make_json_response(json.dumps({"status": "error", "body": "incorrect user info"}), 400)

    return make_json_response(json.dumps({"status": "success", "body": "Authenticated. Logging in."}), 200)


@app.route("/register", methods=["POST"])
def post_register():
    if request.json is None:
        return make_json_response(json.dumps({"status": "error", "body": "bad request"}), 400)

    if "email" not in request.json.keys():
        return make_json_response(json.dumps({"status": "error", "body": "bad request"}), 400)

    if "password" not in request.json.keys():
        return make_json_response(json.dumps({"status": "error", "body": "bad request"}), 400)

    if User.query.filter_by(email=request.json["email"]).first() is not None:
        return make_json_response(json.dumps({
            "status": "error",
            "body": "A user with that username already exists!"
        }), 400)

    if "starting_balance" not in request.json.keys():
        user = User(email=request.json["email"],
                    password=request.json["password"])
    else:
        user = User(email=request.json["email"],
                    password=request.json["password"],
                    starting_balance=request.json["starting_balance"])

    db.session.add(user)
    db.session.commit()

    return make_json_response(json.dumps({"status": "success"}), 201)


@app.route("/seed-db", methods=["POST"])
def seed_db():
    db.drop_all()
    db.create_all()
    seed_db_with_users()
    return make_json_response(json.dumps({"status": "success"}), 200)


@app.route("/breach-database", methods=["POST"])
def breach_database():
    users = User.query.all()

    return make_json_response(json.dumps({
        "users": [user.to_dict() for user in users]
    }), 200)


@app.route("/rainbow", methods=["GET"])
def get_rainbow_table():
    passwords = {}
    with open("bad-passwords.txt", 'r') as f:
        temp = f.read()
    for line in temp.split("\n"):
        if hash_password(line) not in list(passwords.keys()):
            passwords[hash_password(line)] = line
    return make_json_response(json.dumps(passwords), 200)


@app.route("/rainbow-table", methods=["GET"])
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

    return make_json_response(json.dumps(hits), 200)


@app.route("/reset-db", methods=["POST", "GET"])
def reset_db():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=8888)
