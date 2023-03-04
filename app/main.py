from fastapi import FastAPI
from .routers import breakfast, dinner, lunch

app = FastAPI()

app.include_router(breakfast.router)
app.include_router(dinner.router)
app.include_router(lunch.router)
