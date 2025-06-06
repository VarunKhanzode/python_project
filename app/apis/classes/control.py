from app.models import models
from app.schemas import schemas
from fastapi import HTTPException
from pytz import timezone as pytz_timezone, utc, UnknownTimeZoneError
from app.main import logger

def get_all_classes(db, tz: str):
    try:
        try:
            user_tz = pytz_timezone(tz)
        except UnknownTimeZoneError:
            raise HTTPException(status_code=400, detail="Invalid timezone provided.")
        
        classes = db.query(models.FitnessClass).all()
        if not classes:
            raise HTTPException(status_code=404, detail="No classes available")
        result = []
        for cls in classes:
            local_time = cls.datetime.astimezone(user_tz)
            result.append({
                "id": cls.id,
                "name": cls.name,
                "instructor": cls.instructor,
                "datetime": local_time,
                "available_slots": cls.available_slots
            })

        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
    
def add_classes(db, payload):
    try:
        new_classes = []
        for cls in payload:
            input_tz = pytz_timezone(cls.timezone)
            localized_time = input_tz.localize(cls.datetime)
            utc_time = localized_time.astimezone(utc)

            existing = db.query(models.FitnessClass).filter(
            models.FitnessClass.name == cls.name,
            models.FitnessClass.datetime == utc_time
            ).first()

            if existing:
                raise HTTPException(
                    status_code=400,
                    detail=f"{cls.name} class already exists at that time."
                )

            new_class = models.FitnessClass(
                            name=cls.name,
                            instructor=cls.instructor,
                            datetime=utc_time,
                            available_slots=cls.available_slots
                        )
            new_classes.append(new_class)
        db.add_all(new_classes)
        db.commit()
        return {"message": f"{len(new_classes)} classes added successfully."}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")