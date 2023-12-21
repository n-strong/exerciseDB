import pymysql
import sys
project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'
sys.path.append(project_dir)

from project.database import db

def establish_connection():
    cnx = pymysql.connect(user='root', password='brain5075', host='127.0.0.1')

    cursor = cnx.cursor()
    return cursor


def create_app(database_name: str):
    cursor = establish_connection()
    cursor.execute(f"CREATE DATABASE {database_name}")


def check_db(database_name: str):
    cursor = establish_connection()
    cursor.execute('SHOW DATABASES')
    
    database_list = [db[0] for db in cursor]
    
    if database_name in database_list:
        return True
    
    return False



def add_tables():
    db.create_all()

