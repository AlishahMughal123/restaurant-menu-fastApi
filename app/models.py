from sqlalchemy import Column, Integer, String
from .database import Base


class Breakfasts(Base):
    __tablename__ = "breakfasts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)


class Dinners(Base):
    __tablename__ = "dinners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)


class Lunchs(Base):
    __tablename__ = "lunchs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
