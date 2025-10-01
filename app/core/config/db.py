from typing import AsyncGenerator
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.config import settings

class Base(DeclarativeBase):
    pass

def get_db_connection(
    user=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
) -> URL:
    if settings.DB_TYPE == "postgres":
        return URL.create(
            drivername="postgresql+asyncpg",
            username=user,
            password=password,
            host=host,
            port=port,
            database=database,
            query={"async_fallback": "true"}
        )
    elif settings.DB_TYPE == "maria":
        return URL.create(
            drivername="mysql+asyncmy",
            username=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    else:
        raise ValueError("Unsupported DB_TYPE in settings")

engine = None
async_session_maker = None

try:
    engine = create_async_engine(
        get_db_connection(),
        pool_pre_ping=True,
    )
    async_session_maker = async_sessionmaker(
        engine,
        expire_on_commit=False
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize database: {str(e)}")

async def get_sessions_async() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session