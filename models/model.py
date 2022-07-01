from enum import unique
from database import db

class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Notes(db.Model):
    id  = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200),unique=True)
    desc = db.Column(db.String(2000))
    tag = db.Column(db.String(100))