import MySQLdb
import os
import db_credentials

host = db_credentials.host
user = db_credentials.user
passwd = db_credentials.passwd
db = db_credentials.db

def connect_to_database(host = host, user = user, passwd = passwd, db = db):
    db_connection = MySQLdb.connect(host, user, passwd, db)
    return db_connection
