from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from app.core.auth import CurrentUser
from app.core.database import AsyncSessionDep
from app.models.todo import Todo, TodoCreate, TodoUpdate, TodoPublic
from app.models.user import User

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoPublic)
async def create_todo(
    todo: TodoCreate, 
    session: AsyncSessionDep,
    current_user: CurrentUser
) -> TodoPublic:
    """创建新的待办事项"""
    # 将TodoCreate数据转换为字典，并添加user_id
    todo_data = todo.model_dump()
    todo_data["user_id"] = current_user.id
    
    # 创建Todo对象
    db_todo = Todo.model_validate(todo_data)
    session.add(db_todo)
    await session.commit()
    await session.refresh(db_todo)
    return db_todo


@router.get("/", response_model=List[TodoPublic])
async def read_todos(
    session: AsyncSessionDep,
    current_user: CurrentUser,
    offset: int = Query(default=0, ge=0, description="跳过的记录数"),
    limit: int = Query(default=100, le=100, description="返回的记录数"),
    completed: bool | None = Query(default=None, description="筛选已完成/未完成的待办事项")
) -> List[TodoPublic]:
    """获取待办事项列表"""
    statement = select(Todo).where(Todo.user_id == current_user.id)
    
    # 如果指定了完成状态，则添加筛选条件
    if completed is not None:
        statement = statement.where(Todo.completed == completed)
    
    statement = statement.offset(offset).limit(limit)
    result = await session.exec(statement)
    todos = result.all()
    return todos


@router.get("/{todo_id}", response_model=TodoPublic)
async def read_todo(
    todo_id: int, 
    session: AsyncSessionDep,
    current_user: CurrentUser
) -> TodoPublic:
    """获取单个待办事项"""
    todo = await session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="待办事项未找到")
    
    # 检查是否属于当前用户
    if todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权访问此待办事项")
    
    return todo


@router.put("/{todo_id}", response_model=TodoPublic)
async def update_todo(
    todo_id: int, 
    todo_update: TodoUpdate, 
    session: AsyncSessionDep,
    current_user: CurrentUser
) -> TodoPublic:
    """更新待办事项"""
    todo = await session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="待办事项未找到")
    
    # 检查是否属于当前用户
    if todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权修改此待办事项")
    
    # 更新字段
    todo_data = todo_update.model_dump(exclude_unset=True)
    for field, value in todo_data.items():
        setattr(todo, field, value)
    
    # 设置更新时间
    todo.updated_at = datetime.utcnow()
    
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int, 
    session: AsyncSessionDep,
    current_user: CurrentUser
) -> dict:
    """删除待办事项"""
    todo = await session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="待办事项未找到")
    
    # 检查是否属于当前用户
    if todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="无权删除此待办事项")
    
    await session.delete(todo)
    await session.commit()
    return {"message": "待办事项已删除", "id": todo_id} 