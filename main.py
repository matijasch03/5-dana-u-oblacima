from fastapi import FastAPI
from controllers.student_controller import router as student_router
from controllers.canteen_controller import router as canteen_router

app = FastAPI()

app.include_router(student_router)
app.include_router(canteen_router)
