from datetime import datetime
from enum import IntEnum
from uuid import UUID
from pydantic import BaseModel, EmailStr, field_validator, field_serializer, Field

from backend.app.api.v1.exceptions.users import TooShortPasswordException

class UserRole(IntEnum):
    ADMIN = 0b1
    EVENT_PARTICIPANT = 0b10
    EVENT_CREATOR = 0b100

class UserWithPermissionMixin:
    permissions: list[UserRole] = Field(validation_alias="permission")

    @field_validator("permissions", mode="before")
    @classmethod
    def convert_permissions(cls, value):
        if isinstance(value, int):
            roles = []
            for role in UserRole:
                if value & role.value:
                    roles.append(role)
            return roles
        return value

    @field_serializer("permissions")
    @classmethod
    def serialize_permissions(cls, value):
        return map(lambda permission: permission.name, value)


class UserBase(UserWithPermissionMixin, BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str
    email: EmailStr
    avatar_path: str | None = None


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

class UserResponse(UserBase):
    user_id: UUID
    points: int

    model_config = {
        "from_attributes": True,
    }

class UserCreateResponse(BaseModel):
    user_id: UUID

    model_config = {
        "from_attributes": True,
    }