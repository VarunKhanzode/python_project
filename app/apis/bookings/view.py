from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.database.database import get_db
from .control import create_booking, get_bookings_by_email

router = APIRouter(tags=['Bookings'])

@router.post("/book", status_code=201)
def book_class(booking: schemas.CreateBooking, db: Session = Depends(get_db)):
    return create_booking(db, booking)

@router.get("/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(email: str, db: Session = Depends(get_db)):
    return get_bookings_by_email(db, email)
