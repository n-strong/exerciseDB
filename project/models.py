from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from association import Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories

from database import db as db

class Workouts(db.Model):
    __tablename__ = 'Workouts'
    workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workout_name = db.Column(db.String(50), nullable=False)
    calorie_count = db.Column(db.BigInteger, nullable=False)
    
    exercises = relationship('Exercise', secondary=Workouts_have_Exercises, back_populates='workouts')    
    
class Exercise(db.Model):
    __tablename__ = 'Exercise'

    exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(db.String(50), nullable=False)
    
    equipment = relationship('Equipment', secondary=Exercises_have_Equipment, back_populates="exercises")
    
    workouts=relationship('Workouts', secondary=Workouts_have_Exercises, back_populates='exercises')
    
    category = relationship('Category', secondary=Exercises_have_Categories, back_populates='exercises')

class Category(db.Model):
    __tablename__ = 'Category'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(50))
    
    exercises = relationship('Exercise', secondary=Exercises_have_Categories, back_populates='category')
    
    
class Equipment(db.Model):
    __tablename__ = 'Equipment'
    equipment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   
    equipment_name = db.Column(db.String(50), nullable=False)
    exercises = relationship('Exercise',
    secondary=Exercises_have_Equipment, back_populates="equipment")

