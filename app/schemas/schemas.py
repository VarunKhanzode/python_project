from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class CreateClass(BaseModel):
    name: str
    instructor: str
    datetime: datetime
    available_slots: int

class ClassResponse(CreateClass):
    id: int
    class Config:
        orm_mode = True

class CreateBooking(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(CreateBooking):
    id: int
    class Config:
        orm_mode = True
