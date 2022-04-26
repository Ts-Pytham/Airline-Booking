from fastapi import FastAPI
from core.config import settings
from database import models

app = FastAPI(title="Airline Booking", version = "1.0")


@app.get("/")
async def home():
    return {"message": "Welcome to Airline Booking"}

