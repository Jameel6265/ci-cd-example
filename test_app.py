# test_app.py
from app import greet

def test_greet():
    assert greet("World") == "Hello, World!"
