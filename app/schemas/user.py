from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = 'user'

class UserInDB(BaseModel):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str