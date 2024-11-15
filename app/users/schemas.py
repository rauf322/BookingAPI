from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    email:EmailStr
    password:str

class SUserAuth(BaseModel):
    id:int
    email:EmailStr
    password:str