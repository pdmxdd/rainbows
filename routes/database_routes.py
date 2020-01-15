import json
from flask import Blueprint
from application_configuration.app import db
from util.util import seed_db_with_users, make_json_response

# Must import all models for db.create_all() that is used throughout this file
from models.user import User

database_bp = Blueprint(name="database_bp", import_name=__name__, url_prefix="/database")


@database_bp.route("/seed", methods=["POST"])
def seed_db():
    db.drop_all()
    db.create_all()
    seed_db_with_users()
    return make_json_response({"status": "success"}, 200)


@database_bp.route("/reset", methods=["POST", "GET"])
def reset_db():
    db.drop_all()
    db.create_all()
    return make_json_response({"status": "success", "message": "Database has been reset"}, 200)