from fastapi import APIRouter

from .endpoints import auth, events, users, event_members

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(auth.router)
api_v1_router.include_router(users.router)
api_v1_router.include_router(events.router)
api_v1_router.include_router(event_members.router)
