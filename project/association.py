from database import db as db

Workouts_have_Exercises = db.Table(
    'Workouts_have_Exercises', db.Model.metadata,
    db.Column('workout_id', db.Integer, db.ForeignKey('Workouts.workout_id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.exercise_id'))
)

Exercises_have_Equipment = db.Table(
    'Exercises_have_Equipment', db.Model.metadata,
    db.Column('equipment_id', db.Integer, db.ForeignKey('Equipment.equipment_id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.exercise_id'))
)

Exercises_have_Categories = db.Table(
    'Exercises_have_Categories', db.Model.metadata,
    db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.exercise_id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.category_id'))
)
