'''
File to support entities.
'''
from flask import Flask, render_template, jsonify, request

import sys
project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'
sys.path.append(project_dir)

from project.models import Workouts, Exercise, Equipment, Category

from project.association import Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories

from flask_sqlalchemy import SQLAlchemy

from project.database import db as db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:brain5075@localhost/exerciseDB'

db.init_app(app)

# add tables to database
#TODO: move this function to create_db.py
with app.app_context():
    db.create_all()

@app.route('/')
def exercise_form():
    return render_template('index.html')

@app.route('/submit_exercise', methods=['POST'])  #TODO: change this after implementing star schema
def submit_exercise():
    if request.method == 'POST':
        data = request.get_json()
        
        #create new entries
        exercise = Exercise(exercise_name=data['exercise_name'])
        equipment = Equipment(equipment_name=data['equipment_name'])
        workout = Workouts(workout_name=data['workout_name'], calorie_count=data['calorie_count'])
        category = Category(category_name=data['category'])
    
        # add entities to database
        add_workout(exercise)      
        add_workout(equipment)
        add_workout(workout)
        add_workout(category)
        commit_workout()
        
        return jsonify({'message': 'Exercise data saved successfully'})
    
def add_workout(table):
    db.session.add(table)
    
def delete_exercise(table):
    db.session.delete(table)

def commit_workout():
    db.session.commit()
    
if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    