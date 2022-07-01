from lib2to3.pgen2.token import GREATER
from unittest import result

from flask import jsonify
from database import db
from models.model import Notes
from collections import ChainMap
from sqlalchemy import select

class NotesHandler:
    @staticmethod
    def addNotes(title,desc,tag):
        print(title,desc,tag)
        notes = Notes.query.all()
        store = []
        temp = []
        for i in notes:
            store.append(i.__dict__)
        for i in store:
            temp.append(i['id'])
        print(temp)
        temp.sort(reverse=True)
        _id = temp[0]+1
        print(_id)
        note = Notes(id=_id,title=title,desc=desc,tag=tag)
        db.session.add(note)
        db.session.commit()
        return 'Note Added Successfully'

    @staticmethod
    def fetchNotes():
        print('fetching Notes')
        notes = Notes.query.all()
        store = []
        result = {}
        for i in notes:
            store.append(i.__dict__)
        result = store
        return result