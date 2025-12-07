from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository
from backend.app.services.user_service import UserService
from backend.app.api.v1.models.user import UserCreate, UserResponse, UserUpdate, UserCreateResponse

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(session: AsyncSession = Depends(get_db)) -> UserService:
    repo = UserRepository(session)
    return UserService(repo)


@router.post(
    "/",
    response_model=UserCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user"
)
async def create_user(
        user_in: UserCreate,
        service: UserService = Depends(get_user_service)
):
    user_id = await service.create(user_in)
    return UserCreateResponse(user_id=user_id)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID"
)
async def get_user(
        user_id: UUID,
        service: UserService = Depends(get_user_service)
):
    return await service.get_by_id(user_id)


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="List all users"
)
async def list_users(service: UserService = Depends(get_user_service)):
    return await service.list_all()


@router.patch(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update user partially"
)
async def update_user(
        user_id: UUID,
        user_update: UserUpdate,
        service: UserService = Depends(get_user_service)
):
    await service.update(user_id, user_update)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user"
)
async def delete_user(
        user_id: UUID,
        service: UserService = Depends(get_user_service)
):
    await service.delete(user_id)
