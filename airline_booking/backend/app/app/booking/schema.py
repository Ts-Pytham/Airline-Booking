from enum import Enum
from pydantic import BaseModel
from app.flight.schema import Flight
from app.user.schema import User

class BookingStatus(str, Enum):
    UNCONFIRMED = 'UNCONFIRMED'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'

class BookingBase(BaseModel):
    status: BookingStatus
    outboundFlightId: int
    paymentToken: str
    checkedIn: bool
    customerId: int
    createdAt: str
    bookingReference: str

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BookingBase):
    pass

class BookingInDBBase(BookingBase):
    id: int
    flight : Flight
    customer: User
    class Config:
        orm_mode = True

class Booking(BookingInDBBase):
    pass

class BookingInDB(BookingInDBBase):
    pass


