import json
from flask import Blueprint, request
from models.user import User
from util.util import check_password, make_json_response
from application_configuration.app import db

user_bp = Blueprint(name="user_bp", import_name=__name__)


@user_bp.route("/login", methods=["POST"])
def post_login():
    user = User.query.filter_by(email=request.json["email"]).first()

    if not check_password(request.json["password"], user.password):
        return make_json_response({"status": "error", "body": "incorrect user info"}, 400)

    return make_json_response({"status": "success", "body": "Authenticated. Logging in."}, 200)


@user_bp.route("/register", methods=["POST"])
def post_register():
    if request.json is None:
        return make_json_response({"status": "error", "body": "bad request"}, 400)

    if "email" not in request.json.keys():
        return make_json_response({"status": "error", "body": "bad request"}, 400)

    if "password" not in request.json.keys():
        return make_json_response({"status": "error", "body": "bad request"}, 400)

    if User.query.filter_by(email=request.json["email"]).first() is not None:
        return make_json_response({
            "status": "error",
            "body": "A user with that username already exists!"
        }, 400)

    if "starting_balance" not in request.json.keys():
        user = User(email=request.json["email"],
                    password=request.json["password"])
    else:
        user = User(email=request.json["email"],
                    password=request.json["password"],
                    starting_balance=request.json["starting_balance"])

    db.session.add(user)
    db.session.commit()

    return make_json_response({"status": "success"}, 201)