import mysql.connector

cnx = mysql.connector.connect(user='root', password='brain5075', host='127.0.0.1', database='world')

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE exerciseDB")

cursor.execute('SHOW DATABASES')

for db in cursor:
    print(db)
