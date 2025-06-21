from fastapi import APIRouter

from app.api.routes import todos, auth

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(todos.router)
