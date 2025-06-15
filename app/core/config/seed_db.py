from sqlalchemy import text
from app.core.config import settings
from app.core.config.db import async_session_maker
from app.core.config.settings import DB_NAME

async def seed_database():
    await _create_db()

async def _create_db():
    async with async_session_maker() as session:
        if settings.DB_TYPE == "postgres":
            # Проверка существования БД в PostgreSQL
            result = await session.execute(
                text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
                {"dbname": settings.DB_NAME}
            )
            db_exists = result.scalar() == 1
            
            if not db_exists:
                # Создание БД с параметрами для PostgreSQL
                await session.execute(
                    text("CREATE DATABASE :dbname ENCODING 'UTF8' LC_COLLATE 'en_US.utf8' LC_CTYPE 'en_US.utf8'"),
                    {"dbname": settings.DB_NAME}
                )
                await session.commit()
                
        elif settings.DB_TYPE == "maria":
            # Проверка существования БД в MariaDB/MySQL
            try:
                await session.execute(
                    text(f"USE `{settings.DB_NAME}`")
                )
                db_exists = True
            except Exception:
                db_exists = False
                await session.rollback()
            
            if not db_exists:
                # Создание БД с параметрами для MariaDB
                await session.execute(
                    text(f"CREATE DATABASE `{settings.DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
                )
                await session.commit()
        else:
            raise ValueError(f"Unsupported DB type: {settings.DB_TYPE}")