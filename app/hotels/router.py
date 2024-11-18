from typing import Optional

from fastapi import APIRouter, Depends
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.hotels.schemas import SHotels
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix = "/hotels",
    tags = ["Information of hotels"]
)

@router.get("/all_hotels")
async def get_hotels(hotel_id:Optional[int] = None, user:Users = Depends(get_current_user))->list[SHotels]:
    return await BaseDAO.find_all_hotels(Hotels, id= hotel_id)