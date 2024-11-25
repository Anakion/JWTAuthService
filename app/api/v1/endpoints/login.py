from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.core.config import settings
from app.core.security import create_access_token
from app.db.session import get_db
from app.schemas.user import UserCreate, Token
from app.services.db_service import create_user, authenticate_user

router = APIRouter()

@router.post("/token", response_model=Token)
def login(form_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """
       User authentication and token creation.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"}, status_code=200)

