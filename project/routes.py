'''
File to support entities.
'''
from flask import Flask, render_template, jsonify, request

from models import Workouts, Exercise, Equipment, Category, Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:brain5075@localhost/exerciseDB'

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
        workout = Workouts(workout_name=data['exercise_type'], calorie_count=data['calorie_count'])
        
        # many to many relationships
        exercise.equipment.append(equipment)
        workout.exercises.append(exercise)

        db.session.add(exercise)
        db.session.add(equipment)
        db.session.add(workout)
        db.session.commit()
        
        return jsonify({'message': 'Exercise data saved successfully'})
        
if __name__ == '__main__':
    app.run(port=3309, debug=True)
    
    