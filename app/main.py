import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as booking_router
from app.users.router import router as users_router
from app.pages.router import router as pages_router
from app.hotels.router import router as hotels_route
from app.rooms.router import router as rooms_router
from app.images.router import router as image_router

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), "static")


app.include_router(users_router)
app.include_router(hotels_route)
app.include_router(rooms_router)
app.include_router(booking_router)
app.include_router(pages_router)
app.include_router(image_router)

