from server import db
from useful_functions import *
from datetime import datetime


# Create the Users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    salt = db.Column(db.String(64), unique=True, nullable=False)
    salted_password_hash = db.Column(db.String(64), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.now)  # %Y-%m-%d %H:%M:%S.%f

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email.lower()
        self.salt = sha256(self.email)
        self.salted_password_hash = sha256(self.salt + password)

    def __repr__(self):
        return "<Name %r>" % (self.first_name + " " + self.last_name)






