from crypt import methods
from os import name
from handles.authHandler import HandleAuth
from flask import Flask, request
from flask import Blueprint

_auth_  = Blueprint("auth",__name__)    
authHandler  = HandleAuth()

@_auth_.route("/signup",methods=["POST"])
def handle_signup():
    email  = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    return authHandler.handleSignup(name=name,email=email,password=password)

@_auth_.route('/login',methods=['POST'])
def handle_login():
    email = request.form.get('email')
    password  = request.form.get('password')
    return authHandler.handleLogin(email=email,password=password)

@_auth_.route("/")
def test():
    return "hello"