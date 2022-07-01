from crypt import methods
import email
from genericpath import sameopenfile
from pickle import TRUE
from unicodedata import name
from flask import Blueprint
from flask import Flask, request
from flask_login import UserMixin
from models.model import User
from database import db
from route.auth import _auth_
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saurabh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(_auth_, url_prefix="/auth")

class SampleService:
    def process(self):
        user = User(email="saurabhkr733909@gmail.com",password="Hello123",name="saurabh")
        db.session.add(user)
        db.session.commit()
        return 'Hello, World!'


@app.route('/')
def hello_world():
    sample_service = SampleService()
    return sample_service.process()




if __name__ == "__main__":
    app.run(debug=True)