from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List

class CreateClass(BaseModel):
    name: str = Field(title="Class Name", description="Provide name of the class", max_length=15, min_length=2)
    instructor: str = Field(title="Instructor Name", description="Provide name of the instructor", max_length=20, min_length=3)
    datetime: datetime
    available_slots: int = Field(default=1,title="No. of available slots", description="Provide number of available slots for this class")
    timezone: str = Field(default="Asia/Kolkata",title="Time Zone", description="Provide your timezone")

class ClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    datetime: datetime
    available_slots: int
    class Config:
        orm_mode = True

class CreateBooking(BaseModel):
    class_id: int = Field(title="Class ID", description="Provide class ID for booking")
    client_name: str = Field(title="Client Name", description="Provide client name", max_length=15, min_length=2)
    client_email: EmailStr = Field(title="Client Email ID", description="Provide client mail ID")

class BookingResponse(CreateBooking):
    id: int
    class Config:
        orm_mode = True
