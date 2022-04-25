from pydantic import BaseModel, constr

from booking.models import Booking

class UserBase(BaseModel):
    fullname : constr(min_length=2, max_length=50)
    username : str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str
    pass

class UserInDBBase(UserBase):
    id: int
    booking : Booking
    password: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    booking : Booking
    class Config:
        orm_mode = True
