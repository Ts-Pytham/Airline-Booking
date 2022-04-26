from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.booking.models import Booking
from . import schema

async def get_booking_by_id(booking_id: int, db_session : Session) -> Booking:
    booking = db_session.query(Booking).filter(Booking.id == booking_id).first()
    return booking

async def get_all_bookings(db_session : Session, customerName : str | None = None, status : schema.BookingStatus | None = None) -> List[Booking]:
    if not (str and status):
        bookings = db_session.query(Booking).all()
    if str and not status:
        bookings = db_session.query(Booking).filter(Booking.customerName == customerName).all()
    if not str and status:
        bookings = db_session.query(Booking).filter(Booking.status == status).all()
    else:
        bookings = db_session.query(Booking).filter(Booking.customerName == customerName, Booking.status == status).all()

    return bookings

async def create_booking(booking_in: schema.BookingCreate, db_session : Session) -> Booking:
    booking = Booking(**booking_in.dict())
    db_session.add(booking)
    db_session.commit()
    db_session.refresh(booking)
    return booking





