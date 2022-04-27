from fastapi import FastAPI
from app.booking import router as booking_router
from app.user import router as user_router
from app.database import models

app = FastAPI(title="Airline Booking", version = "1.0")


@app.get("/")
async def home():
    return {"message": "Welcome to Airline Booking"}

app.include_router(booking_router.api_router)
app.include_router(user_router.api_router)


