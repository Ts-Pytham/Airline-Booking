from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from app.core import security
from app.database import db
from . import schema
from . import services


api_router = APIRouter(tags = ["booking"])


@api_router.get('/booking/{id}', response_model = schema.Booking)
async def get_booking_by_id(id: int, db_session : Session = Depends(db.get_db)):
    booking = await services.get_booking_by_id(id, db_session)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking

@api_router.get('/booking/', response_model = List[schema.Booking])
async def get_all_bookings(db_session : Session = Depends(db.get_db), customerName : str = None, status : schema.BookingStatus = None):
    bookings = await services.get_all_bookings(db_session=db_session, customerName=customerName, status=status)
    
    if not bookings:
        raise HTTPException(status_code=404, detail="Bookings not found")

    return bookings

@api_router.post('/booking/flight/{idFlight}/user/{idUser}', response_model = schema.BookingCreate)
async def create_booking(idFlight: int, idUser: int, booking_in : schema.BookingCreate, db_session : Session = Depends(db.get_db)):
    booking = await services.create_booking(idFlight=idFlight, idUser=idUser, booking_in=booking_in, db_session=db_session)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking is already exist")
    return booking

@api_router.delete('/booking/{id}', response_model = schema.Booking)
async def delete_booking(id: int, db_session : Session = Depends(db.get_db)):
    booking = await services.delete_booking(id=id, db_session=db_session)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

