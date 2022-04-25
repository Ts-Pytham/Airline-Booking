from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from database.session import Base
from enum import Enum

class BookingStatus(Enum):
    UNCONFIRMED = 0
    CONFIRMED = 1
    CANCELLED = 2

class Booking(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = BookingStatus.CANCELLED #Change
    outboundFlight = relationship("Flight", uselist=False, foreign_keys="Booking.outboundFlightId") #Unchecked
    paymentToken = Column(String(50))
    checkedIn = Column(Boolean)
    customer = relationship("User", uselist=False, foreign_keys="Booking.customerId") #Unchecked
    createdAt = Column(DateTime)
    bookingReference = Column(String(50))





