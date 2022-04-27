from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.booking.models import Booking
from app.flight import models as flight_models
from app.user import models as user_models
from . import schema

async def get_booking_by_id(booking_id: int, db_session : Session) -> Booking:
    booking = db_session.query(Booking).get(booking_id)
    return booking

async def get_booking_by_idFlight(idFlight : int, db_session : Session) -> List[Booking]:
    bookings = db_session.query(Booking).filter(Booking.idFlight == idFlight).all()
    return bookings

async def get_all_bookings(db_session : Session, customerName : str, status : schema.BookingStatus) -> List[Booking]:

    if not (customerName and status):
        bookings = db_session.query(Booking).all()

    elif customerName and not status:
        customer = db_session.query(user_models.User).filter(user_models.User.fullname == customerName).first()
        bookings = db_session.query(Booking).filter(Booking.customer == customer).all()

    elif not customerName and status:
        bookings = db_session.query(Booking).filter(Booking.status == status).all()
    else:
        customer = db_session.query(user_models.User).filter(user_models.fullname == customerName).first()
        bookings = db_session.query(Booking).filter(Booking.customer == customer).all()

    return bookings

async def create_booking(idFlight : int, idUser: int, booking_in: schema.BookingCreate, db_session : Session) -> Booking:
    if not db_session.query(flight_models.Flight.id).filter(flight_models.Flight.id == idFlight).exists():
        raise HTTPException(status_code=404, detail="Flight not found")
    if not db_session.query(user_models.User.id).filter(user_models.User.id == idUser).exists():
        raise HTTPException(status_code=404, detail="User not found")

    booking = Booking(idFlight=idFlight, idUser=idUser, **booking_in.dict())
    db_session.add(booking)
    db_session.commit()
    db_session.refresh(booking)
    return booking

async def delete_booking(booking_id: int, db_session : Session) -> Booking:
    booking = db_session.query(Booking).filter(Booking.id == booking_id).first()
    db_session.delete(booking)
    db_session.commit()
    return booking






