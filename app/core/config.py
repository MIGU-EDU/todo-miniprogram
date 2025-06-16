from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field(default="SaveFlow Todo API", alias="APP_NAME")
    debug: bool = Field(default=True, alias="DEBUG")  # 默认开启调试模式
    secret_key: str = Field(default="your-secret-key-here", alias="SECRET_KEY")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    
    # 数据库配置 - 使用 PostgreSQL
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/saveflow",
        alias="DATABASE_URL"
    )
    
    # PostgreSQL 配置
    postgres_host: str = Field(default="localhost", alias="POSTGRES_SERVER")
    postgres_port: int = Field(default=5432, alias="POSTGRES_PORT")
    postgres_user: str = Field(default="postgres", alias="POSTGRES_USER")
    postgres_password: str = Field(default="postgres", alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(default="saveflow", alias="POSTGRES_DB")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# 创建全局设置实例
settings = Settings()
