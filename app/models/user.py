from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .todo import Todo


class UserBase(SQLModel):
    """用户基础模型"""
    openid: str = Field(unique=True, index=True, description="微信小程序用户openid")
    nickname: Optional[str] = Field(default=None, max_length=100, description="用户昵称")
    avatar_url: Optional[str] = Field(default=None, description="用户头像URL")


class User(UserBase, table=True):
    """用户数据库表模型"""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True, description="用户ID")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    
    # 关联待办事项
    todos: list["Todo"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    """创建用户的数据模型"""
    pass


class UserUpdate(SQLModel):
    """更新用户的数据模型"""
    nickname: Optional[str] = Field(default=None, max_length=100, description="用户昵称")
    avatar_url: Optional[str] = Field(default=None, description="用户头像URL")


class UserPublic(UserBase):
    """公开返回的用户数据模型"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None 