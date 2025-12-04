from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, field_validator

from backend.app.api.v1.exceptions.TooShortPasswordException import TooShortPasswordException


class UserBase(BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str
    email: EmailStr
    avatar_path: str | None = None
    permission: str = "user"

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def password_must_be_strong(cls, v: str) -> str:
        if len(v) < 8:
            raise TooShortPasswordException()
        return v

class UserUpdate(BaseModel):
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    avatar_path: str | None = None
    permission: str | None = None

class UserRead(UserBase):
    user_id: UUID
    points: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

class UserCreateResponse(BaseModel):
    user_id: UUID