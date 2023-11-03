from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Workouts(db.Model):
    __tablename__ = 'Workouts'
    workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workout_name = db.Column(db.String(50), nullable=False)
    calorie_count = db.Column(db.BigInteger, nullable=False)

class Exercise(db.Model):
    __tablename__ = 'Exercise'

    exercise_id = db.Column(db.String(50), primary_key=True)
    exercise_name = db.Column(db.String(50), nullable=False)
   
    equipment = relationship('Equipment', secondary=Exercises_have_Equipment, back_populates="exercises")

class Category(db.Model):
    __tablename__ = 'Category'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(50))

class Equipment(db.Model):
    __tablename__ = 'Equipment'

    equipment_id = db.Column(db.String(50), primary_key=True)
   
    equipment_name = db.Column(db.String(50), nullable=False)
    secondary=(Exercises_have_Equipment, back_populates="equipment")

Workouts_have_Exercises = db.Table(
    'Workouts_have_Exercises', db.Model.metadata,
    db.Column('workout_id', db.Integer, db.ForeignKey('Workouts.workout_id')),
    db.Column('exercise_id', db.String(50), db.ForeignKey('Exercise.exercise_id'))
)

Exercises_have_Equipment = db.Table(
    'Exercises_have_Equipment', db.Model.metadata,
    db.Column('equipment_id', db.String(50), db.ForeignKey('Equipment.equipment_id')),
    db.Column('exercise_id', db.String(50), db.ForeignKey('Exercise.exercise_id'))
)

Exercises_have_Categories = db.Table(
    'Exercises_have_Categories', db.Model.metadata,
    db.Column('exercise_id', db.String(50), db.ForeignKey('Exercise.exercise_id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.category_id'))
)

