from lib2to3.pgen2.token import GREATER
from typing import final
from unittest import result

from flask import jsonify
from database import db
from models.model import Notes
from collections import ChainMap
from sqlalchemy import select
from database import connection_pool

connection_object = connection_pool.get_connection()


class NotesHandler:
    @staticmethod
    def addNotes(title,desc,tag):
        try:
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
                print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)
                print('fetching Notes')
                print(title,desc,tag)
                notes = Notes.query.all()
                store = []
                _id = 0
                temp = []
                if not notes:
                    _id=1
                for i in notes:
                    store.append(i.__dict__)
                for i in store:
                    temp.append(i['id'])
                print(temp)
                temp.sort(reverse=True)
                _id = temp[0]+1
                print(_id)
                cursor = connection_object.cursor(dictionary=True)
                # note = Notes(id=_id,title=title,desc=desc,tag=tag)
                mySql_insert_query = """INSERT INTO notes (id, title, desc, tag) 
                                VALUES (%s, %s, %s, %s) """
                record = (_id,title ,desc,tag)
                cursor.execute(mySql_insert_query,record)
                id_ = cursor.fetchone()
                return 'Note Added Successfully'
        except:
            print("Error while connecting to MySQL using Connection pool ")
        return "hello"


    @staticmethod
    def fetchNotes():
        try:
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
                print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)
                print('fetching Notes')
                cursor = connection_object.cursor(dictionary=True)
                cursor.execute("SELECT * FROM notes")
                print(cursor.fetchall())
                data = cursor.fetchall()
                return "Data Here"
        # notes = Notes.query.all()
        # store = []
        # result = {}
        # for i in notes:
        #     store.append(i.__dict__)
        # result = store
        # print(notes)
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)
        finally:
            if connection_object.is_connected():
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        return "fetched Data"
            
            

        