from datetime import datetime, timedelta
from typing import Union
import jwt
from jose.exceptions import JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """
    Creates a JWT token with the given data and training time.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
        Checks whether the entered password matches the hashed password.

        :param plain_password: Entered password
        :param hashed_password: Hashed password
        :return: True if the passwords are the same, otherwise False

    """
    return bcrypt_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
        Hashes the password using bcrypt.

        :param password: Password
        :return: Hashed password
    """
    return bcrypt_context.hash(password)

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return payload
    except JWTError:
        raise Exception("Invalid token or token expired")