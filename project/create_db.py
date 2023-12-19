import pymysql
import sys
project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'
sys.path.append(project_dir)

from project.database import db


# TODO: test if database_name already exists in schema, if not then create database, if yes then skip
def create_app(database_name: str):
    cnx = pymysql.connect(user='root', password='brain5075', host='127.0.0.1')

    cursor = cnx.cursor()

    cursor.execute(f"CREATE DATABASE {database_name}")

    cursor.execute('SHOW DATABASES')
    
    database_list = [db[0] for db in cursor]
    
    # add_tables()
    
    return cursor, database_list



def add_tables():
    db.create_all()

