#sqlite3 ->python inbuilt module for sqlite3 database


import sqlite3

DB_NAME = "student.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  #lets us access columns by name instead of index
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS students(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         age INTEGER NOT NULL,
                         grade TEXT NOT NULL,
                         marks INTEGER NOT NULL
                     )
                     """)
        
def add_student(name, age, grade, marks)->int:
    with get_connection() as conn:
        cursor = conn.execute("""
                              INSERT INTO students(name, age, grade, marks) VALUES (?, ?, ?, ?)
                              """, (name, age, grade, marks))
        return cursor.lastrowid
    
def get_students():
    with get_connection() as conn:
            return conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
        
def delete_student(student_id) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        return cursor.rowcount > 0  #returns True if a row was deleted, False otherwise
    
    
# cursor.rowcount ->how many rows were affected by that query

# 123 -> False

# 2 -> True