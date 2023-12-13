'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''
import pytest
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.routes import db, app
from project.models import Exercise, Equipment, Workouts, Category
from project.create_db import create_app

class TestExerciseDatabase:
    
    #adding pytest classes here. Trying to break test framework into smaller units
    # @classmethod
    def test_datebase_creation():
        cursor, database_list = create_app('test_database')
        print(database_list)
        assert 'test_database' in database_list
    
    
    #TODO: trying to create test database
    @pytest.fixture(scope='session')
    def test_app():
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:brain5075@localhost/test_database'
        
        with app.app_context():  # not sure what this does
            yield app
    
    
    #TODO: not sure if this is relevant
    @pytest.fixture
    def client():
        with app.test_client() as client:
            yield client
            

            
    def test_home(client):
        response = client.get('/')
        assert response.status_code == 200 
        assert b'id="exercise-form"' in response.data
            
    def test_database_submission(client):
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
    TestExerciseDatabase.setup()
    # test_home()
    # test_database()
    
    print('All tests successful\n')
    
if __name__ == '__main__':
    main()
    