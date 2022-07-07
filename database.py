import sqlalchemy

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from mysql.connector import pooling

db = SQLAlchemy()

connection_pool = pooling.MySQLConnectionPool(pool_name="first_pool",pool_size=5,pool_reset_session=True ,database="Notes",user="root",password="",host="localhost")
