from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 异步引擎
async_engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
)

# 异步会话构造器
AsyncSessionFactory = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db_and_tables():
    """创建数据库表"""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """获取异步数据库会话的依赖函数"""
    async with AsyncSessionFactory() as session:
        yield session


# 创建异步会话依赖类型别名
AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)] 