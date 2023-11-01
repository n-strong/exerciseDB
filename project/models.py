from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Workouts table
class Workouts(Base):
    __tablename__ = 'Workouts'

    workout_id = Column(Integer, primary_key=True, autoincrement=True)
    workout_name = Column(String(50), nullable=False)
    calorie_count = Column(Integer, nullable=False)

# Define the Exercise table
class Exercise(Base):
    __tablename__ = 'Exercise'

    exercise_id = Column(String(50), primary_key=True)
    exercise_name = Column(String(50), nullable=False)

# Define the Category table
class Category(Base):
    __tablename__ = 'Category'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50))

# Define the Equipment table
class Equipment(Base):
    __tablename__ = 'Equipment'

    equipment_id = Column(String(50), primary_key=True)
    equipment_name = Column(String(50), nullable=False)

# Define the Workouts_have_Exercises association table
Workouts_have_Exercises = Table(
    'Workouts_have_Exercises', Base.metadata,
    Column('workout_id', Integer, ForeignKey('Workouts.workout_id')),
    Column('exercise_id', String(50), ForeignKey('Exercise.exercise_id')),
)

# Define the Exercises_have_Equipment association table
Exercises_have_Equipment = Table(
    'Exercises_have_Equipment', Base.metadata,
    Column('equipment_id', String(50), ForeignKey('Equipment.equipment_id')),
    Column('exercise_id', String(50), ForeignKey('Exercise.exercise_id')),
)

# Define the Exercises_have_Categories association table
Exercises_have_Categories = Table(
    'Exercises_have_Categories', Base.metadata,
    Column('exercise_id', String(50), ForeignKey('Exercise.exercise_id')),
    Column('category_id', Integer, ForeignKey('Category.category_id')),
)

# You can create a database engine like this:
# engine = create_engine('mysql://your_username:your_password@localhost/your_database')

# To use these models, create an SQLAlchemy session and interact with the database.
# Example of creating a new Workout:
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# new_workout = Workouts(workout_name="Sample Workout", calorie_count=500)
# session.add(new_workout)
# session.commit()
