from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import setting
from app.dao.base import BaseDAO
from app.users.models import Users

#this function was implemented to hashing user password for not storing the actual password of user in our DB
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password)->bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data:dict)->str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(
        to_encode, setting.JWT_KEY, setting.ALGORITHM
    )
    return encode_jwt


async def authenticate_user(email:EmailStr,password:str):
    user = await BaseDAO.find_one_or_none(Users, email = email)
    if not user and not verify_password(password,user.password):
        return None
    return user
