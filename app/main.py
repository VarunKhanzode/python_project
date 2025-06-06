import logging
from fastapi import FastAPI
from app.database.database import Base, engine

app = FastAPI(title="Fitness Studio Booking API", version="1.0")

formatter = "%(process)d - %(asctime)s - %(name)s - FWVOpen - %(pathname)s - " \
                "%(module)s - %(funcName)s - %(lineno)d- %(levelname)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("/fitness_booking_log.txt")
file_handler.setFormatter(logging.Formatter(formatter))
logger.addHandler(file_handler)

def create_app():
    Base.metadata.create_all(bind=engine)

    from app.apis.classes.view import router
    app.include_router(router)

    from app.apis.bookings.view import router
    app.include_router(router)

    return app

