'''
File to support entities.
'''
from flask import Flask, render_template, jsonify, request

import sys
project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'
sys.path.append(project_dir)

# from project.association import Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories

# from flask_sqlalchemy import SQLAlchemy


from project.create_db import create_app, check_db, app, database_name, add_entry

if not check_db(database_name):
    create_app(database_name)

@app.route('/')
def exercise_form():
    return render_template('index.html')

@app.route('/submit_exercise', methods=['POST'])  #TODO: change this after implementing star schema
def submit_exercise():
    if request.method == 'POST':
        data = request.get_json()

        #create new entries
        exercise = ['Exercise', 'exercise_name', data['exercise_name']]
        equipment = ['Equipment', 'equipment_name', data['equipment_name']]
        workout = ['Workout', ['workout_name', 'calorie_count'], [data['workout_name'], data['calorie_count']]]
        category = ['Category', 'category_name', data['category_name']]
    
        # add entities to database
        add_entry(*exercise)      
        add_entry(*equipment)
        add_entry(*workout)
        add_entry(*category)
        
        
        return jsonify({'message': 'Exercise data saved successfully'})


# TODO: add this to create_app
def commit_workout():
    db.session.commit()
    
if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    