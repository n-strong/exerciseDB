import pytest

from project.app import create_app, db

@pytest.fixture()
def app():
    app = create_app("sqlite://")
    
