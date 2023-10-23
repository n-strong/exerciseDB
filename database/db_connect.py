import mysql.connector
from database import db_credentials
from dotenv import load_dotenv, find_dotenv

host = db_credentials.host
user = db_credentials.user
passwd = db_credentials.passwd
db = db_credentials.db

def connect_to_database(host = host, user = user, passwd = passwd, db = db):
    cnx = mysql.connector.connect(user, passwd, host, db)
    
    cursor = cnx.cursor()
    
    return cursor

