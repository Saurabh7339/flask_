from crypt import methods
import email
from genericpath import sameopenfile
from pickle import TRUE
from sys import implementation
from unicodedata import name
from flask import Blueprint
from flask import Flask, request
from flask_login import UserMixin,LoginManager
from models.model import User
from database import db
from route.auth import _auth_
from route.notes import _notes_
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
login_manager = LoginManager()
app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saurabh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
db.init_app(app)
with app.app_context():
    db.create_all()
login_manager.init_app(app)

app.register_blueprint(_auth_, url_prefix="/auth")
app.register_blueprint(_notes_,url_prefix="/notes")

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