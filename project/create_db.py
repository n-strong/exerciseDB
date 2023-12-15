import mysql.connector
from database import db

def create_app(database_name: str):
    cnx = mysql.connector.connect(user='root', password='brain5075', host='127.0.0.1')

    cursor = cnx.cursor()

    cursor.execute(f"CREATE DATABASE {database_name}")

    cursor.execute('SHOW DATABASES')
    
    database_list = [db[0] for db in cursor]
    
    # add_tables()
    
    return cursor, database_list



def add_tables():
    db.create_all()

