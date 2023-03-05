from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel, Field
from app import models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class breakfast(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float


breakfasts = []


@router.get("/breakfasts")
async def get_breakfasts(db: Session = Depends(get_db)):
    return db.query(models.Breakfasts).all()


@router.post("/breakfasts")
async def create_breakfast(breakfast: breakfast, db: Session = Depends(get_db)):
    breakfast_model = models.Breakfasts()
    breakfast_model.name = breakfast.name
    breakfast_model.description = breakfast.description
    breakfast_model.price = breakfast.price
    db.add(breakfast_model)
    db.commit()
    return "success"


@router.put("/breakfast/{breafast_id}")
def update_breakfast(breakfast_id: int, breakfast: breakfast, db: Session = Depends(get_db)):
    breakfast_model = db.query(models.Breakfasts).filter(
        models.Breakfasts.id == breakfast_id).first()

    if breakfast_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {breakfast_id} : Does not exist"
        )

    breakfast_model.name = breakfast.name
    breakfast_model.description = breakfast.description
    breakfast_model.price = breakfast.price
    db.add(breakfast_model)
    db.commit()

    return breakfast


@router.delete("/breakfast/{breakfast_id}")
def delete_breakfast(breakfast_id: int, db: Session = Depends(get_db)):
    breakfast_model = db.query(models.Breakfasts).filter(
        models.Breakfasts.id == breakfast_id).first()

    if breakfast_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {breakfast_id} : Does not exist"
        )

    db.query(models.Breakfasts).filter(
        models.Breakfasts.id == breakfast_id).delete()

    db.commit()
    return "null"
