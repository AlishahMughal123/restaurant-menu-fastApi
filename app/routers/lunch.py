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


class lunch(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float


lunchs = []


@router.get("/lunchs")
async def get_lunchs(db: Session = Depends(get_db)):
    return db.query(models.Dinners).all()


@router.post("/lunchs")
async def create_lunch(lunch: lunch, db: Session = Depends(get_db)):
    lunch_model = models.Lunchs()
    lunch_model.name = lunch.name
    lunch_model.description = lunch.description
    lunch_model.price = lunch.price
    db.add(lunch_model)
    db.commit()
    return "success"


@router.put("/lunch/{lunch_id}")
def update_lunch(lunch_id: int, lunch: lunch, db: Session = Depends(get_db)):
    lunch_model = db.query(models.Lunchs).filter(
        models.Lunchs.id == lunch_id).first()

    if lunch_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {lunch_id} : Does not exist"
        )
    lunch_model.name = lunch.name
    lunch_model.description = lunch.description
    lunch_model.price = lunch.price
    db.add(lunch_model)
    db.commit()

    return lunch


@router.delete("/lunch/{lunch_id}")
def delete_lunch(lunch_id: int, db: Session = Depends(get_db)):
    lunch_model = db.query(models.Lunchs).filter(
        models.Lunchs.id == lunch_id).first()

    if lunch_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {lunch_id} : Does not exist"
        )

    db.query(models.Lunchs).filter(
        models.Lunchs.id == lunch_id).delete()

    db.commit()
    return "null"
