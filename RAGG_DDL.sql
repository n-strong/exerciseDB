-- Authors:Noah Strong and Anthony Frusti
-- Create the database for RogueAgentsGlobal 
-- Table structure for Workouts entity and necessary attributes

CREATE TABLE Workouts (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    workout_name VARCHAR(50) NOT NULL,
    -- Use BIGINT UNSIGNED to allow for large positive integers in calore_count
    calorie_count BIGINT UNSIGNED NOT NULL
);
-- Table structure for Exercises entity
CREATE TABLE Exercise(
    exercise_id VARCHAR(50) PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL
);
-- Table structure for BodyPart entity and necessary attributes
CREATE TABLE Category(
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50)
);

-- Table structure for Equipment entity and necessary attributes
CREATE TABLE Equipment(
    equipment_id VARCHAR(50) PRIMARY KEY,
    equipment_name VARCHAR(50) NOT NULL
);

-- Table structure for Workouts_have_Exercises
CREATE TABLE Workouts_have_Exercises (
    workout_id INT,
    exercise_id VARCHAR(50),
    FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id),
    PRIMARY KEY (workout_id, exercise_id)
);

-- Table structure for Exercises_have_Equipment
CREATE TABLE Exercises_have_Equipment(
    equipment_id varchar(50),
    exercise_id varchar(50),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id),
    PRIMARY KEY (equipment_id, exercise_id)
);

-- Table structure for Exercises_have_Equipment
CREATE TABLE Exercises_have_Categories(
    exercise_id VARCHAR(50),
    category_id INT,
    FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    PRIMARY KEY (exercise_id, category_id)
);

-- Insertion command into workouts
INSERT INTO Workouts(workout_name, calorie_count)
VALUES("Chest and Tri", 1500),("Back and Bi", 1300), ("Legs", 1500), ("Cardio is hardio", 2000), ("Core power", 1750);

-- Insertion command into category
INSERT INTO Categories(body_part_id, body_part_name)
VALUES("CA-02","Chest+ arms"), ("BA-02","Back+arms"), ("CaT-03","Calves+thighs"), ("H-07","Heart"), ("A-06", "Abs");

-- Insertion command into equipment
INSERT INTO Equipment(equipment_id,equipment_name)
VALUES("E-02","bench press"), ("E-01","olympic row"), ("E-03","squat rack"), ("E-06","stationary bike"), ("B-00","body work");

-- Insertion command into Exercises
INSERT INTO Exercises(exercise_id, exercise_name)
VALUES("UF-001","bench press"), ("UB-001","Row"), ("L-001","Squat"), ("C-001","Elliptical bike"), ("A-001","Crunches");