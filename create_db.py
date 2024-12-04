import os
import sqlite3

# Paths to directories
problems_dir = "./problems/processed_texts"
solutions_dir = "./solutions"
database_path = "cpr.db"

# Function to create and populate the database
def create_database():
    # Connect to SQLite database (it creates the file if it doesn't exist)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problem_solution_pairs (
            id INTEGER PRIMARY KEY,
            problems TEXT NOT NULL,
            solutions TEXT NOT NULL
        )
    ''')
    
    # Iterate through files in the directories
    for i in range(1, 101):  # Assuming files are numbered 1 to 100
        # Read problem text
        problem_file = os.path.join(problems_dir, f"{i}.txt")
        with open(problem_file, 'r', encoding='utf-8') as pf:
            problem_text = pf.read()
        
        # Read solution text
        solution_file = os.path.join(solutions_dir, f"id{i}.py")
        with open(solution_file, 'r', encoding='utf-8') as sf:
            solution_text = sf.read()
        
        # Insert into the database
        cursor.execute('''
            INSERT INTO problem_solution_pairs (id, problems, solutions)
            VALUES (?, ?, ?)
        ''', (i, problem_text, solution_text))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    print(f"Database created and populated successfully at {database_path}")

# Run the script
if __name__ == "__main__":
    create_database()
