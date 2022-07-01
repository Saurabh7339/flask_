from crypt import methods
from os import name
from turtle import title
from flask import Flask, request,flash
from flask import Blueprint
from sqlalchemy import null

from handles.notesHandler import NotesHandler

_notes_ = Blueprint("notes",__name__)
handle_notes = NotesHandler

@_notes_.route('/',methods=['GET'])
def fetch_notes():
    return handle_notes.fetchNotes()

@_notes_.route('/add',methods=['POST'])
def add_notes():
    if((request.form.get('title')=="" ) or request.form.get('desc')==""):
        return 'please provide sufficient data'
    else:
        title = request.form.get('title')
        desc = request.form.get('desc')
        tag = request.form.get('tag')
        return handle_notes.addNotes(title,desc,tag)
    return "hey"
