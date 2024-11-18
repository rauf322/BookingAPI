from fastapi import APIRouter, Response, Depends
from app.dao.base import BaseDAO
from app.exceptions import UserAlreadyExistException, IncorrectLoginException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegister, SUserAuth

router = APIRouter(
    prefix="/auth",
    tags= ["Authentication User"]
)
#Registering of Users and checking if this user exist or not in DB
@router.post("/register")
async def register_user(user_email, password)->SUserRegister:
    #This sentence checking if the user exists
    existing_user = await BaseDAO.find_one_or_none(Users,email = user_email)
    if existing_user:
        raise UserAlreadyExistException
    #if not we will add him in DB
    hashed_password = get_password_hash(password)
    await BaseDAO.add(Users,email = user_email, hashed_password = hashed_password)
    return {"email":user_email, "password":hashed_password}

@router.post("/login")
async def login_user(response: Response, user_data:SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectLoginException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout_user(response:Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def read_user(user:Users = Depends(get_current_user)):
    return user