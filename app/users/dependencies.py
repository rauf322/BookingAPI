from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import setting
from app.dao.base import BaseDAO
from app.exceptions import TokenExpiredException, TokenAbsentException, IncorrectTokenFormatException,UserNotFoundException
from app.users.models import Users


def get_token(request:Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, setting.JWT_KEY, setting.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotFoundException
    user = await BaseDAO.find_by_id(Users,int(user_id))
    if not user:
        raise UserNotFoundException
    return user