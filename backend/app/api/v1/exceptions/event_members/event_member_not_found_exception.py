from uuid import UUID
from backend.app.api.v1.exceptions.base import NotFoundException


class EventMemberNotFoundException(NotFoundException):
    def __init__(self, *, user_id: UUID, event_id: UUID):
        super().__init__(
            f"Member relation between User {user_id} and Event {event_id} not found",
            "EVENT_MEMBER_NOT_FOUND"
        )