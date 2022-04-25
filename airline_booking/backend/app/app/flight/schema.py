from datetime import datetime
from pydantic import BaseModel

from booking.schema import Booking 

class FlightBase(BaseModel):
    departureDate : datetime
    departureAirportCode : str
    departureAirportName : str
    departureCity : str
    departureLocale : str
    arrivalDate : datetime
    arrivalAirportCode : str
    arrivalAirportName : str
    arrivalCity : str
    arrivalLocale : str
    ticketPrice : int
    ticketCurrency : str
    flightNumber : int
    seatCapacity : int

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class FlightInDBBase(FlightBase):
    id : int
    booking : Booking
    class Config:
        orm_mode = True

class Flight(FlightInDBBase):
    pass

class FlightInDB(FlightInDBBase):
    pass
    