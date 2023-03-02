import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()

breakfasts = []


class breakfast(BaseModel):
    name: str
    description: str
    price: float


@router.get("/breakfasts", response_model=List[breakfast])
async def get_breakfasts():
    return breakfasts


@router.post("/breakfasts")
async def create_breakfast(breakfast: breakfast):
    breakfasts.append(breakfast)
    return "success"
