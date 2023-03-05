from fastapi import FastAPI
from .routers import breakfast, dinner, lunch
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(breakfast.router)
app.include_router(dinner.router)
app.include_router(lunch.router)
