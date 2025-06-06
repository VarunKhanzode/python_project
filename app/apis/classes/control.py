from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from fastapi import HTTPException
from app.main import logger

def get_all_classes(db):
    try:
        classes = db.query(models.FitnessClass).all()
        if not classes:
            raise HTTPException(status_code=404, detail="No classes available")
        return classes
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
    
def add_classes(db, payload):
    try:
        new_classes = [
            models.FitnessClass(
                name=cls.name,
                instructor=cls.instructor,
                datetime=cls.datetime,
                available_slots=cls.available_slots
            )
            for cls in payload
        ]
        db.add_all(new_classes)
        db.commit()
        return {"message": f"{len(new_classes)} classes added successfully."}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")