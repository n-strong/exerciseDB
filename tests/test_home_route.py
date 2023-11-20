'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''
import os
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.routes import app

def test_get_exercise_form():
    with app.test_client() as client:
        response = client.get('/')
        
        assert response.status_code == 200
                
        assert b'id="exercise-form"' in response.data
    
if __name__ == '__main__':
    test_get_exercise_form()