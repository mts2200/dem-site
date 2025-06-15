from app.core.config.db import Base

import datetime
from typing import List
from sqlalchemy import ForeignKey, Integer, Boolean, DateTime, Float, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class StudentsModel(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(256), nullable=False)
    last_name: Mapped[str] = mapped_column(String(256), nullable=False)
    second_name: Mapped[str] = mapped_column(String(256), nullable=False)
    department: Mapped[str] = mapped_column(String(256), nullable=False)
    change_status_dt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    def to_dict(self) -> dict:
        """Конвертирует модель SQLAlchemy в словарь Python."""
        result = {}
        for column in self.__table__.columns:
            result[column.name] = getattr(self, column.name)
        return result