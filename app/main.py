import sys
import os
from fastapi import FastAPI


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.bookings.router import router as booking_router
from app.users.router import router as users_router

app = FastAPI()
app.include_router(users_router)
app.include_router(booking_router)



