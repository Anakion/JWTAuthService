from sqlalchemy.ext.asyncio import (create_async_engine,
                                    async_sessionmaker, AsyncSession)

from app.core.config import settings

async_engine = create_async_engine(settings.URL_DB, echo=False)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()