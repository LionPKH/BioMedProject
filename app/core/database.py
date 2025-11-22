from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.settings import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    settings.DB_URL,
    echo=False,
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        # print("NEW SESSION:", id(session))     # проверка корректного DI
        yield session

async def init_db() -> None:
    import app.models

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)