from pydantic import BaseModel
from typing import List
from datetime import date, time

from model.enums import Meal, ReservationStatus


class Student(BaseModel):
    id: str
    name: str
    email: str
    is_admin: bool

class WorkingHour(BaseModel):
    meal: Meal
    start_time: time
    end_time: time

class Canteen(BaseModel):
    id: str
    name: str
    location: str
    capacity: int
    working_hours: List[WorkingHour]
    is_opened: bool

class Reservation(BaseModel):
    id: str
    student_id: str
    canteen_id: str
    date: date
    start_time: time
    duration_minutes: int
    status: ReservationStatus
