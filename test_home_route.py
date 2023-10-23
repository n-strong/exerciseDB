'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''

# import sys
# sys.path.append('/OneDrive/Computer Science/personal projects/exerciseDB')




from main import app
def test_home_route():
    response = app.test_client().get('/')
    print(response)
    
test_home_route()