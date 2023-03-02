from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from api import breakfast

app = FastAPI()

app.include_router(breakfast.router)
# app.include_router(dinner.router)
# app.include_router(lunch.router)
