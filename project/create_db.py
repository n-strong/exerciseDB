import pymysql
import sys
project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'
sys.path.append(project_dir)
from flask import Flask
from project.database import db

port = '3306'


# TODO: commenting this out causes NameError
# da  tabase_name = 'exercisedb'
def is_test_database_or_not(input_database_name='exercisedb'):
    return input_database_name

database_name = is_test_database_or_not()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://root:brain5075@localhost:{port}/{database_name}'
db.init_app(app)

# establish connection to database
def establish_connection():
    cnx = pymysql.connect(user='root', 
                          password='brain5075', 
                          host='127.0.0.1', 
                          port=int(port)) 
    cursor = cnx.cursor()
    return cnx, cursor

# close connection to database
def close_connection(cnx, cursor):
    cursor.close()
    cnx.close()

# create database instance
def create_app(database_name: str):
    cnx, cursor = establish_connection()
    
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        add_tables()
    finally:
        close_connection(cnx, cursor)

# check if database is already created
def check_db(database_name: str):
    cnx, cursor = establish_connection()
    cursor.execute('SHOW DATABASES')
    database_list = [db[0] for db in cursor]
    close_connection(cnx, cursor)
    
    if database_name in database_list:
        return True
    
    return False

def add_tables():
    with app.app_context():
        db.create_all()

def add_entry(table):
    db.session.add(table)

def delete_entry(table, col, entry):
    cnx, cursor = establish_connection()
    try:
        cursor.execute(f'DELETE FROM {table} WHERE {col} = {entry}')
    finally:
        close_connection(cnx, cursor)

# delete database
def delete_database(database_name):
    cnx, cursor = establish_connection()
    
    try:
        cursor.execute(f'DROP DATABASE {database_name}')
    finally:
        close_connection(cnx, cursor)

