import datetime
from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0)
    grade: str = Field(min_length=1, max_length=50)
    marks: int = Field(default=0, ge=0, le=100)  # Assuming marks are between 0 and 100

class Student(StudentCreate):
    id: int