from uuid import UUID
from backend.app.api.v1.exceptions.base import BadRequestException


class EventMemberAlreadyExistsException(BadRequestException):
    def __init__(self, *, user_id: UUID, event_id: UUID):
        super().__init__(
            f"User {user_id} is already a member of Event {event_id}",
            "EVENT_MEMBER_ALREADY_EXISTS"
        )