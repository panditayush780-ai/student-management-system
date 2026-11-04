# get
#post
# delete

from fastapi import FastAPI, HTTPException
import database
from models import Student, StudentCreate

app = FastAPI(title="Student Management System API", description="A simple API to manage students", version="1.0.0")
database.init_db()  #initialize the database when the app starts

@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    student_id = database.add_student(student.name, student.age, student.grade, student.marks)
    return Student(id=student_id, **student.model_dump()) # {"name": "John Doe", "age": 20, "grade": "A", "marks": 85}

@app.get("/students", response_model=list[Student])
def list_students():
    return [dict(row) for row in database.get_students()]

@app.delete("/students/{student_id}", status_code=204)
def remove_student(student_id: int):
    if not database.delete_student(student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}


#200 ,201,204
# 400,401,403 .... error
#500, 502, 503, 504 ->server errors