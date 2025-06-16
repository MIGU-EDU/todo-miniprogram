from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import User


class TodoBase(SQLModel):
    """待办事项基础模型"""
    title: str = Field(max_length=200, description="待办事项标题")
    description: Optional[str] = Field(default=None, description="待办事项描述")
    completed: bool = Field(default=False, description="是否已完成")


class Todo(TodoBase, table=True):
    """待办事项数据库表模型"""
    __tablename__ = "todos"
    
    id: Optional[int] = Field(default=None, primary_key=True, description="待办事项ID")
    user_id: int = Field(foreign_key="users.id", description="用户ID")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    
    # 关联用户
    user: Optional["User"] = Relationship(back_populates="todos")


class TodoCreate(TodoBase):
    """创建待办事项的数据模型"""
    pass


class TodoUpdate(SQLModel):
    """更新待办事项的数据模型"""
    title: Optional[str] = Field(default=None, max_length=200, description="待办事项标题")
    description: Optional[str] = Field(default=None, description="待办事项描述")
    completed: Optional[bool] = Field(default=None, description="是否已完成")


class TodoPublic(TodoBase):
    """公开返回的待办事项数据模型"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None 