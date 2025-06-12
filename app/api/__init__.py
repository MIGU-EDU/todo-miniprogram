from fastapi import APIRouter

from app.api.routes import todos

api_router = APIRouter()

api_router.include_router(todos.router)
