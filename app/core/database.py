from typing import Annotated, AsyncGenerator
import asyncio
import logging

from fastapi import Depends
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from app.core.config import settings

logger = logging.getLogger(__name__)

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
    """创建数据库表，添加重试逻辑等待数据库就绪"""
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            logger.info(f"尝试连接数据库 (尝试 {attempt + 1}/{max_retries})...")
            async with async_engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.create_all)
            logger.info("数据库连接成功，表创建完成")
            return
        except (OperationalError, ConnectionRefusedError) as e:
            if attempt < max_retries - 1:
                logger.warning(f"数据库连接失败，{retry_delay}秒后重试... 错误: {e}")
                await asyncio.sleep(retry_delay)
            else:
                logger.error(f"数据库连接失败，已达到最大重试次数。错误: {e}")
                raise


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """获取异步数据库会话的依赖函数"""
    async with AsyncSessionFactory() as session:
        yield session


# 创建异步会话依赖类型别名
AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)] 