from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import schemas
from app.models import models
from typing import List
from .control import get_all_classes, add_classes

router = APIRouter(tags=['Classes'])

@router.post("/classes", description="This API will add multiple classes at once", status_code=201)
def add_multiple_classes(payload: List[schemas.CreateClass], db: Session = Depends(get_db)):
    return add_classes(db, payload)

@router.get("/classes", response_model=list[schemas.ClassResponse], description="This API will provide all available classes")
def read_classes(db: Session = Depends(get_db)):
    return get_all_classes(db)
