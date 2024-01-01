create_table_queries = {
    'create_Workout_table': '''
        CREATE TABLE IF NOT EXISTS Workout (
            workout_id INT AUTO_INCREMENT PRIMARY KEY,
            workout_name VARCHAR(50) NOT NULL,
            calorie_count BIGINT UNSIGNED NOT NULL
        )
    ''',
    'create_Exercise_table': '''
        CREATE TABLE IF NOT EXISTS Exercise (
            exercise_id INT AUTO_INCREMENT PRIMARY KEY,
            exercise_name VARCHAR(50) NOT NULL
        )
    ''',
    'create_Category_table': '''
        CREATE TABLE IF NOT EXISTS Category (
            category_id INT AUTO_INCREMENT PRIMARY KEY,
            category_name VARCHAR(50)
        )
    ''',
    'create_Equipment_table': '''
        CREATE TABLE IF NOT EXISTS Equipment (
            equipment_id INT AUTO_INCREMENT PRIMARY KEY,
            equipment_name VARCHAR(50) NOT NULL
        )
    ''',
    'create_Workout_Facts_table': '''
        CREATE TABLE IF NOT EXISTS Workout_Facts (
            fact_id INT AUTO_INCREMENT PRIMARY KEY,
            workout_id INT,
            exercise_id INT,
            category_id INT,
            equipment_id INT,
            FOREIGN KEY (workout_id) REFERENCES Workout(workout_id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id),
            FOREIGN KEY (category_id) REFERENCES Category(category_id),
            FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
        )
    '''
}