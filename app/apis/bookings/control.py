from app.main import logger
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from fastapi import HTTPException

def create_booking(db, booking):
    try:
        fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()
        if not fitness_class:
            raise HTTPException(status_code=404, detail="Class not found")
        if not fitness_class.available_slots > 0:
            raise HTTPException(status_code=404, detail=f"Slots unavailable in {fitness_class.name} class")

        fitness_class.available_slots -= 1
        new_booking = models.Booking(**booking.dict())
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)
        return {"message": "Booking confirmed"}
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")

def get_bookings_by_email(db, email):
    try:
        bookings = db.query(models.Booking).filter(models.Booking.client_email == email).all()
        if not bookings:
            raise HTTPException(status_code=404, detail="No bookings done yet")
        return bookings
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
