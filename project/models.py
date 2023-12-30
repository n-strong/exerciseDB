from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
# from project.association import Workouts_have_Exercises, Exercises_have_Equipment, Exercises_have_Categories
import sys

project_dir = r'C:\Users\nsstr\OneDrive\Computer Science\personal projects\exerciseDB'

sys.path.append(project_dir)

from project.database import db as db


#TODO: FUCK THE ORM
    
class Exercise(db.Model):
    __tablename__ = 'Exercise'
    exercise_id = db.Column('exercise_id', db.Integer, primary_key=True, autoincrement=True)
    
    exercise_name = db.Column(db.String(50), nullable=False)
    
    # equipment = relationship('Equipment', secondary=Exercises_have_Equipment, back_populates="exercises")
    
    # workouts=relationship('Workouts', secondary=Workouts_have_Exercises, back_populates='exercises')
    
    # category = relationship('Category', secondary=Exercises_have_Categories, back_populates='exercises')


class Category(db.Model):
    __tablename__ = 'Category'

    category_id = db.Column('category_id',db.Integer, primary_key=True, autoincrement=True)
    
    category_name = db.Column(db.String(50), nullable=True)
    
    # exercises = relationship('Exercise', secondary=Exercises_have_Categories, back_populates='category')
    
    
class Equipment(db.Model):
    __tablename__ = 'Equipment'
    equipment_id = db.Column('equipment_id', db.Integer, primary_key=True, autoincrement=True)
   
    equipment_name = db.Column(db.String(50), nullable=False)
    
    
class Workouts(db.Model):
    __tablename__ = 'Workouts'
    workout_id = db.Column('workout_id', db.Integer, primary_key=True, autoincrement=True)
    workout_name = db.Column(db.String(50), nullable=False)
    calorie_count = db.Column(db.BigInteger, nullable=False)


class WorkoutSessions(db.Model):
    __tablename__ = 'WorkoutSessions'
    workout_id = db.Column(db.Integer, db.ForeignKey('Workouts.workout_id'), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('Exercise.exercise_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.category_id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('Equipment.equipment_id'))

    # Define relationships
    workout = db.relationship('Workouts', backref=db.backref('workout_sessions', cascade='all, delete-orphan'))
    exercise = db.relationship('Exercise', foreign_keys=[exercise_id])
    category = db.relationship('Category', foreign_keys=[category_id])
    equipment = db.relationship('Equipment', foreign_keys=[equipment_id])
    
    

