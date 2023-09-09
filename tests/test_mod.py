'''
This is the test suite for the exerciseDB web app backend that uses Flask.
'''

import unittest
from app import *
from app.app import create_app, db

class TestUserModel(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = create_app(config='testing')