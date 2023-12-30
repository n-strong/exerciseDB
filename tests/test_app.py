'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''
import pytest
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.routes import db
from project.models import Exercise, Equipment, Workouts, Category, WorkoutSessions
from project.create_db import create_app, check_db, delete_database, delete_entry, port, app, is_test_database_or_not


database_name = is_test_database_or_not('test_database')


def test_create_app():
    create_app(database_name)
    assert check_db(database_name) is True


@pytest.fixture(scope='session')
def test_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://root:brain5075@localhost:{port}/{database_name}'
    
    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def test_client(test_app):
    with test_app.test_client() as client:
        yield client


@pytest.fixture
def response(test_client):
    return test_client.get('/')

def test_status_code(response):
    assert response.status_code == 200 
    
def test_home(response):
    assert b'id="exercise-form"' in response.data

        
def test_database_submission(test_client):
    test_data = {
        'exercise_name': 'Incline Bench Press',
        'equipment_name': 'Barbell',
        'workout_name': 'Push Day',
        'calorie_count': 100,
        'category': 'Chest'
    }
    
    response = test_client.post('/submit_exercise', json=test_data)

    assert response.json['message'] == 'Exercise data saved successfully'
 

def test_exercise_submission():
    exercise = Exercise.query.filter_by(exercise_name = 'Incline Bench Press').first()
    assert exercise.exercise_name == 'Incline Bench Press'

def test_equipment_submission():
    equipment = Equipment.query.filter_by(equipment_name = 'Barbell').first()
    assert equipment.equipment_name == 'Barbell'

def test_workout_submission():
    workout = Workouts.query.filter_by(workout_name = 'Push Day').first()
    assert workout.workout_name == 'Push Day'  and workout.calorie_count == 100

def test_category_submission():
    category = Category.query.filter_by(category_name = 'Chest').first()
    assert category.category_name == 'Chest'

# TODO: test to delete entry in database
# def test_delete_exercise():
#     exercise = Exercise.query.filter_by(exercise_name = 'Incline Bench Press').first()
#     delete_entry('Exercise', 'exercise_name', exercise.exercise_name)
#     exercise = Exercise.query.filter_by(exercise_name = 'Incline Bench Press').first()
#     assert exercise.exercise_name is None


# TODO: test entries are being added to production database when they shouldn't be

# def test_delete_database():
#     delete_database(database_name)
#     assert check_db(database_name) is False
        
if __name__ == '__main__':
    pytest.main()
    