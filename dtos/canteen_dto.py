from typing import List
from pydantic import BaseModel
from model.models import WorkingHour


class CanteenCreate(BaseModel):
    name: str
    location: str
    capacity: int
    workingHours: List[WorkingHour]
