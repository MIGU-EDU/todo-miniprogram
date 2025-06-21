from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.config import settings
from app.core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时创建数据库表
    await create_db_and_tables()
    yield
    # 应用关闭时的清理工作（如果需要）


def create_app() -> FastAPI:
    """创建 FastAPI 应用实例"""
    app = FastAPI(
        title=settings.app_name,
        description="一个使用 FastAPI + SQLModel + PostgreSQL 构建的待办事项 API",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
    )

    # 配置 CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # 允许前端访问
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 包含 API 路由
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/")
    async def root():
        """根路径"""
        return {
            "message": f"欢迎使用 {settings.app_name}",
            "docs": "/docs",
            "version": "1.0.0"
        }
        
    @app.get("/health")
    async def health_check():
        """健康检查端点"""
        return {"status": "healthy"}

    return app


# 创建应用实例
app = create_app() 