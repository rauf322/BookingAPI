from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declared_attr
from app.config import setting


engine = create_async_engine(url = setting.async_DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession,expire_on_commit=False)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()