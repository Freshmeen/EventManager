from fastapi import APIRouter
from .endpoints import users
from .endpoints import events

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(users.router)
api_v1_router.include_router(events.router)