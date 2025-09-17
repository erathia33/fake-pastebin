from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True) 
    author: Mapped[str] = mapped_column(String(25))
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now(), onupdate=func.now())
