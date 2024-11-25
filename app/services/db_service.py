from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserInDB


async def create_user(db: AsyncSession, user_create: UserCreate) -> User:
    user = User(username=user_create.username,
                email=user_create.email,
                hashed_password=get_password_hash(user_create.password),
                role=user_create.role)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, username: str) -> Union[User, None]:
    result = await db.execute(select(User).filter(User.username == username))
    user = result.scalar_one_or_none()
    return user


async def authenticate_user(db: AsyncSession, username: str, password: str) -> Union[UserInDB, None]:
    user = await get_user(db, username)
    if user and verify_password(password, user.hashed_password):
        return UserInDB(**user.__dict__)
    return None
