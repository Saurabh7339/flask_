from database import db
from models.model import User

class HandleAuth:
    @staticmethod
    def handleSignup(name,email,password):
        print(name,email,password)
        
        user = User.query.filter_by(email=email).first()
        if(user):
            return "User Already Exists"
        else:
            user = User(email=email,password=password,name=name)
            db.session.add(user)
            db.session.commit()
            return "User Registered Successfully"