import datetime
from enum import Enum
from pydantic import BaseModel

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
    createdAt: datetime.datetime
    bookingReference: str

class BookingCreate(BookingBase):
    pass

class BookingInDBBase(BookingBase):
    id : int
    customerId: int
    outboundFlightId : int
    class Config:
        orm_mode = True

class Booking(BookingInDBBase):
    pass

class BookingInDB(BookingInDBBase):
    pass
