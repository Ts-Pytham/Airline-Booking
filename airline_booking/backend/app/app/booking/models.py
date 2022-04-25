from tkinter import CASCADE
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flight.models import Flight
from user.models import User
from database.session import Base
from schema import BookingStatus

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(50), default=BookingStatus.UNCONFIRMED)
    outboundFlightId = Column(Integer, ForeignKey(Flight.id, ondelete="CASCADE"), ) #Unchecked
    flight = relationship(Flight, back_populates="booking")
    paymentToken = Column(String(50))
    checkedIn = Column(Boolean)
    customerId = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), ) #Unchecked
    customer = relationship(User, back_populates="bookings")
    createdAt = Column(DateTime)
    bookingReference = Column(String(50))
    





