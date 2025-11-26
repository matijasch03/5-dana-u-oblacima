from pydantic import BaseModel
from typing import List
from datetime import date, time

from enums import *


class Student(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    is_admin: bool

class WorkingHour(BaseModel):
    meal: Meal
    start_time: time
    end_time: time

class Canteen(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    working_hours: List[WorkingHour]
    is_opened: bool

class Reservation(BaseModel):
    id: int
    student_id: int
    canteen_id: int
    date: date
    start_time: time
    duration_minutes: int
    status: ReservationStatus
