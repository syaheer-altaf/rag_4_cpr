import os
import sqlite3

# paths to directories
problems_dir = "./problems/processed_texts"
solutions_dir = "./solutions"
database_path = "cpr.db"

# function to create and populate the database
def create_database():
    # connect to SQLite database (it creates the file if it doesn't exist)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problem_solution_pairs (
            id INTEGER PRIMARY KEY,
            problems TEXT NOT NULL,
            solutions TEXT NOT NULL
        )
    ''')
    
    # get list of problem files in the directory
    problem_files = sorted(os.listdir(problems_dir))  # get all files and sort them
    
    for problem_file in problem_files:
        if problem_file.endswith(".txt"):  # ensure it's a text file
            problem_id = os.path.splitext(problem_file)[0]  # extract file name without extension
            
            # read problem text
            with open(os.path.join(problems_dir, problem_file), 'r', encoding='utf-8') as pf:
                problem_text = pf.read()
            
            # read corresponding solution text
            solution_file = f"id{problem_id}.py"
            solution_path = os.path.join(solutions_dir, solution_file)
            
            if os.path.exists(solution_path):
                with open(solution_path, 'r', encoding='utf-8') as sf:
                    solution_text = sf.read()
                
                # insert into the database
                cursor.execute('''
                    INSERT INTO problem_solution_pairs (id, problems, solutions)
                    VALUES (?, ?, ?)
                ''', (problem_id, problem_text, solution_text))
    
    # commit and close connection
    conn.commit()
    conn.close()
    print(f"Database created and populated successfully at {database_path}")


if __name__ == "__main__":
    create_database()