from sqlalchemy import Column, Integer, String
from .database import Base


class Breakfasts(Base):
    __tablename__ = "breakfasts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
