from fastapi import FastAPI, HTTPException
from model.models import Student


students = []
app = FastAPI()

@app.post("/students", status_code=201)
def create_student(data: Student):

    # email and ID must be unique
    for s in students:
        if s["email"] == data.email:
            raise HTTPException(status_code=400, detail="Email already exists.")

        if s["id"] == data.id:
            raise HTTPException(status_code=400, detail="ID already exists.")

    new_student = {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "is_admin": data.is_admin
    }

    students.append(new_student)
    return new_student