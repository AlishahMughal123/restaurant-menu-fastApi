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


class dinner(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float


dinners = []


@router.get("/dinners")
async def get_dinners(db: Session = Depends(get_db)):
    return db.query(models.Dinners).all()


@router.post("/dinners")
async def create_dinner(dinner: dinner, db: Session = Depends(get_db)):
    dinner_model = models.Dinners()
    dinner_model.name = dinner.name
    dinner_model.description = dinner.description
    dinner_model.price = dinner.price
    db.add(dinner_model)
    db.commit()
    return "success"


@router.put("/dinner/{dinner_id}")
def update_dinner(dinner_id: int, dinner: dinner, db: Session = Depends(get_db)):
    dinner_model = db.query(models.Dinners).filter(
        models.Dinners.id == dinner_id).first()

    if dinner_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {dinner_id} : Does not exist"
        )
    dinner_model.name = dinner.name
    dinner_model.description = dinner.description
    dinner_model.price = dinner.price
    db.add(dinner_model)
    db.commit()

    return dinner


@router.delete("/dinner/{dinner_id}")
def delete_dinner(dinner_id: int, db: Session = Depends(get_db)):
    dinner_model = db.query(models.Dinners).filter(
        models.Dinners.id == dinner_id).first()

    if dinner_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {dinner_id} : Does not exist"
        )

    db.query(models.Dinners).filter(
        models.Dinners.id == dinner_id).delete()

    db.commit()
    return "null"
