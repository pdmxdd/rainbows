import json
from application_configuration.app import app, db
from flask import request
from util.util import make_json_response, hash_password
from models.user import User
from scripts.seed_db import seed_db_with_users


@app.route("/register", methods=["POST"])
def post_register():
    if request.json is None:
        return make_json_response(json.dumps({"status": "error", "body": "bad request"}), 400)

    if "email" not in request.json.keys():
        return make_json_response(json.dumps({"status": "error", "body": "bad request"}), 400)

    if User.query.filter_by(email=request.json["email"]).first() is not None:
        return make_json_response(json.dumps({
            "status": "error",
            "body": "A user with that username already exists!"
        }), 400)

    user = User(email=request.json["email"],
                password=hash_password(request.json["password"]))

    db.session.add(user)
    db.session.commit()

    return make_json_response(json.dumps({"status": "success"}), 201)


@app.route("/seed-db", methods=["GET", "POST"])
def seed_db():
    seed_db_with_users()
    return make_json_response(json.dumps({"status": "success"}), 200)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True, port=8888)
