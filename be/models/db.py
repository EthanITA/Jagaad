import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://myuser:mypassword@localhost:5432/mydb"

db = SQLAlchemy(app)
