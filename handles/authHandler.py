import bcrypt
from database import db
from models.model import User
from flask_bcrypt import Bcrypt
from flask_login import login_user

_bcrypt = Bcrypt()


class HandleAuth:
    @staticmethod
    def handleSignup(name,email,password):
        print(name,email,password)
        
        user = User.query.filter_by(email=email).first()
        if(user):
            return "User Already Exists"
        else:
            hashed_pass = _bcrypt.generate_password_hash(password)
            user = User(email=email,password=hashed_pass,name=name)
            db.session.add(user)
            db.session.commit()
            return "User Registered Successfully"
    @staticmethod
    def handleLogin(email,password):
        print(email,password)
        user = User.query.filter_by(email=email).first()
        if(_bcrypt.check_password_hash(user.password,password)):
            login_user(user)
            return "Hey user"
        else:
            return "Invalid Credentials"
    # return "hello"        