from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.session import get_db
from app.schemas.user import UserCreate
from app.services.db_service import create_user

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    New User Registration.
    """
    db_user = await create_user(db, user)
    if db_user:
        return JSONResponse(
            content={"message": "User successfully registered", "user_id": db_user.id},
            status_code=201
        )
    else:
        raise HTTPException(status_code=400, detail="User registration failed")