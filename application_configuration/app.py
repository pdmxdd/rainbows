import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://bank_user:bankuserpass@127.0.0.1:5432/bank"
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_USER']}@{os.environ['DB_USER']}:{os.environ['DB_USER']}/{os.environ['DB_USER']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
