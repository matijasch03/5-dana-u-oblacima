from fastapi import HTTPException, APIRouter, Header

from dtos.canteen_dto import CanteenCreate
from model.models import Canteen
from data_base.shared import students



router = APIRouter(prefix="/canteens", tags=["Canteens"])

canteens = []
canteen_counter = 0


@router.post("", status_code=201, response_model=Canteen)
def create_canteen(canteen: CanteenCreate, student_id: str = Header(...)):
    global canteen_counter

    # generator expression in one line using next()
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if not student.get("isAdmin", False):
        raise HTTPException(status_code=403, detail="User is not admin")

    new_canteen = {
        "id": str(canteen_counter),
        "name": canteen.name,
        "location": canteen.location,
        "capacity": canteen.capacity,
        "workingHours": canteen.workingHours
    }
    canteen_counter += 1

    canteens.append(new_canteen)
    return new_canteen
