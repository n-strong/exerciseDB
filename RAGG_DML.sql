-- INDEX PAGE
-- SELECT commands for all index.html
SELECT workout_name FROM Workouts WHERE workout_name = ":workoutvariable";

SELECT exercise_name FROM Exercises WHERE exercise_name = "exercises_variable";

SELECT equipment_name FROM Equipment WHERE equipment_name = "equipment_variable";

SELECT body_part_name FROM Categories WHERE body_part_name = "categoryvariable";

SELECT 

-- WORKOUTS PAGE
-- SELECT command for WORKOUTS
SELECT workout_id FROM Workouts WHERE 'SELECT_button_variable'= true;

-- Insertion command for WORKOUTS
INSERT INTO Workouts(workout_name, calorie_count)
VALUES(:workout_name,:calorie_count);

-- Update command for WORKOUTS
UPDATE Workouts
SET workout_name = "update_edit button"
WHERE workout_id = "user_specification_under_edit";

-- DELETE command for WORKOUTS
DELETE FROM Workouts WHERE workout_id = 'DELETE_button_variable';

-- EXERCISES PAGE
-- SELECT command for EXERCISES
SELECT exercise_id FROM Exercises WHERE 'SELECT_button_variable' = true;

-- Insertion command for EXERCISES
INSERT INTO Exercises(exercise_name)
VALUES(:exercise_name);

-- Update command for EXERCISES
UPDATE Exercises
SET exercise_name = "update_edit button"
WHERE exercise_id ="user_specification_under_edit";

-- DELETE command for EXERCISES
DELETE FROM Exercises WHERE exercise_id = 'DELETE_button_variable';

-- CATEGORIES PAGE
-- SELECT command for CATEGORIES
SELECT category_id FROM Category WHERE 'SELECT_button_variable' = true;

-- Insertion command for CATEGORIES
INSERT INTO Category(body_part_name)
VALUES(:body_part_name);

-- Update command for CATEGORIES
UPDATE Category
SET body_part_name = "update_edit button"
WHERE category_id = "user_specification_under_edit";

-- DELETE command for CATEGORIES
DELETE FROM Category WHERE category_id = 'DELETE_button_variable';

-- EQUIPMENT PAGE
-- SELECT command for EQUIPMENT
SELECT equipment_id FROM Equipment WHERE 'SELECT_button_variable' = true;

-- Insertion command for EQUIPMENT
INSERT INTO Equipment(equipment_id, equipment_name)
VALUES(:equipment_id,:equipment_name);

-- Update command for EQUIPMENT
UPDATE Equipment
SET equipment_name = "update_edit button"
WHERE equipment_id = "user_specification_under_edit";

-- DELETE command for EQUIPMENT 
DELETE FROM Equipment WHERE equipment_id = 'DELETE_button_variable';

-- Workouts_have_Exercises table
-- SELECT command for Workouts_have_Exercises
SELECT workout_id, exercise_id
FROM Workouts_have_Exercises
WHERE workout_id = :workout_id;

-- Insertion command for Workouts_have_Exercises
INSERT INTO Workouts_have_Exercises(workout_id, exercise_id)
VALUES (:workout_id, :exercise_id);

-- DELETE command for Workouts_have_Exercises
DELETE FROM Workouts_have_Exercises
WHERE workout_id = :workout_id
  AND exercise_id = :exercise_id;


-- Exercises_have_equipment table
-- SELECT command for Exercises_have_equipment
SELECT exercise_id, equipment_id
FROM Exercises_have_equipment
WHERE exercise_id = :exercise_id;

-- Insertion command for Exercises_have_equipment
INSERT INTO Exercises_have_equipment(exercise_id, equipment_id)
VALUES (:exercise_id, :equipment_id);

-- DELETE command for Exercises_have_equipment
DELETE FROM Exercises_have_equipment
WHERE exercise_id = :exercise_id
  AND equipment_id = :equipment_id;


-- Exercises_have_Categories table
-- SELECT command for Exercises_have_Categories
SELECT exercise_id, category_id
FROM Exercises_have_Categories
WHERE exercise_id = :exercise_id;

-- Insertion command for Exercises_have_Categories
INSERT INTO Exercises_have_Categories(exercise_id, category_id)
VALUES (:exercise_id, :category_id);

-- DELETE command for Exercises_have_Categories
DELETE FROM Exercises_have_Categories
WHERE exercise_id = :exercise_id
  AND category_id = :category_id;

