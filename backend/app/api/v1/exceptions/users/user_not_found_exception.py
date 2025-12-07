from uuid import UUID

from backend.app.api.v1.exceptions.base import NotFoundException


class UserNotFoundException(NotFoundException):
    def __init__(self, *, user_id: UUID = None, email: str = None):
        user_identifier = user_id or email
        super().__init__(f"User {user_identifier} is not found", "USER_NOT_FOUND")
