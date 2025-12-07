from datetime import datetime
from enum import IntEnum
from uuid import UUID
from pydantic import BaseModel, EmailStr, constr, conset, field_serializer

from backend.app.api.v1.exceptions.users import TooShortPasswordException
from backend.app.database.models.data import UserPermission


class UserWithPermissionMixin:
    permission: set[UserPermission] = set()

    @field_serializer("permission")
    @classmethod
    def serialize_permissions(cls, value):
        return map(lambda permission: permission.name, value)


class UserBase(UserWithPermissionMixin, BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str
    email: EmailStr
    avatar_path: str | None = None

    model_config = {
        "from_attributes": True,
    }


class UserCreate(UserBase):
    password: str = constr(min_length=8)

class UserUpdate(BaseModel):
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    avatar_path: str | None = None

class UserResponse(UserBase):
    user_id: UUID

class UserCreateResponse(BaseModel):
    user_id: UUID

    model_config = {
        "from_attributes": True,
    }