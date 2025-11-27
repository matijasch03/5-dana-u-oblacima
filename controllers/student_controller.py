from fastapi import FastAPI, HTTPException

from dtos.student_dto import StudentCreate


students = []
student_counter = 0
app = FastAPI()

@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    global student_counter

    # email must be unique
    for s in students:
        if s["email"] == student.email:
            raise HTTPException(status_code=400, detail="Email already exists.")

    new_student = {
        "id": str(student_counter),
        "name": student.name,
        "email": student.email,
        "isAdmin": student.isAdmin
    }
    student_counter += 1

    students.append(new_student)
    return new_student