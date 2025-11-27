from pydantic import BaseModel, Field
from typing import List
from datetime import date, time

from model.enums import Meal, ReservationStatus


class Student(BaseModel):
    id: str
    name: str
    email: str
    isAdmin: bool

class WorkingHour(BaseModel):
    meal: Meal
    start: time = Field(..., alias="from")
    to: time

class Canteen(BaseModel):
    id: str
    name: str
    location: str
    capacity: int
    workingHours: List[WorkingHour]

class Reservation(BaseModel):
    id: str
    student_id: str
    canteen_id: str
    date: date
    start_time: time
    duration_minutes: int
    status: ReservationStatus
