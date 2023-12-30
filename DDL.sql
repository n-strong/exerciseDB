CREATE TABLE Workout(
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


CREATE TABLE Workout_Facts(
    workout_id INT,
    exercise_id INT,
    category_id INT, 
    equipment_id INT,
    FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercises(exercise_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
    PRIMARY KEY(workout_id, exercise_id, category_id, equipment_id)
);
