from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.v1.exceptions.base.forbidden_exception import ForbiddenException
from backend.app.api.v1.models.user import UserResponse
from backend.app.core.security import decode_access_token
from backend.app.database.models.data import UserPermission
from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)


async def get_current_user(
    request: Request,
    token: str | None = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_db),
):
    if token is None:
        token = request.cookies.get("access_token")

    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    email = decode_access_token(token)
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    repo = UserRepository(session)
    user = await repo.get_by_email(email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return UserResponse.model_validate(user)

def auth_required(roles: list[UserPermission] | None = None):
    async def dependency(user: UserResponse = Depends(get_current_user)) -> UserResponse:
        if roles:
            user_roles = set(user.permission)
            required_roles = set(roles)
            if not user_roles & required_roles:
                raise ForbiddenException()
        return user

    return dependency
