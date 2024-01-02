'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''
import pytest
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.create_db import create_app, create_db, check_db, delete_database, delete_entry, port, is_test_database_or_not


database_name = is_test_database_or_not('test_database')


# def test_create_db():
#     create_db(database_name)
#     assert check_db(database_name) is True

# TODO: getting 404 error and not sure why. I think it's somewhere herer
@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    # app_context = app.app_context()    
    
    # app_context.push()
    with app.app_context():
        yield app
    
    # app_context.pop()

@pytest.fixture(scope='session')
def test_client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def response(test_client):
    return test_client.get('/')

def test_status_code(response):
    assert response.status_code == 200 
    
# def test_home(response):
#     assert b'id="exercise-form"' in response.data

        
# def test_database_submission(test_client):
#     test_data = {
#         'exercise_name': 'Incline Bench Press',
#         'equipment_name': 'Barbell',
#         'workout_name': 'Push Day',
#         'calorie_count': 100,
#         'category': 'Chest'
#     }
    
#     response = test_client.post('/submit_exercise', json=test_data)

#     assert response.json['message'] == 'Exercise data saved successfully'
 

# def test_exercise_submission():
#     exercise = Exercise.query.filter_by(exercise_name = 'Incline Bench Press').first()
#     assert exercise.exercise_name == 'Incline Bench Press'

# def test_equipment_submission():
#     equipment = Equipment.query.filter_by(equipment_name = 'Barbell').first()
#     assert equipment.equipment_name == 'Barbell'

# def test_workout_submission():
#     workout = Workouts.query.filter_by(workout_name = 'Push Day').first()
#     assert workout.workout_name == 'Push Day'  and workout.calorie_count == 100

# def test_category_submission():
#     category = Category.query.filter_by(category_name = 'Chest').first()
#     assert category.category_name == 'Chest'

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
    