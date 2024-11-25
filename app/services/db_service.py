from typing import Union
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserInDB


def create_user(db: Session, user_create: UserCreate) -> User:
    user = User(username=user_create.username,
                email=user_create.email,
                hashed_password=get_password_hash(user_create.password),
                role=user_create.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, username: str) -> Union[User, None]:
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str) -> Union[UserInDB, None]:
    user = get_user(db, username)
    if user and verify_password(password, user.hashed_password):
        return UserInDB(**user.__dict__)
    return None