from datetime import date

from fastapi import APIRouter,Depends
from app.bookings.model import Bookings
from app.bookings.schemas import SBooking
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.exceptions import RoomCantBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.get("")
async def get_bookings(user:Users = Depends(get_current_user)):
    return await  BaseDAO.find_all(Bookings, user_id = user.id)

@router.get("/rooms_amount")
async def booking_add(room_id:int, date_from: date, date_to:date, user:Users = Depends(get_current_user)):
    booking = await BaseDAO.add_booking(user.id, room_id,date_from, date_to)
    if not booking:
        raise RoomCantBeBookedException





