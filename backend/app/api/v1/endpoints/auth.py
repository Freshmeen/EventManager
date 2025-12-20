from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.v1.deps.auth import get_current_user
from backend.app.api.v1.models.auth import LoginRequest, TokenResponse
from backend.app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)
from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository
from backend.app.services.user_service import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me")
async def me(user=Depends(get_current_user)):
    return user

@router.post("/login", response_model=TokenResponse)
async def login(
    data: LoginRequest,
    response: Response,
    session: AsyncSession = Depends(get_db),
):
    repo = UserRepository(session)
    user = await repo.get_by_email(str(data.email))

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    access = create_access_token(user.email)
    refresh = create_refresh_token(user.email)

    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        secure=True,
        samesite="strict",
        path="/api/v1/auth",
    )

    return TokenResponse(access_token=access)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(
    request: Request,
):
    token = request.cookies.get("refresh_token")
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    decoded = decode_refresh_token(token)
    if decoded is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    email, _ = decoded
    access = create_access_token(email)

    return TokenResponse(access_token=access)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response):
    response.delete_cookie("refresh_token", path="/api/v1/auth")
    return None
