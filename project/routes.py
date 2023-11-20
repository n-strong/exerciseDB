'''
File to support entities.
'''
from flask import Flask, render_template, jsonify, request

from project.models import Workouts, Exercise, Equipment, Category

from project.association import Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories

from flask_sqlalchemy import SQLAlchemy

from project.database import db as db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:brain5075@localhost/exerciseDB'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def exercise_form():
    return render_template('index.html')

@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    if request.method == 'POST':
        data = request.get_json()
        
        #create new entries
        exercise = Exercise(exercise_name=data['exercise_name'])
        equipment = Equipment(equipment_name=data['equipment_name'])
        workout = Workouts(workout_name=data['workout_name'], calorie_count=data['calorie_count'])
        category = Category(category_name=data['category'])
        
        # many to many relationships
        exercise.equipment.append(equipment)
        workout.exercises.append(exercise)
        exercise.category.append(category)

        db.session.add(exercise)
        db.session.add(equipment)
        db.session.add(workout)
        db.session.add(category)
        db.session.commit()
        
        return jsonify({'message': 'Exercise data saved successfully'})
        
if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    