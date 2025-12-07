from typing import Any

from sqlalchemy.types import TypeDecorator, Integer
from pydantic_core import core_schema
from backend.app.database.models.data.user_permission import UserPermission


class UserPermissionType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if isinstance(value, set) or isinstance(value, list):
            return sum(role.value for role in value)
        return value

    def process_result_value(self, value, dialect):
        if isinstance(value, int):
            roles = []
            for role in UserPermission:
                if value & role.value:
                    roles.append(role)
            return roles
        return value