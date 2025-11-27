from fastapi import HTTPException, APIRouter
from dtos.student_dto import StudentCreate
from model.models import Student
from data_base.shared import students

import re


router = APIRouter(prefix="/students", tags=["Students"])
student_counter = 0
email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

def is_valid_email(email: str) -> bool:
    return re.match(email_regex, email) is not None


@router.post("", status_code=201, response_model=Student)
def create_student(student: StudentCreate):
    global student_counter

    if not is_valid_email(student.email):
        raise HTTPException(status_code=422, detail="Invalid email format")

    # email must be unique
    for s in students:
        if s["email"] == student.email:     # newly created student is dict - look at line 28
            raise HTTPException(status_code=400, detail="Email already exists")

    new_student = {
        "id": str(student_counter),
        "name": student.name,
        "email": student.email,
        "isAdmin": student.isAdmin
    }
    student_counter += 1

    students.append(new_student)
    return new_student


@router.get("/{id}", status_code=200, response_model=Student)
def get_student(id: str):
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
