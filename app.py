'''
File to support entities.
'''
from flask import Flask, render_template, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/query')
def query():
    cnx = mysql.connector.connect(user='root', password='brain5075', host='127.0.0.1', database='world')
    
    cursor = cnx.cursor()
    
    query = ('SELECT * FROM city')
    cursor.execute(query)
    
    results=cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    results = jsonify(results)
    
    return render_template('index.html')

# @app.route('/')
# def home():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    