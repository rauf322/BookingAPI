from typing import Optional

from fastapi import APIRouter, Depends

from app.dao.base import BaseDAO
from app.rooms.models import Rooms
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

@router.get("/view_rooms")
async def get_rooms(room_id:Optional[int] = None, user:Users = Depends(get_current_user)):
    return await BaseDAO.find_all_hotels(Rooms, id = room_id )

