from sqlalchemy.orm import mapped_column, Mapped
from app.db.base import Base
from sqlalchemy import Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, nullable=False, default='user')
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
