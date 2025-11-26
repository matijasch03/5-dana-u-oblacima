from enum import Enum

class Meal(Enum):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3

class ReservationStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELLED = 3