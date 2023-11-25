'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''
import os
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.routes import app, db
from project.models import Exercise, Equipment, Workouts, Category

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200 
        assert b'id="exercise-form"' in response.data
        
def test_database():
    with app.test_client() as client:
        test_data = {
            'exercise_name': 'Incline Bench Press',
            'equipment_name': 'Barbell',
            'workout_name': 'Push Day',
            'calorie_count': 100,
            'category': 'Chest'
        }
        
        response = client.post('/submit_exercise', json=test_data)
        
        assert response.status_code == 200
        assert response.json['message'] == 'Exercise data saved successfully'
        
        
        exercise = Exercise.query.filter_by(exercise_name = 'Incline Bench Press').first()
        equipment = Equipment.query.filter_by(equipment_name = 'Barbell').first()
        workout = Workouts.query.filter_by(workout_name = 'Push Day').first()        
        category = Category.query.filter_by(category_name = 'Chest').first()
        
        assert exercise is not None
        assert equipment is not None
        assert workout is not None
        assert category is not None

        # Deleting the records added during the test
        db.session.delete(exercise)
        db.session.delete(equipment)
        db.session.delete(workout)
        db.session.delete(category)
        db.session.commit()

        # Ensure the records are deleted
        assert Exercise.query.filter_by(exercise_name='Incline Bench Press').first() is None
        assert Equipment.query.filter_by(equipment_name='Barbell').first() is None
        assert Workouts.query.filter_by(workout_name='Push Day').first() is None
        assert Category.query.filter_by(category_name='Chest').first() is None
        
def main():
    test_home()
    test_database()
    
    print('All tests successful\n')
    
if __name__ == '__main__':
    main()
    