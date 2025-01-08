from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    name: str
    email: EmailStr
    username: str
    dob: date

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

