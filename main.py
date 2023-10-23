'''
File to support entities.
'''
from flask import Flask, render_template, jsonify
import mysql.connector
# from database import db_connect


app = Flask(__name__)

@app.route('/')
def read():
    cnx = mysql.connector.connect(user='root', password='brain5075', host='127.0.0.1', database='world')
    
    cursor = cnx.cursor()
    # cursor = db_connect.connect_to_database()
    
    query = ('SELECT * FROM city')
    cursor.execute(query)
    
    results=cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    