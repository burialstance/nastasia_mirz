import re
from contextlib import asynccontextmanager

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from advanced_alchemy.base import CommonTableAttributes, BigIntPrimaryKey


class Model(CommonTableAttributes, BigIntPrimaryKey, DeclarativeBase):
    ...


class Database:
    def __init__(self, db_url: str, echo: bool = False) -> None:
        self._engine: AsyncEngine = create_async_engine(
            url=db_url,
            echo=echo,
        )
        self._session_factory = async_sessionmaker(
            self._engine,
            autoflush=False,
            expire_on_commit=False,
        )

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    async def create_database(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)

    @asynccontextmanager
    async def session(self) -> async_sessionmaker[AsyncSession]:
        session: AsyncSession = self._session_factory()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
